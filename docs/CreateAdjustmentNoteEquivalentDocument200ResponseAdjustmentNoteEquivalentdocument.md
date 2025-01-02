# CreateAdjustmentNoteEquivalentDocument200ResponseAdjustmentNoteEquivalentdocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id de la nota de ajuste al documento equivlanete electrónico | [optional] 
**associated_document_id** | **str** | Identificador único del documento de equivalente afectado por la nota de ajuste | [optional] 
**var_date** | **datetime** | Fecha de emisión de una una nota de ajuste al documento equivalente electrónico | [optional] 
**status** | **str** | Estado de una una nota de ajuste al documento equivalente electrónico | [optional] 
**legal_status** | **str** | Estado legal del documento equivalente electrónico ante la DIAN | [optional] 
**company_identification** | **str** | Identificación de la empresa empleadora | [optional] 
**cude** | **str** | Código único de la una nota de ajuste al documento equivalente electrónico asignado para el documento | [optional] 
**prefix** | **str** | Prefijo de la una nota de ajuste al documento equivalente electrónico | [optional] 
**number** | **float** | Número de la una nota de ajuste al documento equivalente electrónico | [optional] 
**full_number** | **str** | Número de la una nota de ajuste al documento equivalente electrónico (Incluye prefijo y número) | [optional] 
**government_response** | [**GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse**](GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse.md) |  | [optional] 
**xml_file_name** | **str** | Nombre del archivo XML que se envió a la DIAN | [optional] 
**zip_file_name** | **str** | Nombre del archivo Zip que se envió a la DIAN | [optional] 
**errors** | [**List[CreateEquivalentDocumentPos200ResponseEquivalentDocumentErrorsInner]**](CreateEquivalentDocumentPos200ResponseEquivalentDocumentErrorsInner.md) | Array con mensajes de error generados en el sistema | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_equivalent_document200_response_adjustment_note_equivalentdocument import CreateAdjustmentNoteEquivalentDocument200ResponseAdjustmentNoteEquivalentdocument

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteEquivalentDocument200ResponseAdjustmentNoteEquivalentdocument from a JSON string
create_adjustment_note_equivalent_document200_response_adjustment_note_equivalentdocument_instance = CreateAdjustmentNoteEquivalentDocument200ResponseAdjustmentNoteEquivalentdocument.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteEquivalentDocument200ResponseAdjustmentNoteEquivalentdocument.to_json())

# convert the object into a dict
create_adjustment_note_equivalent_document200_response_adjustment_note_equivalentdocument_dict = create_adjustment_note_equivalent_document200_response_adjustment_note_equivalentdocument_instance.to_dict()
# create an instance of CreateAdjustmentNoteEquivalentDocument200ResponseAdjustmentNoteEquivalentdocument from a dict
create_adjustment_note_equivalent_document200_response_adjustment_note_equivalentdocument_from_dict = CreateAdjustmentNoteEquivalentDocument200ResponseAdjustmentNoteEquivalentdocument.from_dict(create_adjustment_note_equivalent_document200_response_adjustment_note_equivalentdocument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


