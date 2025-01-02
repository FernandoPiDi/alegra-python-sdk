# CreateSupportDocumentRequestCompanyTaxCode

Objeto que contiene el grupo de detalles tributarios del Emisor. <br><i>Campo oficial DIAN &lt;TaxScheme&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identificador del tributo. Se debe colocar el Código que corresponda de la tabla de tipos de tributos de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 

## Example

```python
from openapi_client.models.create_support_document_request_company_tax_code import CreateSupportDocumentRequestCompanyTaxCode

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupportDocumentRequestCompanyTaxCode from a JSON string
create_support_document_request_company_tax_code_instance = CreateSupportDocumentRequestCompanyTaxCode.from_json(json)
# print the JSON string representation of the object
print(CreateSupportDocumentRequestCompanyTaxCode.to_json())

# convert the object into a dict
create_support_document_request_company_tax_code_dict = create_support_document_request_company_tax_code_instance.to_dict()
# create an instance of CreateSupportDocumentRequestCompanyTaxCode from a dict
create_support_document_request_company_tax_code_from_dict = CreateSupportDocumentRequestCompanyTaxCode.from_dict(create_support_document_request_company_tax_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


