# REST-API Documentation for PatrowlHears
| Format        | Link                                                         |
| ------------- |--------------------------------------------------------------|
| OpenApi 3.0   | [patrowl-hears-openapi.yaml](patrowl-hears-openapi.yaml) |
| Swagger-JSON  | [patrowl-hears-swagger.json](patrowl-hears-swagger.json) |

You can import the OpenApi YAML file in the swagger-editor or any other compatible client.
A Web-based client for REST-API endpoints is also available at url `/api/docs/swagger/` or `/api/docs/redoc/`.

## Token Authentication
Example:

`curl -X GET http://127.0.0.1:8000/assets/api/v1/list -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'`
