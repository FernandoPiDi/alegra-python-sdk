# CreateDebitNote200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debit_note** | [**GetDebitNotes200ResponseInvoicesInner**](GetDebitNotes200ResponseInvoicesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_debit_note200_response import CreateDebitNote200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDebitNote200Response from a JSON string
create_debit_note200_response_instance = CreateDebitNote200Response.from_json(json)
# print the JSON string representation of the object
print(CreateDebitNote200Response.to_json())

# convert the object into a dict
create_debit_note200_response_dict = create_debit_note200_response_instance.to_dict()
# create an instance of CreateDebitNote200Response from a dict
create_debit_note200_response_from_dict = CreateDebitNote200Response.from_dict(create_debit_note200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


