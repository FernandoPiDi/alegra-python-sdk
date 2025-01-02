# GetInvoiceEvents200ResponseEventsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Código del evento | [optional] 
**type** | **str** | Descripción del tipo de evento | [optional] 
**effective_time** | **str** | Fecha y hora de emisión del evento | [optional] 
**document_reference** | [**GetInvoiceEvents200ResponseEventsInnerDocumentReference**](GetInvoiceEvents200ResponseEventsInnerDocumentReference.md) |  | [optional] 
**issuer_party** | [**GetInvoiceEvents200ResponseEventsInnerIssuerParty**](GetInvoiceEvents200ResponseEventsInnerIssuerParty.md) |  | [optional] 
**receiver_party** | [**GetInvoiceEvents200ResponseEventsInnerReceiverParty**](GetInvoiceEvents200ResponseEventsInnerReceiverParty.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_invoice_events200_response_events_inner import GetInvoiceEvents200ResponseEventsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceEvents200ResponseEventsInner from a JSON string
get_invoice_events200_response_events_inner_instance = GetInvoiceEvents200ResponseEventsInner.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceEvents200ResponseEventsInner.to_json())

# convert the object into a dict
get_invoice_events200_response_events_inner_dict = get_invoice_events200_response_events_inner_instance.to_dict()
# create an instance of GetInvoiceEvents200ResponseEventsInner from a dict
get_invoice_events200_response_events_inner_from_dict = GetInvoiceEvents200ResponseEventsInner.from_dict(get_invoice_events200_response_events_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


