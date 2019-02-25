# Installation Guide
Before installing PatrOwl, you need to choose the installation option which suits your environment as described below.

## Table of Contents
+ [Hardware Pre-requisites](#hardware-pre-requisites)
+ [PatrowlManager Deployment Steps](#patrowlmanager-deployment-steps)
  - [Install and deploy PatrOwl-Manager Backend from Docker](#install-and-deploy-backend-from-docker)
  - [Or, install and deploy Backend from Sources](#install-and-deploy-backend-from-sources)
+ [Patrowl Engines Deployment Steps](#patrowl-engines-deployment-steps)
  - [Download PatrowlEngines from GitHub](#download-patrowlengines-from-gitHub)
  - [Deploy PatrOwl Engines from Docker images](#deploy-engines-from-docker-images)
  - [Or, deploy Engines from Sources](#deploy-engines-from-sources)
+ [Useful Commands](#useful-commands)

## Hardware Pre-requisites
PatrOwlManager uses PosgreSQL to store data. We recommend using a virtual machine with at least 4vCPU, 8 GB of RAM and 60 GB of disk. You can also use a physical machine with similar specifications.

## PatrowlManager Deployment Steps

### Install and deploy Backend from Docker
#### 1. Install system pre-requisites
Install Docker:
+ [Docker and Docker-Compose](https://docs.docker.com/install/)

#### 2. Download PatrowlManager from GitHub
```
git clone https://github.com/Patrowl/PatrowlManager.git
```
#### 3. Deploy the backend using docker-compose
```
cd PatrowlManager
docker-compose build --force-rm
docker-compose up
```
> Note: Persistent volume is not set in the default db configuration. Activate this if needed (it should be !). Adjust it in the `docker-compose.yml` file

#### 4. Use it
Go to http://localhost:8083/ and sign in with default admin credentials : admin/Bonjour1!

### Install and deploy Backend from Sources
The following section contains a step-by-step guide to build PatrOwl from its sources.

#### 1. Install system pre-requisites
The following software are required to download and run PatrOwl:
+ [PosgreSQL](https://www.postgresql.org/download/)
+ [Git client](http://www.git-scm.com/downloads)
+ [Python2.7](https://www.python.org/download/releases/2.7/)
+ [Python pip](https://pip.pypa.io/en/stable/installing/)
+ [Python virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
+ [RabbitMQ](https://www.rabbitmq.com)


We strongly recommend to use the system packages.

##### 2. Install required packages
To install the requirements and run PatrOwl from sources, please follow the instructions below depending on your operating system.

###### 2.1. MacOS/X
Using `brew`:
```
brew update
brew install postgres python rabbitmq
python -m ensurepip
pip install virtualenv
```

###### 2.2. Ubuntu 16.04/18.04 LTS
```
sudo apt install build-essential python2.7 python2.7-dev git curl rabbitmq-server postgresql
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py
rm get-pip.py
sudo pip install virtualenv
```

###### 2.3. CentOS/RHEL
```
yum install -y git python python-pip python-virtualenv rabbitmq-server postgresql
```

##### 3. Download PatrowlManager from GitHub
```
git clone https://github.com/Patrowl/PatrowlManager.git
```

##### 4. Install python dependencies
```
cd PatrowlManager
python2.7 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
> Note 1: if `python2.7 -m virtualenv env` does not work, please consider the command `virtualenv env` but ensure that Python2 is selected.  
> Note 2: Be careful, next commands MUST be launched within the python virtual environment. The prefix `(env)` should appear in the command prompt. Ex:
```
(env) GreenLock@GL01:PatrowlManager$ ls
```
If you open another terminal, please enter in the virtualenv with the command `source env/bin/activate`. If you want to exit the virtual environment, use the command `deactivate`.

##### 5. Create the PosgreSQL database
###### 5.1. Method 1 (fast but unsecure)
+ Edit file the `var/db/create_user_and_db.sql` and update the user and password values (default values are: PATROWL_DB_USER and PATROWL_DB_PASSWD_TO_CHANGE)

###### 5.1.1. MacOS
+ Execute the SQL script:
```
psql < var/db/create_user_and_db.sql
```

###### 5.1.2. Ubuntu 16.04/18.04 LTS
+ Execute the SQL script:
```
sudo -u postgres psql < var/db/create_user_and_db.sql
```

###### 5.2. Method 2 (slow but more secure)
+ Connect to the PostgreSQL CLI `psql`:
```
sudo -u postgres psql
```

+ Create the user and database:
```
CREATE USER "PATROWL_DB_USER" WITH PASSWORD 'PATROWL_DB_PASSWD_TO_CHANGE';
CREATE DATABASE "patrowl_db" WITH OWNER "PATROWL_DB_USER";
```

+ Set the next attributes for PATROWL_DB_USER:
```
ALTER ROLE "PATROWL_DB_USER" SET client_encoding TO 'utf8';
ALTER ROLE "PATROWL_DB_USER" SET default_transaction_isolation TO 'read committed';
-- ALTER ROLE "PATROWL_DB_USER" SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE "patrowl_db" TO "PATROWL_DB_USER";
```

##### 6. Configure PatrowlManager (Django backend) application
+ Copy `app/settings.py.sample` to `app/settings.py` and update at least following options:
  * Application settings `ALLOWED_HOSTS`, `LOGGING_LEVEL`, `PROXIES`, `SECRET_KEY`
  * DB settings (service location and credentials): `DATABASES`,  
  * RabbitMQ settings (service location and credentials): `BROKER_URL` (default values are `guest/guest`),
  * Email settings (alerting): `EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_HOST_PORT`
+ Create the db schema using the Django commands:
```
python manage.py makemigrations
python manage.py migrate
```

+ Collect static files (produciton mode - files copied to /staticfiles/):
```
python manage.py collectstatic
```

+ Create the Django superuser:
```
python manage.py createsuperuser
```
> Please keep these credentials in a safe place. This account will be used for the first login on the PatrowlManager application

+ Populate the db with default data (AssetCategory, EnginePolicy, ...):
```
python manage.py loaddata var/data/assets.AssetCategory.json
python manage.py loaddata var/data/engines.Engine.json
python manage.py loaddata var/data/engines.EnginePolicyScope.json
python manage.py loaddata var/data/engines.EnginePolicy.json
```

##### 7. Start the Django backend server (development)
###### 7.1 Testing environment
+ Start Supervisord (Celery workers)
```
supervisord -c var/etc/supervisord.conf
```

+ Then, the Django application:
```
python manage.py runserver_plus 0.0.0.0:8000
```
+ or, using Gunicorn (recommended) :
```
gunicorn app.wsgi:application [-b 0.0.0.0:8000] [--access-logfile -]
```

###### 7.2 Production environment (Nginx serving static files)
+ Open the `app/settings.py` file and set the variable `DEBUG=True`.
+ Follow the same steps for starting the development environment (see #7.1)
+ Customize the `nginx.conf` file provided. Then start it:
```
[sudo] nginx -p .
```

## Patrowl Engines deployment steps
### Download PatrowlEngines from GitHub
```
git clone https://github.com/Patrowl/PatrowlEngines.git
cd PatrowlEngines
```

### Configure Patrowl Engines
Configuration files are the JSON files and parameters are quite straightforward. For each engine, copy the  `<engine_name>.json.sample` file to `<engine_name>.json` and edit the new file.
Please refer to the README files from each engine directory.

### Deploy Engines from Docker Images
#### 1. Build the Docker images
+ Build the Docker images separately. Ex:
```
cd engines/virustotal
docker build --quiet --tag "patrowl-virustotal" .
```
+ Or, using the script `scripts/build-docker-engines.sh` to build all docker containers:
```
scripts/build-docker-engines.sh
```
#### 2. Run local Docker containers
+ Start the docker containers separately (be careful to correctly map your JSON configuration files as a volume). Ex:
```
docker run -d --rm -p 5101:5001 --name="nmap-docker-001" patrowl-nmap
docker run -d --rm -p 5106:5006 --name="owldns-docker-001" -v $PWD/engines/owl_dns/owl_dns.json:/opt/patrowl-engines/owl_dns/owl_dns.json:ro patrowl-owldns
docker run -d --rm -p 5107:5007 --name="virustotal-docker-001" -v $PWD/engines/virustotal/virustotal.json:/opt/patrowl-engines/virustotal/virustotal.json:ro patrowl-virustotal
```

> Note: The full path to the configuration file must be passed to docker in order to correctly mount it to the container as a valid volume. That's why `$PWD` is added.

+ Or, using the script `start-docker-engines.sh` to start all the containers:
```
scripts/start-docker-engines.sh
```

### Deploy Engines from Sources
##### 1. Install required packages
```
sudo apt install build-essential python2.7-dev
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py
rm get-pip.py
sudo pip install virtualenv
```

##### 2. Install python dependencies
Use the script `install-engines.sh` from folder `scripts` to install all engines and their dependencies:
```
cd scripts
./install-engines.sh
```

or, install manually dependencies for each engine. Ex:
```
cd engines/nmap
python2.7 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

#### 3. Start the PatrOwl engines
Start engines one-by-one (within the current engine virtualenv). Ex:
```
[sudo] env/bin/python engine-virustotal.py [--host=0.0.0.0] [--port=5007] [--debug]
```

Or, using Gunicorn:
```
[sudo] gunicorn engine-virustotal:app [0.0.0.0:5007]
```
> Useful hint: sudo is needed to start the 'nmap' engine.

Or, start all engines using the script `start-engines.sh`:
```
[sudo] scripts/start-engines.sh
```

## Useful commands
+ See the __[Useful Commands](useful-commands.md)__ guide
