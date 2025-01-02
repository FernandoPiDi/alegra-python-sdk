# CreateAdjustmentNoteSupportDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_currency** | [**CreateSupportDocumentRequestDocumentCurrency**](CreateSupportDocumentRequestDocumentCurrency.md) |  | [optional] 
**number** | **float** | Número de la nota de ajuste del Documento Soporte Electrónico. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**prefix** | **str** | Indica el prefijo asignado a las notas de ajuste. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | [optional] 
**note** | **str** | Información adicional: Texto libre, relativo al documento | [optional] 
**invoice_document_reference** | [**CreateAdjustmentNoteSupportDocumentRequestInvoiceDocumentReference**](CreateAdjustmentNoteSupportDocumentRequestInvoiceDocumentReference.md) |  | 
**discrepancies** | [**List[CreateAdjustmentNoteSupportDocumentRequestDiscrepanciesInner]**](CreateAdjustmentNoteSupportDocumentRequestDiscrepanciesInner.md) | Array que contiene el listado de objetos que explican la naturaleza de la Nota de ajuste al documento soporte | 
**company** | [**CreateAdjustmentNoteSupportDocumentRequestCompany**](CreateAdjustmentNoteSupportDocumentRequestCompany.md) |  | 
**supplier** | [**CreateAdjustmentNoteSupportDocumentRequestSupplier**](CreateAdjustmentNoteSupportDocumentRequestSupplier.md) |  | 
**items** | [**List[CreateAdjustmentNoteSupportDocumentRequestItemsInner]**](CreateAdjustmentNoteSupportDocumentRequestItemsInner.md) | Array que contiene el listado de articulos y/o servicios | 
**total_amounts** | [**CreateSupportDocumentRequestTotalAmounts**](CreateSupportDocumentRequestTotalAmounts.md) |  | 
**payments** | [**List[CreateAdjustmentNoteSupportDocumentRequestPaymentsInner]**](CreateAdjustmentNoteSupportDocumentRequestPaymentsInner.md) | Array con el listado de pagos. Grupo de campos para información relacionadas con el pago de la factura. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;PaymentMeans&amp;gt;&lt;/i&gt; | 
**discounts_and_charges** | [**List[CreateAdjustmentNoteSupportDocumentRequestDiscountsAndChargesInner]**](CreateAdjustmentNoteSupportDocumentRequestDiscountsAndChargesInner.md) | Descuentos o cargos a nivel del DSE, estos descuentos o cargos no afectan las bases gravables. Si se desea agregar un descuento o cargo que afecte la base gravable se debe informan a nivel de items en el elemento &#x60;discountAmount&#x60;. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;AllowanceCharge&amp;gt;&lt;/i&gt; | [optional] 
**order_reference** | [**CreateSupportDocumentRequestOrderReference**](CreateSupportDocumentRequestOrderReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_support_document_request import CreateAdjustmentNoteSupportDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteSupportDocumentRequest from a JSON string
create_adjustment_note_support_document_request_instance = CreateAdjustmentNoteSupportDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteSupportDocumentRequest.to_json())

# convert the object into a dict
create_adjustment_note_support_document_request_dict = create_adjustment_note_support_document_request_instance.to_dict()
# create an instance of CreateAdjustmentNoteSupportDocumentRequest from a dict
create_adjustment_note_support_document_request_from_dict = CreateAdjustmentNoteSupportDocumentRequest.from_dict(create_adjustment_note_support_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


