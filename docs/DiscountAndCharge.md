# DiscountAndCharge

Información de un cargo o descuento

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_charge** | **bool** | True si se desea informar un cargo o false si se desea informar un descuento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ChargeIndicator&amp;gt;&lt;/i&gt; | 
**reason** | **str** | Razón (texto): Texto libre para informar la razón del cargo o descuento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;AllowanceChargeReason&amp;gt;&lt;/i&gt; | 
**percentage_amount** | **float** | Porcentaje a aplicar. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;MultiplierFactorNumeric&amp;gt;&lt;/i&gt; | 
**amount** | **float** | Valor total del cargo o descuento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Amount&amp;gt;&lt;/i&gt; | 
**base_amount** | **float** | Valor Base para calcular el descuento o el cargo. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;BaseAmount&amp;gt;&lt;/i&gt; | 

## Example

```python
from openapi_client.models.discount_and_charge import DiscountAndCharge

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountAndCharge from a JSON string
discount_and_charge_instance = DiscountAndCharge.from_json(json)
# print the JSON string representation of the object
print(DiscountAndCharge.to_json())

# convert the object into a dict
discount_and_charge_dict = discount_and_charge_instance.to_dict()
# create an instance of DiscountAndCharge from a dict
discount_and_charge_from_dict = DiscountAndCharge.from_dict(discount_and_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


