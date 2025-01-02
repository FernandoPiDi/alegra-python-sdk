# CreateInvoiceRequestCustomerTaxCode

Objeto que contiene el grupo de detalles tributarios del adquiriente. <br><i>Campo oficial DIAN &lt;TaxScheme&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identificador del tributo. Se debe colocar el Código que corresponda de la tabla de tipos de tributos de la DIAN. En caso de que no se envíe el tipo de tributo, se especificará por defecto el valor 01 (IVA) si el tipo de identifación es &#39;31&#39;, de lo contrario se especificará el valor &#39;ZZ&#39; &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 

## Example

```python
from openapi_client.models.create_invoice_request_customer_tax_code import CreateInvoiceRequestCustomerTaxCode

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestCustomerTaxCode from a JSON string
create_invoice_request_customer_tax_code_instance = CreateInvoiceRequestCustomerTaxCode.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestCustomerTaxCode.to_json())

# convert the object into a dict
create_invoice_request_customer_tax_code_dict = create_invoice_request_customer_tax_code_instance.to_dict()
# create an instance of CreateInvoiceRequestCustomerTaxCode from a dict
create_invoice_request_customer_tax_code_from_dict = CreateInvoiceRequestCustomerTaxCode.from_dict(create_invoice_request_customer_tax_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


