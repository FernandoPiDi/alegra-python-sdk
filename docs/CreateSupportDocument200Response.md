# CreateSupportDocument200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**GetSupportDocuments200ResponseSupportDocumentsInner**](GetSupportDocuments200ResponseSupportDocumentsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_support_document200_response import CreateSupportDocument200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupportDocument200Response from a JSON string
create_support_document200_response_instance = CreateSupportDocument200Response.from_json(json)
# print the JSON string representation of the object
print(CreateSupportDocument200Response.to_json())

# convert the object into a dict
create_support_document200_response_dict = create_support_document200_response_instance.to_dict()
# create an instance of CreateSupportDocument200Response from a dict
create_support_document200_response_from_dict = CreateSupportDocument200Response.from_dict(create_support_document200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


