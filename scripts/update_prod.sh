#!/usr/bin/env bash

set -ex

conda run -n "rizhiy.com-prod" --no-capture-output pip install -U .
sudo service waitress restart
sudo service nginx restart
