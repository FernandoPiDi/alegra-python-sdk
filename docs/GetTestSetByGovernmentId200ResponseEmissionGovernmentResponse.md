# GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse

Objeto con información de la respuesta de la DIAN

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Código de respuesta de la DIAN | [optional] 
**message** | **str** | Mensaje de respuesta de la DIAN | [optional] 
**error_messages** | **List[str]** | Array con mensajes de error devueltos por la DIAN | [optional] 

## Example

```python
from openapi_client.models.get_test_set_by_government_id200_response_emission_government_response import GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse from a JSON string
get_test_set_by_government_id200_response_emission_government_response_instance = GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse.from_json(json)
# print the JSON string representation of the object
print(GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse.to_json())

# convert the object into a dict
get_test_set_by_government_id200_response_emission_government_response_dict = get_test_set_by_government_id200_response_emission_government_response_instance.to_dict()
# create an instance of GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse from a dict
get_test_set_by_government_id200_response_emission_government_response_from_dict = GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse.from_dict(get_test_set_by_government_id200_response_emission_government_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


