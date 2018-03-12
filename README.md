# BTC-USD-Exchange-Rates-App

Django Application Displaying Exchange Rates For Bitcoin

## Running Using Docker

### Requirements

- Docker
- Docker-compose
- Git

Clone the repository into a directory of your own choice.

`git clone https://github.com/SamwelOpiyo/BTC-USD-Exchange-Rates-App.git`

`cd BTC-USD-Exchange-Rates-App`

### Starting the server

Build docker container

    $ docker-compose build

Start docker container

    $ docker-compose up or $ docker-compose up -d for daemon

Visit 127.0.0.1:8000 or 0.0.0.0:8000

## Running locally

### Requirements

- Python 2.7
- Make sure you have pip (pip --version)
- pip install virtualenv to install virtual environment
- Influxdb
- Redis-server
- Git

Clone the repository into a directory of your own choice.

`git clone https://github.com/SamwelOpiyo/BTC-USD-Exchange-Rates-App.git`

`cd BTC-USD-Exchange-Rates-App`

Edit the configuration file bitcoin_rates/settings.py appropriately or leave it for default redis-server and influxdb settings.

Start redis-server on a new terminal window/tab

- redis-server or redis-server -d for daemon mode

Start Influxdb

- systemctl start influxdb

Install requirements

- `pip install -r requirements.txt` (you almost certainly want to do this in a virtualenv).

Database Migration

- `python manage.py migrate`

Create logs directory

- mkdir logs

### Starting the server

Starting celery worker and beat

    $ celery -A bitcoin_rates -l info worker -B

Starting gunicorn server

    $ ./bash_scripts/start.sh

Visit 127.0.0.1:8000 or 0.0.0.0:8000
