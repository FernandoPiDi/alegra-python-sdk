# GetIdentificationTypes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | [**List[GetIdentificationTypes200ResponseTableInner]**](GetIdentificationTypes200ResponseTableInner.md) | Array con elementos disponibles para la DIAN | [optional] 

## Example

```python
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIdentificationTypes200Response from a JSON string
get_identification_types200_response_instance = GetIdentificationTypes200Response.from_json(json)
# print the JSON string representation of the object
print(GetIdentificationTypes200Response.to_json())

# convert the object into a dict
get_identification_types200_response_dict = get_identification_types200_response_instance.to_dict()
# create an instance of GetIdentificationTypes200Response from a dict
get_identification_types200_response_from_dict = GetIdentificationTypes200Response.from_dict(get_identification_types200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


