# GetSupportDocuments200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**GetPayrolls200ResponseMetadata**](GetPayrolls200ResponseMetadata.md) |  | [optional] 
**support_documents** | [**List[GetSupportDocuments200ResponseSupportDocumentsInner]**](GetSupportDocuments200ResponseSupportDocumentsInner.md) | Array con Documentos Soporte | [optional] 

## Example

```python
from openapi_client.models.get_support_documents200_response import GetSupportDocuments200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSupportDocuments200Response from a JSON string
get_support_documents200_response_instance = GetSupportDocuments200Response.from_json(json)
# print the JSON string representation of the object
print(GetSupportDocuments200Response.to_json())

# convert the object into a dict
get_support_documents200_response_dict = get_support_documents200_response_instance.to_dict()
# create an instance of GetSupportDocuments200Response from a dict
get_support_documents200_response_from_dict = GetSupportDocuments200Response.from_dict(get_support_documents200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


