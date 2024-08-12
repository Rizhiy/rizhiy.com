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
	conda run -n "$env_name" pip install .
fi

# Change to another dir to make sure that app in environment gets used
cd /tmp
conda run -n "$env_name" flask --app rizhiy_com --debug init-db
cd -

sudo cp -f other/waitress.service /etc/systemd/system/
sudo systemctl enable waitress
sudo systemctl restart waitress
