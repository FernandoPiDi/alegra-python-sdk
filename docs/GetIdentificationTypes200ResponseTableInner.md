# GetIdentificationTypes200ResponseTableInner

Objeto que representa un elemento de la tabla

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | El código ante la DIAN que representa el elemento, este código es el que se debe enviar a la DIAN | [optional] 
**value** | **str** | Es la representación textual del elemento | [optional] 

## Example

```python
from openapi_client.models.get_identification_types200_response_table_inner import GetIdentificationTypes200ResponseTableInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetIdentificationTypes200ResponseTableInner from a JSON string
get_identification_types200_response_table_inner_instance = GetIdentificationTypes200ResponseTableInner.from_json(json)
# print the JSON string representation of the object
print(GetIdentificationTypes200ResponseTableInner.to_json())

# convert the object into a dict
get_identification_types200_response_table_inner_dict = get_identification_types200_response_table_inner_instance.to_dict()
# create an instance of GetIdentificationTypes200ResponseTableInner from a dict
get_identification_types200_response_table_inner_from_dict = GetIdentificationTypes200ResponseTableInner.from_dict(get_identification_types200_response_table_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


