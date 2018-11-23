# API Documentation for Patrowl Engines
| Format        | Link        |
| ------------- |-------------|
| OpenApi 3.0   | [openapi-patrowl-engines.yaml](openapi-patrowl-engines.yaml) |
| JSON          | [openapi-patrowl-engines.json](openapi-patrowl-engines.json) |
| html          | [openapi-patrowl-engines.html](openapi-patrowl-engines.html) |


## Minimum Routes
| Path        | Method | Function |
| ------------ |----|-------------|
| ```/engine/engine_name/``` | GET | Index page |
| ```/engine/engine_name/liveness``` | GET | Liveness page (return 'OK') |
| ```/engine/engine_name/liveness``` | GET | Readiness page (return 'OK') |
| ```/engine/engine_name/liveness``` | GET | Readiness page (return 'OK') |
| ```/engine/engine_name/test``` | GET | Test page |
| ```/engine/engine_name/info``` | GET | Engine information |
| ```/engine/engine_name/clean``` | GET | Clean all scans |
| ```/engine/engine_name/clean/:*scan_id*``` | GET | Clean scan identified by id |
| ```/engine/engine_name/startscan``` | POST | Start a new scan |
| ```/engine/engine_name/stopscans``` | GET | Stop all scans |
| ```/engine/engine_name/stop/:*scan_id*``` | GET | Stop scan identified by id |
| ```/engine/engine_name/status``` | GET | Status of all scans |
| ```/engine/engine_name/status/:*scan_id*``` | GET | Status of scan identified by id |
| ```/engine/engine_name/getfindings/:*scan_id*``` | GET | Findings of finished scan identified by id |
| ```/engine/engine_name/getreport/:*scan_id*``` | GET | Findings of finished scan identified by id |


## Workflow
@todo
