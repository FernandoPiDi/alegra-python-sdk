# CreateEquivalentDocumentPosRequestCompanyTaxCode

Objeto que contiene el grupo de detalles tributarios del Emisor. <br><i>Campo oficial DIAN &lt;TaxScheme&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identificador del tributo. Se debe colocar el Código que corresponda de la tabla de tipos de tributos de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**name** | **str** | Nombre del tributo o nombre de la figura tributaria. Se debe enviar en caso de que el identificador del tributo sea &#39;ZZ&#39;. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Name&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_equivalent_document_pos_request_company_tax_code import CreateEquivalentDocumentPosRequestCompanyTaxCode

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEquivalentDocumentPosRequestCompanyTaxCode from a JSON string
create_equivalent_document_pos_request_company_tax_code_instance = CreateEquivalentDocumentPosRequestCompanyTaxCode.from_json(json)
# print the JSON string representation of the object
print(CreateEquivalentDocumentPosRequestCompanyTaxCode.to_json())

# convert the object into a dict
create_equivalent_document_pos_request_company_tax_code_dict = create_equivalent_document_pos_request_company_tax_code_instance.to_dict()
# create an instance of CreateEquivalentDocumentPosRequestCompanyTaxCode from a dict
create_equivalent_document_pos_request_company_tax_code_from_dict = CreateEquivalentDocumentPosRequestCompanyTaxCode.from_dict(create_equivalent_document_pos_request_company_tax_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


