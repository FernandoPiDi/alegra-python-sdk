# GetCreditNote200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_note** | [**GetCreditNotes200ResponseInvoicesInner**](GetCreditNotes200ResponseInvoicesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_credit_note200_response import GetCreditNote200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCreditNote200Response from a JSON string
get_credit_note200_response_instance = GetCreditNote200Response.from_json(json)
# print the JSON string representation of the object
print(GetCreditNote200Response.to_json())

# convert the object into a dict
get_credit_note200_response_dict = get_credit_note200_response_instance.to_dict()
# create an instance of GetCreditNote200Response from a dict
get_credit_note200_response_from_dict = GetCreditNote200Response.from_dict(get_credit_note200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


