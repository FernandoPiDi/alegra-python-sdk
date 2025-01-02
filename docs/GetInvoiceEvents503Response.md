# GetInvoiceEvents503Response

Objeto de la respuesta de error de comunicación

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[GetDailyDocumentReport400ResponseInner]**](GetDailyDocumentReport400ResponseInner.md) | Array que contiene N errores generados en el sistema | [optional] 

## Example

```python
from openapi_client.models.get_invoice_events503_response import GetInvoiceEvents503Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceEvents503Response from a JSON string
get_invoice_events503_response_instance = GetInvoiceEvents503Response.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceEvents503Response.to_json())

# convert the object into a dict
get_invoice_events503_response_dict = get_invoice_events503_response_instance.to_dict()
# create an instance of GetInvoiceEvents503Response from a dict
get_invoice_events503_response_from_dict = GetInvoiceEvents503Response.from_dict(get_invoice_events503_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


