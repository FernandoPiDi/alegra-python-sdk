# CreateCreditNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | **str** | Tipo de Nota de Crédito. 91: Estándar, 91-22: Estándar sin referencia a Factura, 02: Exportación. Este atributo es opcional, sino se envia este valor, Alegra asociará esta Nota Crédito como una Nota Crédito de Venta Estándar | [optional] 
**prefix** | **str** | Prefijo de la nota crédito electrónica | [optional] 
**number** | **float** | Número de la nota crédito electrónica | 
**concept_code** | **str** | Concepto por el cual se genera la nota crédito. Se debe colocar el Código que corresponda de la tabla de tipos de concepto de corrección para Notas crédito disponibles de la DIAN | 
**note** | **str** | Nota o información adicional: Texto libre, relativo al documento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Note&amp;gt;&lt;/i&gt; | [optional] 
**associated_documents** | [**List[CreateCreditNoteRequestAssociatedDocumentsInner]**](CreateCreditNoteRequestAssociatedDocumentsInner.md) | Array que contiene la información de la factura electrónica afectada por la Nota. Solamente puede reportar 1 factura electrónica y debe ser de un mismo adquiriente. Obligatorio si el tipo de documento es Estandar o Exportación. | [optional] 
**company** | [**CreateInvoiceRequestCompany**](CreateInvoiceRequestCompany.md) |  | 
**customer** | [**CreateInvoiceRequestCustomer**](CreateInvoiceRequestCustomer.md) |  | 
**items** | [**List[CreateCreditNoteRequestItemsInner]**](CreateCreditNoteRequestItemsInner.md) | Array que contiene el listado de artículos y/o servicios | 
**total_amounts** | [**CreateEquivalentDocumentPosRequestTotalAmounts**](CreateEquivalentDocumentPosRequestTotalAmounts.md) |  | 
**payments** | [**List[CreateEquivalentDocumentPosRequestPaymentsInner]**](CreateEquivalentDocumentPosRequestPaymentsInner.md) | Array con el listado de pagos. Grupo de campos para información relacionadas con el pago de la factura. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;PaymentMeans&amp;gt;&lt;/i&gt; | 
**exchange_rate** | [**CreateEquivalentDocumentPosRequestExchangeRate**](CreateEquivalentDocumentPosRequestExchangeRate.md) |  | [optional] 
**discounts_and_charges** | [**List[CreateInvoiceRequestDiscountsAndChargesInner]**](CreateInvoiceRequestDiscountsAndChargesInner.md) | Array con el listado de Descuentos o Cargos a nivel de factura. Grupo de campos para información relacionada con los descuentos o cargos que no afectan las bases gravables. Los descuentos o cargos que afectan bases gravables se deben informar a nivel de ítem. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;AllowanceCharge&amp;gt;&lt;/i&gt; | [optional] 
**invoice_period** | [**CreateInvoiceRequestInvoicePeriod**](CreateInvoiceRequestInvoicePeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_credit_note_request import CreateCreditNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCreditNoteRequest from a JSON string
create_credit_note_request_instance = CreateCreditNoteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCreditNoteRequest.to_json())

# convert the object into a dict
create_credit_note_request_dict = create_credit_note_request_instance.to_dict()
# create an instance of CreateCreditNoteRequest from a dict
create_credit_note_request_from_dict = CreateCreditNoteRequest.from_dict(create_credit_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


