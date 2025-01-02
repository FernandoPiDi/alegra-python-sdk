# AssociatedDocument

Objeto que contiene la información del documento referencia

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Fecha de emisión del documento referencia | 
**document_type** | **str** | Tipo de documento | 
**number** | **float** | Número del documento referencia | 
**prefix** | **str** | Prefijo del documento referencia | 
**uuid** | **str** | CUFE del documento referencia | 

## Example

```python
from openapi_client.models.associated_document import AssociatedDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AssociatedDocument from a JSON string
associated_document_instance = AssociatedDocument.from_json(json)
# print the JSON string representation of the object
print(AssociatedDocument.to_json())

# convert the object into a dict
associated_document_dict = associated_document_instance.to_dict()
# create an instance of AssociatedDocument from a dict
associated_document_from_dict = AssociatedDocument.from_dict(associated_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


