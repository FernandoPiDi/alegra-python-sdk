# CreateInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | **str** | Tipo de Documento / Factura. 01: Estándar, 02: Exportación, 03: Mandato, 04: Contingencia Facturador Electrónico, 05: Transporte, 06: AIU, 07: Factura electrónica de Compra de divisa, 08: Factura electrónica de Venta de divisa | 
**number** | **float** | Número de la factura electrónica. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**note** | **str** | Nota o información adicional: Texto libre, relativo al documento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Note&amp;gt;&lt;/i&gt; | [optional] 
**resolution** | [**CreateInvoiceRequestResolution**](CreateInvoiceRequestResolution.md) |  | 
**company** | [**CreateInvoiceRequestCompany**](CreateInvoiceRequestCompany.md) |  | 
**customer** | [**CreateInvoiceRequestCustomer**](CreateInvoiceRequestCustomer.md) |  | 
**items** | [**List[CreateInvoiceRequestItemsInner]**](CreateInvoiceRequestItemsInner.md) | Array que contiene el listado de artículos y/o servicios | 
**payments** | [**List[CreateEquivalentDocumentPosRequestPaymentsInner]**](CreateEquivalentDocumentPosRequestPaymentsInner.md) | Array con el listado de pagos. Grupo de campos para información relacionadas con el pago de la factura. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;PaymentMeans&amp;gt;&lt;/i&gt; | [optional] 
**advance_payments** | [**List[CreateInvoiceRequestAdvancePaymentsInner]**](CreateInvoiceRequestAdvancePaymentsInner.md) | Array con el listado de anticipos. Grupo de campos para información relacionadas con un anticipo. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;PrePaidPayment&amp;gt;&lt;/i&gt; | [optional] 
**discounts_and_charges** | [**List[CreateInvoiceRequestDiscountsAndChargesInner]**](CreateInvoiceRequestDiscountsAndChargesInner.md) | Array con el listado de Descuentos o Cargos a nivel de factura. Grupo de campos para información relacionada con los descuentos o cargos que no afectan las bases gravables. Los descuentos o cargos que afectan bases gravables se deben informar a nivel de ítem. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;AllowanceCharge&amp;gt;&lt;/i&gt; | [optional] 
**exchange_rate** | [**CreateEquivalentDocumentPosRequestExchangeRate**](CreateEquivalentDocumentPosRequestExchangeRate.md) |  | [optional] 
**total_amounts** | [**CreateEquivalentDocumentPosRequestTotalAmounts**](CreateEquivalentDocumentPosRequestTotalAmounts.md) |  | 
**health_sector_general** | [**CreateInvoiceRequestHealthSectorGeneral**](CreateInvoiceRequestHealthSectorGeneral.md) |  | [optional] 
**invoice_period** | [**CreateInvoiceRequestInvoicePeriod**](CreateInvoiceRequestInvoicePeriod.md) |  | [optional] 
**additional_document_reference** | [**CreateInvoiceRequestAdditionalDocumentReference**](CreateInvoiceRequestAdditionalDocumentReference.md) |  | [optional] 
**order_reference** | [**CreateInvoiceRequestOrderReference**](CreateInvoiceRequestOrderReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_invoice_request import CreateInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequest from a JSON string
create_invoice_request_instance = CreateInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequest.to_json())

# convert the object into a dict
create_invoice_request_dict = create_invoice_request_instance.to_dict()
# create an instance of CreateInvoiceRequest from a dict
create_invoice_request_from_dict = CreateInvoiceRequest.from_dict(create_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


