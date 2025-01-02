# CreateAdjustmentNoteSupportDocumentRequestCompanyTaxCode

Objeto que contiene el grupo de detalles tributarios del Emisor. <br><i>Campo oficial DIAN &lt;TaxScheme&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identificador del tributo. Se debe colocar el Código que corresponda de la tabla de tipos de tributos de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 

## Example

```python
from openapi_client.models.create_adjustment_note_support_document_request_company_tax_code import CreateAdjustmentNoteSupportDocumentRequestCompanyTaxCode

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteSupportDocumentRequestCompanyTaxCode from a JSON string
create_adjustment_note_support_document_request_company_tax_code_instance = CreateAdjustmentNoteSupportDocumentRequestCompanyTaxCode.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteSupportDocumentRequestCompanyTaxCode.to_json())

# convert the object into a dict
create_adjustment_note_support_document_request_company_tax_code_dict = create_adjustment_note_support_document_request_company_tax_code_instance.to_dict()
# create an instance of CreateAdjustmentNoteSupportDocumentRequestCompanyTaxCode from a dict
create_adjustment_note_support_document_request_company_tax_code_from_dict = CreateAdjustmentNoteSupportDocumentRequestCompanyTaxCode.from_dict(create_adjustment_note_support_document_request_company_tax_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


