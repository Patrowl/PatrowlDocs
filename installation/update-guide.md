# Update Guide
You already installed [PatrowlManager](https://github.com/Patrowl/PatrowlManager) and/or [PatrowlEngines](https://github.com/Patrowl/PatrowlEngines). A new version is available and you want to update your installation. Great idea !

## PatrowlManager
### Native installation (non-Docker)
- [ ] Stop running scans and temporary disable periodic scans
- [ ] Stop Celery workers (supervisord): `supervisorctl shutdown`
- [ ] Backup your database
```
pg_dump -U <postgres_db_username> -W -F c patrowl_db -f /opt/patrowlmanager/save/db.tar
```
- [ ] Backup all your configuration files, including:
  * Django/web: env vars: `set > /opt/patrowlmanager/save/.env`
  * Django/web: application settings file: `cp app/settings.py /opt/patrowlmanager/save/settings.py`
  * Django/Web: log files: `cp var/log/* /opt/patrowlmanager/save/log/`
  * Django/Web: static files: `cp staticfiles/* /opt/patrowlmanager/save/staticfiles/`
  * Django/Web: media files: `cp media/* /opt/patrowlmanager/save/media/`
  * Nginx: configuration file: `cp /etc/nginx/conf.d/default.conf /opt/patrowlmanager/save/patrowlmanager_nginx.conf`
- [ ] Update the application files: `git fetch && git pull`
- [ ] Install potential python module updates: `pip install -U -r requirements.txt`
- [ ] Update `app/settings.py` from the sample with potential new/old configuration variables
- [ ] Update static files: `python manage.py collectstatic —noinput`
- [ ] Update DB schema (if already created): `var/bin/update_db_migrations.sh`
- [ ] Prepare potential changes in model defintitions (plz respect the order) :
```
python manage.py makemigrations scans
python manage.py makemigrations findings
python manage.py makemigrations events
python manage.py makemigrations
```
- [ ] Apply potential changes in DB: `python manage.py migrate`
- [ ] (Re-)Load default data:
```
python manage.py loaddata var/data/assets.AssetCategory.json
python manage.py loaddata var/data/engines.Engine.json
python manage.py loaddata var/data/engines.EnginePolicyScope.json
python manage.py loaddata var/data/engines.EnginePolicy.json
```
- [ ] Create the default admin user (if not exists): `python manage.py shell < var/bin/create_default_admin.py`
- [ ] Create default team (if not exists): `python manage.py shell < var/bin/create_default_team.py`
- [ ] Restart Celery workers (supervisord): `supervisorctl reload-c var/etc/supervisord.conf`
- [ ] Restart Web server (Gunicorn): `gunicorn -b 0.0.0.0:8003 app.wsgi:application --timeout 300`
- [ ] Restart service Nginx: `sudo nginx -s reload`
- [ ] Login and enable again your periodic scans
- [ ] Give us feedback: [getsupport@patrowl.io](mailto:getsupport@patrowl.io?subject=Migration%20successful)
