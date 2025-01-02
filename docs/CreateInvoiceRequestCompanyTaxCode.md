# CreateInvoiceRequestCompanyTaxCode

Objeto que contiene el grupo de detalles tributarios del Emisor. <br><i>Campo oficial DIAN &lt;TaxScheme&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identificador del tributo. Este elemento acepta una de las siguientes opciones: &#x60;01&#x60; IVA; &#x60;04&#x60; INC; &#x60;ZA&#x60; IVA e INC; &#x60;ZZ&#x60; No aplica. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 

## Example

```python
from openapi_client.models.create_invoice_request_company_tax_code import CreateInvoiceRequestCompanyTaxCode

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestCompanyTaxCode from a JSON string
create_invoice_request_company_tax_code_instance = CreateInvoiceRequestCompanyTaxCode.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestCompanyTaxCode.to_json())

# convert the object into a dict
create_invoice_request_company_tax_code_dict = create_invoice_request_company_tax_code_instance.to_dict()
# create an instance of CreateInvoiceRequestCompanyTaxCode from a dict
create_invoice_request_company_tax_code_from_dict = CreateInvoiceRequestCompanyTaxCode.from_dict(create_invoice_request_company_tax_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


