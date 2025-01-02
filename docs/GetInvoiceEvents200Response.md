# GetInvoiceEvents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** | Indica la validez de la factura electrónica | [optional] 
**error_messages** | **List[str]** | Lista de mensajes de error | [optional] 
**status_code** | **str** | Código regresado por la DIAN | [optional] 
**status_description** | **str** | Significado del código regresado por la DIAN | [optional] 
**events** | [**List[GetInvoiceEvents200ResponseEventsInner]**](GetInvoiceEvents200ResponseEventsInner.md) | Eventos asociados a la factura electrónica | [optional] 
**xml_base64** | **str** | Documento xml obtenido como respuesta de la DIAN, se regresa en base64 y únicamente cuando se indica en la url [?xmlbase64&#x3D;true] como un query param | [optional] 

## Example

```python
from openapi_client.models.get_invoice_events200_response import GetInvoiceEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceEvents200Response from a JSON string
get_invoice_events200_response_instance = GetInvoiceEvents200Response.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceEvents200Response.to_json())

# convert the object into a dict
get_invoice_events200_response_dict = get_invoice_events200_response_instance.to_dict()
# create an instance of GetInvoiceEvents200Response from a dict
get_invoice_events200_response_from_dict = GetInvoiceEvents200Response.from_dict(get_invoice_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


