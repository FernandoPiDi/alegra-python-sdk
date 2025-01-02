# GetCreditNotes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**GetPayrolls200ResponseMetadata**](GetPayrolls200ResponseMetadata.md) |  | [optional] 
**invoices** | [**List[GetCreditNotes200ResponseInvoicesInner]**](GetCreditNotes200ResponseInvoicesInner.md) | Array con Notas Crédito / Documentos | [optional] 

## Example

```python
from openapi_client.models.get_credit_notes200_response import GetCreditNotes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCreditNotes200Response from a JSON string
get_credit_notes200_response_instance = GetCreditNotes200Response.from_json(json)
# print the JSON string representation of the object
print(GetCreditNotes200Response.to_json())

# convert the object into a dict
get_credit_notes200_response_dict = get_credit_notes200_response_instance.to_dict()
# create an instance of GetCreditNotes200Response from a dict
get_credit_notes200_response_from_dict = GetCreditNotes200Response.from_dict(get_credit_notes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


