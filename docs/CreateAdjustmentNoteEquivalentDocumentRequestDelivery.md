# CreateAdjustmentNoteEquivalentDocumentRequestDelivery

Información acerca del envío y la compañía encargada

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Fecha de la entrega | [optional] 
**time** | **str** | Hora de la entrega | [optional] 
**address** | [**CreateAdjustmentNoteEquivalentDocumentRequestDeliveryAddress**](CreateAdjustmentNoteEquivalentDocumentRequestDeliveryAddress.md) |  | [optional] 
**delivery_company** | [**CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompany**](CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompany.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_equivalent_document_request_delivery import CreateAdjustmentNoteEquivalentDocumentRequestDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDelivery from a JSON string
create_adjustment_note_equivalent_document_request_delivery_instance = CreateAdjustmentNoteEquivalentDocumentRequestDelivery.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteEquivalentDocumentRequestDelivery.to_json())

# convert the object into a dict
create_adjustment_note_equivalent_document_request_delivery_dict = create_adjustment_note_equivalent_document_request_delivery_instance.to_dict()
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDelivery from a dict
create_adjustment_note_equivalent_document_request_delivery_from_dict = CreateAdjustmentNoteEquivalentDocumentRequestDelivery.from_dict(create_adjustment_note_equivalent_document_request_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


