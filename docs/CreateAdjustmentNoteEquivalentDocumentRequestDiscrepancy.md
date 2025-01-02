# CreateAdjustmentNoteEquivalentDocumentRequestDiscrepancy

Objeto que contiene el Grupo para explicaciones sobre la naturaleza de la Nota de ajuste al DE

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_id** | **str** | Identifica la sección del Documento Equivalente original a la cual se aplica la corrección | [optional] 
**response_code** | **float** | Código de descripción de la corrección para notas de ajuste. (1) Devolución parcial de los bienes y/o no aceptación parcial del servicio. (2) Anulación del documento soporte en adquisiciones efectuadas a sujetos no obligados a expedir factura de venta o documento equivalente. (3) Rebaja o descuento parcial o total. (4) Ajuste de precio. (5) Otros. | 
**description** | **str** | Descripción de la naturaleza de la corrección | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_equivalent_document_request_discrepancy import CreateAdjustmentNoteEquivalentDocumentRequestDiscrepancy

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDiscrepancy from a JSON string
create_adjustment_note_equivalent_document_request_discrepancy_instance = CreateAdjustmentNoteEquivalentDocumentRequestDiscrepancy.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteEquivalentDocumentRequestDiscrepancy.to_json())

# convert the object into a dict
create_adjustment_note_equivalent_document_request_discrepancy_dict = create_adjustment_note_equivalent_document_request_discrepancy_instance.to_dict()
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDiscrepancy from a dict
create_adjustment_note_equivalent_document_request_discrepancy_from_dict = CreateAdjustmentNoteEquivalentDocumentRequestDiscrepancy.from_dict(create_adjustment_note_equivalent_document_request_discrepancy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


