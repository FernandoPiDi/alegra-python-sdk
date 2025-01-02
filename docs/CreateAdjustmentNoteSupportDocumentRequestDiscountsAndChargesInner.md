# CreateAdjustmentNoteSupportDocumentRequestDiscountsAndChargesInner

Información de un cargo o descuento

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_charge** | **bool** | Cargo es true, aumenta el valor del DSE; Descuento es false, disminuye el valor del NADSE. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ChargeIndicator&amp;gt;&lt;/i&gt; | 
**reason** | **str** | Texto libre para informar la razón del cargo o descuento aplicado al documento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;AllowanceChargeReason&amp;gt;&lt;/i&gt; | [optional] 
**percentage_amount** | **float** | Porcentaje a aplicar. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;MultiplierFactorNumeric&amp;gt;&lt;/i&gt; | 
**amount** | **float** | Valor total del cargo o descuento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Amount&amp;gt;&lt;/i&gt; | 
**base_amount** | **float** | Valor Base para calcular el descuento o el cargo. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;BaseAmount&amp;gt;&lt;/i&gt; | 

## Example

```python
from openapi_client.models.create_adjustment_note_support_document_request_discounts_and_charges_inner import CreateAdjustmentNoteSupportDocumentRequestDiscountsAndChargesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteSupportDocumentRequestDiscountsAndChargesInner from a JSON string
create_adjustment_note_support_document_request_discounts_and_charges_inner_instance = CreateAdjustmentNoteSupportDocumentRequestDiscountsAndChargesInner.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteSupportDocumentRequestDiscountsAndChargesInner.to_json())

# convert the object into a dict
create_adjustment_note_support_document_request_discounts_and_charges_inner_dict = create_adjustment_note_support_document_request_discounts_and_charges_inner_instance.to_dict()
# create an instance of CreateAdjustmentNoteSupportDocumentRequestDiscountsAndChargesInner from a dict
create_adjustment_note_support_document_request_discounts_and_charges_inner_from_dict = CreateAdjustmentNoteSupportDocumentRequestDiscountsAndChargesInner.from_dict(create_adjustment_note_support_document_request_discounts_and_charges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


