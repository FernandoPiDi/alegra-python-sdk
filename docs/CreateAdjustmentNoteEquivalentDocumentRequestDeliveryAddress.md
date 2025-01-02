# CreateAdjustmentNoteEquivalentDocumentRequestDeliveryAddress

Dirección donde se entrega el producto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | Se debe colocar el Código que corresponda de la tabla de municipios disponibles de la DIAN | [optional] 
**postal** | **str** | Código postal del lugar de entrega | [optional] 
**department** | **str** | Se debe colocar el Código que corresponda de la tabla de departamentos disponibles de la DIAN | [optional] 
**address** | **str** | Dirección del lugar fisico, sin ciudad ni departamento | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_equivalent_document_request_delivery_address import CreateAdjustmentNoteEquivalentDocumentRequestDeliveryAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDeliveryAddress from a JSON string
create_adjustment_note_equivalent_document_request_delivery_address_instance = CreateAdjustmentNoteEquivalentDocumentRequestDeliveryAddress.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteEquivalentDocumentRequestDeliveryAddress.to_json())

# convert the object into a dict
create_adjustment_note_equivalent_document_request_delivery_address_dict = create_adjustment_note_equivalent_document_request_delivery_address_instance.to_dict()
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDeliveryAddress from a dict
create_adjustment_note_equivalent_document_request_delivery_address_from_dict = CreateAdjustmentNoteEquivalentDocumentRequestDeliveryAddress.from_dict(create_adjustment_note_equivalent_document_request_delivery_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


