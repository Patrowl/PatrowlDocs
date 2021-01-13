- Data management:
	* export data into file: `python manage.py dumpdata assets.AssetCategory > var/data/assets.AssetCategory.json`
	* load data from file: `python manage.py loaddata var/data/assets.AssetCategory.json`
- RabbitMQ
	* start RabbitMQ server: `sudo rabbitmq-server -detached`
	* stop RabbitMQ server: `rabbitmqctl stop`
	* get status: `rabbitmqctl status`
- Supervisord
	* Start the supervisor daemon: `supervisord -c etc/supervisord.conf`
	* Shutdown the supervisor daemon: `supervisorctl shutdown`
	* Show status: `supervisorctl status`
	* Reload configuration: `supervisorctl reload`
	* Restart all engines workers: `supervisorctl restart celery-workers`
	* Restart nessus worker: `supervisorctl restart all`
