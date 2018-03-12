#!/bin/sh

echo "***********************************************"
echo "***************** install *********************"
echo "***********************************************"

echo "***********************************************"
echo "---install dependencies (including django)  ---"
echo "***********************************************"
# install requirements
pip install -r requirements.txt
# show installed python modules
pip freeze
