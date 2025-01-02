# CreateDebitNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | Prefijo de la nota débito electrónica | [optional] 
**number** | **float** | Número de la nota débito electrónica | 
**concept_code** | **str** | Concepto por el cual se genera la nota débito. Se debe colocar el Código que corresponda de la tabla de tipos de concepto de corrección para Notas débito disponibles de la DIAN | 
**note** | **str** | Nota o información adicional: Texto libre, relativo al documento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Note&amp;gt;&lt;/i&gt; | [optional] 
**associated_documents** | [**List[CreateCreditNoteRequestAssociatedDocumentsInner]**](CreateCreditNoteRequestAssociatedDocumentsInner.md) | Array que contiene la información de las facturas electrónicas afectadas por la Nota. Todas las facturas afectadas deben ser de un mismo adquiriente | 
**company** | [**CreateInvoiceRequestCompany**](CreateInvoiceRequestCompany.md) |  | 
**customer** | [**CreateInvoiceRequestCustomer**](CreateInvoiceRequestCustomer.md) |  | 
**items** | [**List[CreateCreditNoteRequestItemsInner]**](CreateCreditNoteRequestItemsInner.md) | Array que contiene el listado de artículos y/o servicios | 
**discounts_and_charges** | [**List[CreateInvoiceRequestDiscountsAndChargesInner]**](CreateInvoiceRequestDiscountsAndChargesInner.md) | Array con el listado de Descuentos o Cargos a nivel de factura. Grupo de campos para información relacionada con los descuentos o cargos que no afectan las bases gravables. Los descuentos o cargos que afectan bases gravables se deben informar a nivel de ítem. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;AllowanceCharge&amp;gt;&lt;/i&gt; | [optional] 
**total_amounts** | [**CreateEquivalentDocumentPosRequestTotalAmounts**](CreateEquivalentDocumentPosRequestTotalAmounts.md) |  | 
**payments** | [**List[CreateEquivalentDocumentPosRequestPaymentsInner]**](CreateEquivalentDocumentPosRequestPaymentsInner.md) | Array con el listado de pagos. Grupo de campos para información relacionadas con el pago de la factura. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;PaymentMeans&amp;gt;&lt;/i&gt; | 
**advance_payments** | [**List[CreateInvoiceRequestAdvancePaymentsInner]**](CreateInvoiceRequestAdvancePaymentsInner.md) | Array con el listado de anticipos. Grupo de campos para información relacionadas con un anticipo. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;PrePaidPayment&amp;gt;&lt;/i&gt; | [optional] 
**invoice_period** | [**CreateInvoiceRequestInvoicePeriod**](CreateInvoiceRequestInvoicePeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_debit_note_request import CreateDebitNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDebitNoteRequest from a JSON string
create_debit_note_request_instance = CreateDebitNoteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDebitNoteRequest.to_json())

# convert the object into a dict
create_debit_note_request_dict = create_debit_note_request_instance.to_dict()
# create an instance of CreateDebitNoteRequest from a dict
create_debit_note_request_from_dict = CreateDebitNoteRequest.from_dict(create_debit_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


