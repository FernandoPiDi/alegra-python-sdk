# CreateInvoiceRequestDiscountsAndChargesInner

Información de un cargo o descuento

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_charge** | **bool** | True si se desea informar un cargo o false si se desea informar un descuento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ChargeIndicator&amp;gt;&lt;/i&gt; | 
**reason** | **str** | Razón (texto): Texto libre para informar la razón del cargo o descuento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;AllowanceChargeReason&amp;gt;&lt;/i&gt; | 
**reason_code** | **str** | Código para categorizar el descuento o el recargo a nivel de documento, este elemento acepta una de las siguientes opciones: &#x60;00&#x60; Descuento no condicionado; &#x60;01&#x60; Descuento condicionado; &#x60;02&#x60; Recargo no condicionado; &#x60;03&#x60; Recargo condicionado. Es obligatorio enviar el código cuando se desee aplicar un descuento. Para descuentos solo se pueden enviar &#x60;00&#x60; y &#x60;01&#x60; por default es &#x60;01&#x60;, para recargos solo se puede enviar &#x60;02&#x60; y &#x60;03&#x60;.&lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;AllowanceChargeReasonCode&amp;gt;&lt;/i&gt; | [optional] 
**percentage_amount** | **float** | Porcentaje a aplicar. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;MultiplierFactorNumeric&amp;gt;&lt;/i&gt; | 
**amount** | **float** | Valor total del cargo o descuento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Amount&amp;gt;&lt;/i&gt; | 
**base_amount** | **float** | Valor Base para calcular el descuento o el cargo. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;BaseAmount&amp;gt;&lt;/i&gt; | 

## Example

```python
from openapi_client.models.create_invoice_request_discounts_and_charges_inner import CreateInvoiceRequestDiscountsAndChargesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestDiscountsAndChargesInner from a JSON string
create_invoice_request_discounts_and_charges_inner_instance = CreateInvoiceRequestDiscountsAndChargesInner.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestDiscountsAndChargesInner.to_json())

# convert the object into a dict
create_invoice_request_discounts_and_charges_inner_dict = create_invoice_request_discounts_and_charges_inner_instance.to_dict()
# create an instance of CreateInvoiceRequestDiscountsAndChargesInner from a dict
create_invoice_request_discounts_and_charges_inner_from_dict = CreateInvoiceRequestDiscountsAndChargesInner.from_dict(create_invoice_request_discounts_and_charges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


