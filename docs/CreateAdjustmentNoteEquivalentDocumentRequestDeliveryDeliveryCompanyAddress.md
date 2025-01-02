# CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyAddress

Dirección de la empresa de envíos

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | Se debe colocar el Código que corresponda de la tabla de municipios disponibles de la DIAN | [optional] 
**postal** | **str** | Código postal del lugar de entrega | [optional] 
**department** | **str** | Se debe colocar el Código que corresponda de la tabla de departamentos disponibles de la DIAN | [optional] 
**address** | **str** | Dirección del lugar fisico, sin ciudad ni departamento | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_equivalent_document_request_delivery_delivery_company_address import CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyAddress from a JSON string
create_adjustment_note_equivalent_document_request_delivery_delivery_company_address_instance = CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyAddress.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyAddress.to_json())

# convert the object into a dict
create_adjustment_note_equivalent_document_request_delivery_delivery_company_address_dict = create_adjustment_note_equivalent_document_request_delivery_delivery_company_address_instance.to_dict()
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyAddress from a dict
create_adjustment_note_equivalent_document_request_delivery_delivery_company_address_from_dict = CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyAddress.from_dict(create_adjustment_note_equivalent_document_request_delivery_delivery_company_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


