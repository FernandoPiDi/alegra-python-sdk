# CreateAdjustmentNoteEquivalentDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | Prefijo de la nota de ajuste | [optional] 
**number** | **float** | Número de la nota de ajuste del documento equivalente electrónico | 
**note** | **str** | Información adicional: Texto libre, relativo al documento | [optional] 
**document_reference** | [**CreateAdjustmentNoteEquivalentDocumentRequestDocumentReference**](CreateAdjustmentNoteEquivalentDocumentRequestDocumentReference.md) |  | 
**discrepancy** | [**CreateAdjustmentNoteEquivalentDocumentRequestDiscrepancy**](CreateAdjustmentNoteEquivalentDocumentRequestDiscrepancy.md) |  | 
**company** | [**CreateEquivalentDocumentPosRequestCompany**](CreateEquivalentDocumentPosRequestCompany.md) |  | 
**customer** | [**CreateAdjustmentNoteEquivalentDocumentRequestCustomer**](CreateAdjustmentNoteEquivalentDocumentRequestCustomer.md) |  | [optional] 
**items** | [**List[CreateAdjustmentNoteEquivalentDocumentRequestItemsInner]**](CreateAdjustmentNoteEquivalentDocumentRequestItemsInner.md) | Array que contiene el listado de artículos y/o servicios | 
**total_amounts** | [**CreateEquivalentDocumentPosRequestTotalAmounts**](CreateEquivalentDocumentPosRequestTotalAmounts.md) |  | 
**payments** | [**List[CreateEquivalentDocumentPosRequestPaymentsInner]**](CreateEquivalentDocumentPosRequestPaymentsInner.md) | Array con el listado de pagos. Grupo de campos para información relacionadas con el pago de la factura. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;PaymentMeans&amp;gt;&lt;/i&gt; | 
**discounts_and_charges** | [**List[CreateEquivalentDocumentPosRequestDiscountsAndChargesInner]**](CreateEquivalentDocumentPosRequestDiscountsAndChargesInner.md) | Array con el listado de Descuentos o Cargos a nivel de factura. Grupo de campos para información relacionada con los descuentos o cargos que no afectan las bases gravables. Los descuentos o cargos que afectan bases gravables se deben informar a nivel de ítem. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;AllowanceCharge&amp;gt;&lt;/i&gt; | [optional] 
**delivery** | [**CreateAdjustmentNoteEquivalentDocumentRequestDelivery**](CreateAdjustmentNoteEquivalentDocumentRequestDelivery.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_equivalent_document_request import CreateAdjustmentNoteEquivalentDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequest from a JSON string
create_adjustment_note_equivalent_document_request_instance = CreateAdjustmentNoteEquivalentDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteEquivalentDocumentRequest.to_json())

# convert the object into a dict
create_adjustment_note_equivalent_document_request_dict = create_adjustment_note_equivalent_document_request_instance.to_dict()
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequest from a dict
create_adjustment_note_equivalent_document_request_from_dict = CreateAdjustmentNoteEquivalentDocumentRequest.from_dict(create_adjustment_note_equivalent_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


