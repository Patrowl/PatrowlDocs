- Data management:
	* export data into file: `python manage.py dumpdata assets.AssetCategory > var/data/assets.AssetCategory.json`
	* load data from file: `python manage.py loaddata var/data/assets.AssetCategory.json`
- RabbitMQ
	* start RMQ server: `sudo rabbitmq-server -detached`
	* stop RMQ server: `rabbitmqctl stop`
	* get status: `rabbitmqctl status`
- celery
	* start the celery workers: `celery -A app worker -l info -Q engine_nmapq,celery --purge --detach --logfile logs/celery.log`
	* start the celery beat scheduler: `celery -A app beat -l info -S django`
	* start Flower Web Monitor: `celery -A app flower --port=5555`
	* start Curse Monitor: `celery -A app events`
- Supervisord
	* Start the supervisor daemon: `supervisord -c etc/supervisord.conf`
	* Show status: `supervisorctl status`
	* Reload configuration: `supervisorctl reload`
	* Restart all engines workers: `supervisorctl restart celery-workers`
	* Restart nessus worker: `supervisorctl restart celery-workers:celery-nessus`
