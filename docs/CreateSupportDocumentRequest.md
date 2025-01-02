# CreateSupportDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_currency** | [**CreateSupportDocumentRequestDocumentCurrency**](CreateSupportDocumentRequestDocumentCurrency.md) |  | [optional] 
**number** | **float** | Número del documento soporte electrónico | 
**resolution** | [**CreateSupportDocumentRequestResolution**](CreateSupportDocumentRequestResolution.md) |  | 
**company** | [**CreateSupportDocumentRequestCompany**](CreateSupportDocumentRequestCompany.md) |  | 
**supplier** | [**CreateSupportDocumentRequestSupplier**](CreateSupportDocumentRequestSupplier.md) |  | 
**items** | [**List[CreateSupportDocumentRequestItemsInner]**](CreateSupportDocumentRequestItemsInner.md) | Array que contiene el listado de articulos y/o servicios | 
**payments** | [**List[CreateSupportDocumentRequestPaymentsInner]**](CreateSupportDocumentRequestPaymentsInner.md) | Array con el listado de pagos. Grupo de campos para información relacionadas con el pago de la factura. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;PaymentMeans&amp;gt;&lt;/i&gt; | 
**discounts_and_charges** | [**List[CreateSupportDocumentRequestDiscountsAndChargesInner]**](CreateSupportDocumentRequestDiscountsAndChargesInner.md) | Descuentos Descuentos o cargos a nivel del DSE, estos descuentos o cargos no afectan las bases gravables. Si se desea agregar un descuento o cargo que afecte la base gravable se debe informan a nivel de items en el elemento &#x60;discountAmount&#x60;. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;AllowanceCharge&amp;gt;&lt;/i&gt; | [optional] 
**total_amounts** | [**CreateSupportDocumentRequestTotalAmounts**](CreateSupportDocumentRequestTotalAmounts.md) |  | 
**notes** | **str** | Información adicional: Texto libre, relativo al documento | [optional] 
**order_reference** | [**CreateSupportDocumentRequestOrderReference**](CreateSupportDocumentRequestOrderReference.md) |  | [optional] 
**billing_reference** | [**CreateSupportDocumentRequestBillingReference**](CreateSupportDocumentRequestBillingReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_support_document_request import CreateSupportDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupportDocumentRequest from a JSON string
create_support_document_request_instance = CreateSupportDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSupportDocumentRequest.to_json())

# convert the object into a dict
create_support_document_request_dict = create_support_document_request_instance.to_dict()
# create an instance of CreateSupportDocumentRequest from a dict
create_support_document_request_from_dict = CreateSupportDocumentRequest.from_dict(create_support_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


