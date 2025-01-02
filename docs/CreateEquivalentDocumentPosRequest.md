# CreateEquivalentDocumentPosRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | **str** | Indica que se emitirá un documento equivalente POS electrónico reemplazando un documento físico generado en contingencia, este elemento acepta la siguiente opción: &#x60;07&#x60; Contingencia por parte del emisor.&lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;InvoiceTypeCode&amp;gt;&lt;/i&gt; | [optional] 
**number** | **str** | Número del documento equivalente. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**resolution** | [**CreateEquivalentDocumentPosRequestResolution**](CreateEquivalentDocumentPosRequestResolution.md) |  | 
**company** | [**CreateEquivalentDocumentPosRequestCompany**](CreateEquivalentDocumentPosRequestCompany.md) |  | 
**customer** | [**CreateEquivalentDocumentPosRequestCustomer**](CreateEquivalentDocumentPosRequestCustomer.md) |  | [optional] 
**items** | [**List[CreateEquivalentDocumentPosRequestItemsInner]**](CreateEquivalentDocumentPosRequestItemsInner.md) | Array que contiene el listado de artículos y/o servicios | 
**payments** | [**List[CreateEquivalentDocumentPosRequestPaymentsInner]**](CreateEquivalentDocumentPosRequestPaymentsInner.md) | Array con el listado de pagos. Grupo de campos para información relacionadas con el pago de la factura. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;PaymentMeans&amp;gt;&lt;/i&gt; | [optional] 
**discounts_and_charges** | [**List[CreateEquivalentDocumentPosRequestDiscountsAndChargesInner]**](CreateEquivalentDocumentPosRequestDiscountsAndChargesInner.md) | Array con el listado de Descuentos o Cargos a nivel de factura. Grupo de campos para información relacionada con los descuentos o cargos que no afectan las bases gravables. Los descuentos o cargos que afectan bases gravables se deben informar a nivel de ítem. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;AllowanceCharge&amp;gt;&lt;/i&gt; | [optional] 
**exchange_rate** | [**CreateEquivalentDocumentPosRequestExchangeRate**](CreateEquivalentDocumentPosRequestExchangeRate.md) |  | [optional] 
**total_amounts** | [**CreateEquivalentDocumentPosRequestTotalAmounts**](CreateEquivalentDocumentPosRequestTotalAmounts.md) |  | 
**buyer_benefits** | [**CreateEquivalentDocumentPosRequestBuyerBenefits**](CreateEquivalentDocumentPosRequestBuyerBenefits.md) |  | [optional] 
**cash_register** | [**CreateEquivalentDocumentPosRequestCashRegister**](CreateEquivalentDocumentPosRequestCashRegister.md) |  | [optional] 
**note** | **str** | Nota relativa al documento equivalente | [optional] 
**additional_document_reference** | [**CreateEquivalentDocumentPosRequestAdditionalDocumentReference**](CreateEquivalentDocumentPosRequestAdditionalDocumentReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_equivalent_document_pos_request import CreateEquivalentDocumentPosRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEquivalentDocumentPosRequest from a JSON string
create_equivalent_document_pos_request_instance = CreateEquivalentDocumentPosRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEquivalentDocumentPosRequest.to_json())

# convert the object into a dict
create_equivalent_document_pos_request_dict = create_equivalent_document_pos_request_instance.to_dict()
# create an instance of CreateEquivalentDocumentPosRequest from a dict
create_equivalent_document_pos_request_from_dict = CreateEquivalentDocumentPosRequest.from_dict(create_equivalent_document_pos_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


