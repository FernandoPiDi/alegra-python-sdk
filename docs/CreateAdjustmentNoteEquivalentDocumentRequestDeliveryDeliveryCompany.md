# CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompany

Información de la compañía encargada de la entrega

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre de la empresa de envíos | [optional] 
**address** | [**CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyAddress**](CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyAddress.md) |  | [optional] 
**tax_scheme** | [**CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxScheme**](CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxScheme.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_equivalent_document_request_delivery_delivery_company import CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompany

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompany from a JSON string
create_adjustment_note_equivalent_document_request_delivery_delivery_company_instance = CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompany.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompany.to_json())

# convert the object into a dict
create_adjustment_note_equivalent_document_request_delivery_delivery_company_dict = create_adjustment_note_equivalent_document_request_delivery_delivery_company_instance.to_dict()
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompany from a dict
create_adjustment_note_equivalent_document_request_delivery_delivery_company_from_dict = CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompany.from_dict(create_adjustment_note_equivalent_document_request_delivery_delivery_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


