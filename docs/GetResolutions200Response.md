# GetResolutions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolutions** | [**List[GetResolutions200ResponseResolutionsInner]**](GetResolutions200ResponseResolutionsInner.md) | Array con el listato de Resoluciones o Rangos de Numeración | [optional] 

## Example

```python
from openapi_client.models.get_resolutions200_response import GetResolutions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetResolutions200Response from a JSON string
get_resolutions200_response_instance = GetResolutions200Response.from_json(json)
# print the JSON string representation of the object
print(GetResolutions200Response.to_json())

# convert the object into a dict
get_resolutions200_response_dict = get_resolutions200_response_instance.to_dict()
# create an instance of GetResolutions200Response from a dict
get_resolutions200_response_from_dict = GetResolutions200Response.from_dict(get_resolutions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


