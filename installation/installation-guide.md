# Installation Guide
Before installing PatrOwl, you need to choose the installation option which suits your environment as described below.

## Table of Contents
+ [Hardware Pre-requisites](#hardware-pre-requisites)
+ [Backend Deployment Steps](#backend-deployment-steps)
  - [Install and deploy PatrOwl-Manager Backend from Docker](#install-and-deploy-backend-from-docker)
  - [Or, install and deploy Backend from Sources](#install-and-deploy-backend-from-sources)
+ [Engines Deployment Steps](#engines-deployment-steps)
  - [Install and deploy PatrOwl Engines from Docker](#install-and-deploy-engines-from-docker)
  - [Or, install and deploy Engines from Sources](#install-and-deploy-engines-from-sources)
+ [Useful Commands](#useful-commands)

## Hardware Pre-requisites
PatrOwl-Manager uses PosgreSQL to store data. We recommend using a virtual machine with at least 4vCPU, 8 GB of RAM and 60 GB of disk. You can also use a physical machine with similar specifications.

## Backend Deployment Steps
### Install and deploy Backend from Docker
@In progress (Docker Compose)

### Install and deploy Backend from Sources
The following section contains a step-by-step guide to build PatrOwl from its sources.

#### 1. Pre-requisites
The following software are required to download and run PatrOwl:
+ [PosgreSQL](https://www.postgresql.org/download/)
+ [GIT](http://www.git-scm.com/downloads)
+ [Python2.7](https://www.python.org/download/releases/2.7/)
+ [Python pip](https://pip.pypa.io/en/stable/installing/)
+ [Python virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
+ [RabbitMQ](https://www.rabbitmq.com)
+ [Docker](https://docs.docker.com/install/) if needed (not described below)

We strongly recommend to use the system package.

##### 2. Install required packages
To install the requirements and run PatrOwl from sources, please follow the instructions below depending on your operating system.

###### 2.1. MacOS/X
Using `brew`:
```
brew update
brew install postgres python rabbitmq
sudo python -m ensurepip
sudo pip install virtualenv
```

###### 2.2. Ubuntu 16.04+
```
apt-get install git python python-pip virtualenv rabbitmq-server postgresql
```

###### 2.3. CentOS/RHEL
```
yum install -y git python python-pip python-virtualenv rabbitmq-server postgresql
```

##### 3. Download PatrOwl and install python dependencies
```
git clone https://github.com/Patrowl/patrowl.git
cd patrowl/backoffice
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
> Be careful, next commands MUST be launched within the python virtual environment. The prefix `(env)` should appear in the command prompt. Ex:
```
(env) GreenLock@GL01:backoffice$ ls
```
If you open another terminal, please enter in the virtualenv with the command `source env/bin/activate`.

##### 4. Begin backend configuration
+ Copy `app/settings.py.sample` to `app/settings.py` and update at least following options:
	- Application settings `ALLOWED_HOSTS`, `LOGGING_LEVEL`, `PROXIES`, `SECRET_KEY`,
  - DB settings (service location and credentials): `DATABASES`,
  - RabbitMQ settings (service location and credentials): `BROKER_URL`,
	- Email settings (alerting): `EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_HOST_PORT`
+ Create the Django superuser:
```
python manage.py createsuperuser
```
> Please keep these credentials in a safe place. This account will be used for the first login on the PatrOwl Manager application

##### 5. Configure, create and populate the database
+ Edit file the `var/db/create_user_and_db.sql` and update the user and password values (default values are: PATROWL_DB_USER and PATROWL_DB_PASSWD_TO_CHANGE)

+ Execute the SQL script:
```
psql -U postgres < var/db/create_user_and_db.sql
```
+ Update the configuration file `app/settings.py` with these db credentials

+ Create the db schema using the Django commands:
```
python manage.py makemigrations
python manage.py migrate
```

+ Populate the db with default data (AssetCategory, EnginePolicy, ...)
```
python manage.py loaddata var/data/assets.AssetCategory.json
python manage.py loaddata var/data/engines.Engine.json
python manage.py loaddata var/data/engines.EnginePolicyScope.json
python manage.py loaddata var/data/engines.EnginePolicy.json
```

##### 6. Start the Django backend server
```
supervisord -c var/etc/supervisord.conf
python manage.py runserver_plus 0.0.0.0:8000
```

## Engines deployment steps
### Install and deploy PatrOwl engines from Docker
#### 1. Build the Docker images
+ Build the Docker images separately. Ex:
```
cd patrowl/engines/nmap
docker build --quiet --tag "nmap_docker" .
```
+ Or, using the script `engines/build-docker-engines.sh`
```
cd patrowl/engines
./build-docker-engines.sh
```
#### 2. Run Docker containers
+ Start the docker containers separately (be careful to correctly map your JSON configuration files as a volume). Ex:
```
docker run -d --rm -p 5101:5001 --name="nmap-docker-001" nmap_docker
docker run -d --rm -p 5106:5006 --name="owldns-docker-001" -v $PWD/engines/owl_dns/owl_dns.json:/opt/patrowl-engines/owl_dns/owl_dns.json:ro owldns_docker
docker run -d --rm -p 5107:5007 --name="virustotal-docker-001" -v $PWD/engines/virustotal/virustotal.json:/opt/patrowl-engines/virustotal/virustotal.json:ro virustotal_docker
```
+ Or, using the script `engines/start-docker-engines.sh`
```
./start-docker-engines.sh
```

### Install and deploy PatrOwl engines from Sources
#### 1. Configure engines
Please refer to README files from each engine directory. Configuration files are the JSON files and parameters are quite straightforward.
For each engine, copy the  `<engine_name>.json.sample` file to `<engine_name>.json` and edit the new file.

#### 2. Start PatrOwl engines
Start the engines using the script `engines/start-engines.sh`:
```
./start-engines.sh
```

## Useful commands
+ See the __[Useful Commands](install/useful-commands.md)__ guide
