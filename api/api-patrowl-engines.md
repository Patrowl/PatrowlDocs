# API Documentation for Patrowl Engines
| Format        | Link                                                         |
| ------------- |--------------------------------------------------------------|
| OpenApi 3.0   | [openapi-patrowl-engines.yaml](openapi-patrowl-engines.yaml) |
| JSON          | [openapi-patrowl-engines.json](openapi-patrowl-engines.json) |
| html          | [openapi-patrowl-engines.html](openapi-patrowl-engines.html) |

You can import the OpenApi YAML file in the swagger-editor or any other compatible client.


## Minimum Routes
All API responses are formatted in JSON.

| Path        | Method | Function |
| ------------|:------:|----------|
| `/engine/engine_name/` | GET | Index page |
| `/engine/engine_name/liveness` | GET | Liveness page (return 'OK'). Mostly for K8s purpose ;) |
| `/engine/engine_name/Readiness` | GET | Readiness page (return 'OK'). Mostly for K8s purpose ;) |
| `/engine/engine_name/test` | GET | Test page (list of available routes) |
| `/engine/engine_name/info` | GET | Engine information |
| `/engine/engine_name/clean` | GET | Clean all scans |
| `/engine/engine_name/clean/:scan_id` | GET | Clean scan identified by id |
| `/engine/engine_name/startscan` | POST | Start a new scan |
| `/engine/engine_name/stopscans` | GET | Stop all scans |
| `/engine/engine_name/stop/:scan_id` | GET | Stop scan identified by id |
| `/engine/engine_name/status` | GET | Status of all scans |
| `/engine/engine_name/status/:scan_id` | GET | Status of scan identified by id |
| `/engine/engine_name/getfindings/:scan_id` | GET | Findings of finished scan identified by id |
| `/engine/engine_name/getreport/:scan_id` | GET | I the scan is finished, return the report archive (Zip) |

## Workflow (minimalistic !)
When a scan is started by the Patrowl Manager (PM) instance, following steps are performed:
- The PM ask the status of the the Patrowl Engine (PE) --> `/status`.
- Status = "**READY**" means it's OK. So, PM prepares the scan parameters and send the POST request `/startscan` with the scan parameters in data header.
- Status = "**accepted**" means the scan is accepted by the engine. At least one internal thread is created to follow the scan steps. The status '**STARTED**'' is set to the scan context.
- The PM regularly check the scan engine using the `/status/:scan_id` method.
- If the scan is not finished or in error, the engine respond with the status '**SCANNING**'.
- If the scan status become '**FINISHED**', the PM call the method `/getfindings/:scan_id`... to retrieve the findings. The findings are then validated and imported in the internal DB. Risk calculations are then performed.
- Finally, the PM retrieve the scan report using the method `/getreport/:scan_id`. The report is a ZIP archive containing the findings JSON-formatted and, if any, the raw scan reports retrieved from the tools.

## Object states
### Engine:
| State   | Comments |
| --------|----------|
| READY   | The engine is ready to perform a new scan. |
| BUSY    | The engine has reached the maximum number of allowed scans started and not finished (see `APP_MAXSCANS` variable). |
| ERROR   | Something bad happened... Consider restarting the engine. |

### Scan:
| State      | Comments |
| -----------|----------|
| STARTED    | Cool ! The scan has been successfully started. The scan parameters has been validated and the engine was is a good mood. You rocks. |
| FINISHED   | Wow ! The scan has finished. You are now ready to call `/getfindings` and `/getreport` to collect hot findings. |
| SCANNING   | Wait ! The scan is not finished yet, or... has not reached the timeout. Take a coffee and come back later. |
| ERROR      | Huh ! Something bad happened. Consider reviewing the logs. |

## More
See `engines/engine_name/tests/` folder to discover examples (files used in the Travis build)
