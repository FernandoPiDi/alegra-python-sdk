# CreateAdjustmentNoteEquivalentDocumentRequestDocumentReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id registrado por la API E-providers, en caso de que el documento de referencia haya sido emitido a través de E-providers solo se necesita este dato para identificar el documento | [optional] 
**full_number** | **str** | Número del Documento Equivalente al que se hace referencia. (Prefijo + Número). Se indica en caso de que sea un documento equivalente emitido con otro proveedor y/o el id no se especifique | [optional] 
**cude** | **str** | Cude del Documento Equivalente relacionado. Se indica en caso de que sea un documento equivalente emitido con otro proveedor y/o el id no se especifique | [optional] 
**issue_date** | **str** | Fecha del documento referenciado. | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_equivalent_document_request_document_reference import CreateAdjustmentNoteEquivalentDocumentRequestDocumentReference

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDocumentReference from a JSON string
create_adjustment_note_equivalent_document_request_document_reference_instance = CreateAdjustmentNoteEquivalentDocumentRequestDocumentReference.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteEquivalentDocumentRequestDocumentReference.to_json())

# convert the object into a dict
create_adjustment_note_equivalent_document_request_document_reference_dict = create_adjustment_note_equivalent_document_request_document_reference_instance.to_dict()
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDocumentReference from a dict
create_adjustment_note_equivalent_document_request_document_reference_from_dict = CreateAdjustmentNoteEquivalentDocumentRequestDocumentReference.from_dict(create_adjustment_note_equivalent_document_request_document_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


