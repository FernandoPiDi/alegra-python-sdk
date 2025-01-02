# CreateEvent200ResponseEventReceiver

Información relacionada al receptor del documento

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Número de identificación o NIT del receptor, sin guiones ni DV | [optional] 
**name** | **str** | Nombre o razón social del receptor | [optional] 
**identification_type** | **str** | Tipo de organización jurídica. Se debe colocar el Código que corresponda de la tabla de tipos de organización jurídica de la DIAN | [optional] 
**dv** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_event200_response_event_receiver import CreateEvent200ResponseEventReceiver

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEvent200ResponseEventReceiver from a JSON string
create_event200_response_event_receiver_instance = CreateEvent200ResponseEventReceiver.from_json(json)
# print the JSON string representation of the object
print(CreateEvent200ResponseEventReceiver.to_json())

# convert the object into a dict
create_event200_response_event_receiver_dict = create_event200_response_event_receiver_instance.to_dict()
# create an instance of CreateEvent200ResponseEventReceiver from a dict
create_event200_response_event_receiver_from_dict = CreateEvent200ResponseEventReceiver.from_dict(create_event200_response_event_receiver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


