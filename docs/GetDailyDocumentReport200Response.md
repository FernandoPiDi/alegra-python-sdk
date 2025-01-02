# GetDailyDocumentReport200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_date** | **date** | Fecha del reporte | [optional] 
**report_document** | **str** | Tipo de documento del reporte | [optional] 
**report_url** | **str** | URL de descarga del reporte, link valido por 1 hora. | [optional] 

## Example

```python
from openapi_client.models.get_daily_document_report200_response import GetDailyDocumentReport200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDailyDocumentReport200Response from a JSON string
get_daily_document_report200_response_instance = GetDailyDocumentReport200Response.from_json(json)
# print the JSON string representation of the object
print(GetDailyDocumentReport200Response.to_json())

# convert the object into a dict
get_daily_document_report200_response_dict = get_daily_document_report200_response_instance.to_dict()
# create an instance of GetDailyDocumentReport200Response from a dict
get_daily_document_report200_response_from_dict = GetDailyDocumentReport200Response.from_dict(get_daily_document_report200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


