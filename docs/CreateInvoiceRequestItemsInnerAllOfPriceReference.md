# CreateInvoiceRequestItemsInnerAllOfPriceReference

Si se proporciona un precio de referencia, el atributo \"price\" debe ser cero (0.00), ya que se considera una muestra o regalo comercial. <br><i>Campo oficial DIAN &lt;AlternativeConditionPrice&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_amount** | **float** | Valor del artículo o servicio. Este precio se deberá utilizar para calcular el impuesto correspondiente. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PriceAmount&amp;gt;&lt;/i&gt; | 
**price_type_code** | **str** | Deberá contener uno de los siguientes valores posibles de acuerdo al precio informado en el elemento \&quot;priceAmount\&quot;:&lt;br&gt;\&quot;1\&quot;: Valor comercial; \&quot;2\&quot;: Valor en Inventarios; \&quot;3\&quot;: Otro valor&lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PriceTypeCode&amp;gt;&lt;/i&gt; | 

## Example

```python
from openapi_client.models.create_invoice_request_items_inner_all_of_price_reference import CreateInvoiceRequestItemsInnerAllOfPriceReference

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestItemsInnerAllOfPriceReference from a JSON string
create_invoice_request_items_inner_all_of_price_reference_instance = CreateInvoiceRequestItemsInnerAllOfPriceReference.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestItemsInnerAllOfPriceReference.to_json())

# convert the object into a dict
create_invoice_request_items_inner_all_of_price_reference_dict = create_invoice_request_items_inner_all_of_price_reference_instance.to_dict()
# create an instance of CreateInvoiceRequestItemsInnerAllOfPriceReference from a dict
create_invoice_request_items_inner_all_of_price_reference_from_dict = CreateInvoiceRequestItemsInnerAllOfPriceReference.from_dict(create_invoice_request_items_inner_all_of_price_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


