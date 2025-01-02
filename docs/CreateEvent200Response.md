# CreateEvent200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**CreateEvent200ResponseEvent**](CreateEvent200ResponseEvent.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_event200_response import CreateEvent200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEvent200Response from a JSON string
create_event200_response_instance = CreateEvent200Response.from_json(json)
# print the JSON string representation of the object
print(CreateEvent200Response.to_json())

# convert the object into a dict
create_event200_response_dict = create_event200_response_instance.to_dict()
# create an instance of CreateEvent200Response from a dict
create_event200_response_from_dict = CreateEvent200Response.from_dict(create_event200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


