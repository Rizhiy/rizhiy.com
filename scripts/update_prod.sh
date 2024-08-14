#!/usr/bin/env bash

set -ex

conda run -n "rizhiy.com-prod" --no-capture-output pip install .
sudo service waitress restart
