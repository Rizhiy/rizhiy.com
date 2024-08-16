#!/usr/bin/env bash

set -ex

config_name="rizhiy_com.nginx"
env_name="rizhiy.com-prod"

sudo apt install nginx
sudo ln -sf "$(pwd)"/other/"$config_name" /etc/nginx/sites-available/
cd /etc/nginx/sites-enabled/
sudo ln -sf ../sites-available/"$config_name" .
sudo rm -f default
cd -
sudo service nginx restart


if [[ ! $(conda env list | grep "$env_name") >/dev/null ]]; then
	conda create -n "$env_name" python=3.12 -y
	conda run -n "$env_name" --no-capture-output pip install .
fi

# Change to another dir to make sure that app in environment gets used
cd /tmp
conda run -n "$env_name" flask --app rizhiy_com --debug init-db
cd -

sudo cp -f other/waitress.service /etc/systemd/system/
sudo systemctl enable waitress
sudo systemctl restart waitress

# Setup Let's Encrypt
conda run -n "$env_name" --no-capture-output pip install certbot certbot-nginx
certbot_exe="$(conda run -n "$env_name" which certbot)"
pip_exe="$(conda run -n "$env_name" which pip)"
sudo "$certbot_exe" run --nginx -d rizhiy.ddns.net -n
sudo service nginx restart
## Setup update
echo "0 0,12 * * * root python -c 'import random; import time; time.sleep(random.random() * 1800)' && sudo "$certbot_exe" renew -q" | sudo tee -a /etc/crontab > /dev/null
echo "0 1 1 * * root python -c 'import random; import time; time.sleep(random.random() * 1800)' && sudo "$pip_exe" install -U certbot certbot-nginx" | sudo tee -a /etc/crontab > /dev/null
