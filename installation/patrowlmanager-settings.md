# Environment variable
Variable                       | Default Value                | PRO only | Comments
------------------------------ | ---------------------------- | -------- | --------
DEBUG                          | True                         | no       | Enable/Disable Django DEBUG mode
LOGGING_LEVEL                  | INFO,WARNING,ERROR,DEBUG     | no       | LOGGING levels (comma-separated)
ENGINE_HTTP_TIMEOUT            | 600                          | no       | Max timeout for HTTP requests from Manager to Engine
SCAN_JOB_DEFAULT_TIMEOUT       | 7200                         | no       | Max timeout for each scan job
SCAN_JOB_DEFAULT_SPLIT_ASSETS  | 100                          | no       | Max assets by scan job (override with 'max_scanjob_timeout' value in engin policy options)
PRO_EDITION                    | False                        | yes      | Enable/Disable PRO features (only compatible with PRO plugins)
PATROWL_ASSETS_MAX             | 100000000                    | yes      | Max number of allowed assets
PATROWL_ASSETS_MARGIN          | 10                           | yes      | % of overload allowed assets
PATROWL_ASSETGROUPS_MAX        | 100000000                    | yes      | Max number of allowed asset groups
PATROWL_USERS_MAX              | 5                            | yes      | Max number of allowed users
PATROWL_SCAN_DEFINITIONS_MAX   | 5                            | yes      | Max number of allowed scan definitions
PATROWL_FINDINGS_MAX           | -1                           | yes      | Max number of allowed findings (old ones are automatically purged). -1 for unlimited
PATROWL_ENGINES_MAX            | 5                            | yes      | Max number of allowed engine slots
PATROWL_ENGINE_POLICIES_MAX    | 100                          | yes      | Max number of allowed engine policies
PATROWL_ENGINES_MANAGE_ENABLED | True                         | yes      | Enable/Disable management of engines
PATROWL_REFRESH_ENGINE         | 7000                         | no       | Enable/Disable management of engines
EMAIL_USE_TLS                  | True                         | no       | Enable/Disable TLS support for SMTP access
EMAIL_HOST                     | ''                           | no       | SMTP Host
EMAIL_PORT                     | 587                          | no       | SMTP Port
EMAIL_HOST_USER                | ''                           | no       | SMTP Username
EMAIL_HOST_PASSWORD            | ''                           | no       | SMTP Password
PATROWL_TZ                     | Europe/Paris                 | no       | Timezone
DB_ENV_DB                      | patrowl_db                   | no       | PostgreSQL Database name
DB_ENV_POSTGRES_USER           | PATROWL_DB_USER              | no       | PostgreSQL Database username
DB_ENV_POSTGRES_PASSWORD       | PATROWL_DB_PASSWD_TO_CHANGE  | no       | PostgreSQL Database password
DB_PORT_5432_TCP_HOST          | localhost                    | no       | PostgreSQL Database hostname
DB_PORT_5432_TCP_PORT          | 5432                         | no       | PostgreSQL Database TCP/port
DB_ENV_POSTGRES_OPTIONS        | 5432                         | no       | PostgreSQL Database options
RABBIT_PORT_5672_TCP           | localhost:5672               | no       | RabbitMQ hostname + port
RABBIT_ENV_USER                | guest                        | no       | RabbitMQ hostname
RABBIT_ENV_RABBITMQ_PASS       | guest                        | no       | RabbitMQ password
RABBIT_ENV_VHOST               | ''                           | no       | RabbitMQ password
SUPERVISORD_API_URL            | http://localhost:9001/RPC2   | no       | RabbitMQ password
PATROWL_PROXY_HTTP             | None                         | no       | Proxy URL for HTTP requests
PATROWL_PROXY_HTTPS            | None                         | no       | Proxy URL for HTTPS requests


# Alert notification settings
Scope   | Setting                        | Examples
------- | ------------------------------ | -----------
TheHive | alerts.endpoint.thehive.apikey | -
TheHive | alerts.endpoint.thehive.url    | -
TheHive | alerts.endpoint.thehive.user   | -
Slack | alerts.endpoint.slack.webhook    | -
Slack | alerts.endpoint.slack.channel    | -
Email | alerts.endpoint.email            | -
