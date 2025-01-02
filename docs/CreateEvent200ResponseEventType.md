# CreateEvent200ResponseEventType

Tipo de evento emitido

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Código del evento emitido | [optional] 
**value** | **str** | Nombre del evento emitido | [optional] 

## Example

```python
from openapi_client.models.create_event200_response_event_type import CreateEvent200ResponseEventType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEvent200ResponseEventType from a JSON string
create_event200_response_event_type_instance = CreateEvent200ResponseEventType.from_json(json)
# print the JSON string representation of the object
print(CreateEvent200ResponseEventType.to_json())

# convert the object into a dict
create_event200_response_event_type_dict = create_event200_response_event_type_instance.to_dict()
# create an instance of CreateEvent200ResponseEventType from a dict
create_event200_response_event_type_from_dict = CreateEvent200ResponseEventType.from_dict(create_event200_response_event_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


