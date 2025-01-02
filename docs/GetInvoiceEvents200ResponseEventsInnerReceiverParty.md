# GetInvoiceEvents200ResponseEventsInnerReceiverParty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identification_number** | **str** | Número de identificación del receptor del evento | [optional] 
**name** | **str** | Nombre o razón social del receptor del evento | [optional] 

## Example

```python
from openapi_client.models.get_invoice_events200_response_events_inner_receiver_party import GetInvoiceEvents200ResponseEventsInnerReceiverParty

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceEvents200ResponseEventsInnerReceiverParty from a JSON string
get_invoice_events200_response_events_inner_receiver_party_instance = GetInvoiceEvents200ResponseEventsInnerReceiverParty.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceEvents200ResponseEventsInnerReceiverParty.to_json())

# convert the object into a dict
get_invoice_events200_response_events_inner_receiver_party_dict = get_invoice_events200_response_events_inner_receiver_party_instance.to_dict()
# create an instance of GetInvoiceEvents200ResponseEventsInnerReceiverParty from a dict
get_invoice_events200_response_events_inner_receiver_party_from_dict = GetInvoiceEvents200ResponseEventsInnerReceiverParty.from_dict(get_invoice_events200_response_events_inner_receiver_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


