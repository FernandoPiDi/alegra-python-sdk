# GetDailyDocumentReport400ResponseInner

Objeto que representa un error en el sistema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Código de error | [optional] 
**message** | **str** | Mensaje de error | 

## Example

```python
from openapi_client.models.get_daily_document_report400_response_inner import GetDailyDocumentReport400ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDailyDocumentReport400ResponseInner from a JSON string
get_daily_document_report400_response_inner_instance = GetDailyDocumentReport400ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetDailyDocumentReport400ResponseInner.to_json())

# convert the object into a dict
get_daily_document_report400_response_inner_dict = get_daily_document_report400_response_inner_instance.to_dict()
# create an instance of GetDailyDocumentReport400ResponseInner from a dict
get_daily_document_report400_response_inner_from_dict = GetDailyDocumentReport400ResponseInner.from_dict(get_daily_document_report400_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


