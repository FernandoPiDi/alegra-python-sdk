# CreateCreditNoteRequestAssociatedDocumentsInner

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
from openapi_client.models.create_credit_note_request_associated_documents_inner import CreateCreditNoteRequestAssociatedDocumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCreditNoteRequestAssociatedDocumentsInner from a JSON string
create_credit_note_request_associated_documents_inner_instance = CreateCreditNoteRequestAssociatedDocumentsInner.from_json(json)
# print the JSON string representation of the object
print(CreateCreditNoteRequestAssociatedDocumentsInner.to_json())

# convert the object into a dict
create_credit_note_request_associated_documents_inner_dict = create_credit_note_request_associated_documents_inner_instance.to_dict()
# create an instance of CreateCreditNoteRequestAssociatedDocumentsInner from a dict
create_credit_note_request_associated_documents_inner_from_dict = CreateCreditNoteRequestAssociatedDocumentsInner.from_dict(create_credit_note_request_associated_documents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


