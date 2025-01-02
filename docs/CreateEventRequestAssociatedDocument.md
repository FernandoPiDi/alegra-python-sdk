# CreateEventRequestAssociatedDocument

Objecto que contiene la información del documento de referencia

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | Prefijo del documento de referencia | [optional] 
**number** | **float** | Número del documento de referencia | 
**uuid** | **str** | CUFE del documento de referencia | 

## Example

```python
from openapi_client.models.create_event_request_associated_document import CreateEventRequestAssociatedDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventRequestAssociatedDocument from a JSON string
create_event_request_associated_document_instance = CreateEventRequestAssociatedDocument.from_json(json)
# print the JSON string representation of the object
print(CreateEventRequestAssociatedDocument.to_json())

# convert the object into a dict
create_event_request_associated_document_dict = create_event_request_associated_document_instance.to_dict()
# create an instance of CreateEventRequestAssociatedDocument from a dict
create_event_request_associated_document_from_dict = CreateEventRequestAssociatedDocument.from_dict(create_event_request_associated_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


