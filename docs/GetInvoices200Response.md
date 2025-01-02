# GetInvoices200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**GetPayrolls200ResponseMetadata**](GetPayrolls200ResponseMetadata.md) |  | [optional] 
**invoices** | [**List[GetInvoices200ResponseInvoicesInner]**](GetInvoices200ResponseInvoicesInner.md) | Array con facturas | [optional] 

## Example

```python
from openapi_client.models.get_invoices200_response import GetInvoices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoices200Response from a JSON string
get_invoices200_response_instance = GetInvoices200Response.from_json(json)
# print the JSON string representation of the object
print(GetInvoices200Response.to_json())

# convert the object into a dict
get_invoices200_response_dict = get_invoices200_response_instance.to_dict()
# create an instance of GetInvoices200Response from a dict
get_invoices200_response_from_dict = GetInvoices200Response.from_dict(get_invoices200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


