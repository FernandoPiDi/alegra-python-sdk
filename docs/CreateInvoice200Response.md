# CreateInvoice200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**GetInvoices200ResponseInvoicesInner**](GetInvoices200ResponseInvoicesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_invoice200_response import CreateInvoice200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoice200Response from a JSON string
create_invoice200_response_instance = CreateInvoice200Response.from_json(json)
# print the JSON string representation of the object
print(CreateInvoice200Response.to_json())

# convert the object into a dict
create_invoice200_response_dict = create_invoice200_response_instance.to_dict()
# create an instance of CreateInvoice200Response from a dict
create_invoice200_response_from_dict = CreateInvoice200Response.from_dict(create_invoice200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


