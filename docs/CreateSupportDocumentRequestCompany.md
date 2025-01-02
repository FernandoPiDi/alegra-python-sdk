# CreateSupportDocumentRequestCompany

Objeto que contiene la información del obligado a facturar o emisor del documento electrónico. <br><i>Grupo de información oficial DIAN &lt;AccountingSupplierParty&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id de la empresa. Id único generado por la API | 
**organization_type** | **float** | Identificador de tipo de organización jurídica de la persona o empresa. Se debe colocar el Código que corresponda de la tabla de tipos de organización jurídica de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;AdditionalAccountID&amp;gt;&lt;/i&gt; | [optional] 
**identification_number** | **str** | Número de identificación o NIT del emisor, sin guiones ni DV. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;CompanyID&amp;gt;&lt;/i&gt; | [optional] 
**dv** | **str** | DV del NIT del emisor. Es obligatorio si identificationType &#x3D; 31. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;@schemeID&amp;gt;&lt;/i&gt; | [optional] 
**name** | **str** | Nombre (Razón Social) del Emisor. Si no se envía, se tomará el Nombre/Razón Social de la compañía. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;RegistrationName&amp;gt;&lt;/i&gt; | [optional] 
**regime_code** | **str** | Régimen o tipo de obligación o responsabilidad del emisor. Se debe colocar el Código que corresponda de la tabla de tipos de régimen/responsabilidades fiscales de la DIAN. Para reportar varias obligaciones / responsabilidades, se deben reportar separando cada uno de los valores de la lista con &#39;;&#39;. Ejemplo O‐13;O‐15; &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;TaxLevelCode&amp;gt;&lt;/i&gt; | [optional] 
**tax_code** | [**CreateSupportDocumentRequestCompanyTaxCode**](CreateSupportDocumentRequestCompanyTaxCode.md) |  | 

## Example

```python
from openapi_client.models.create_support_document_request_company import CreateSupportDocumentRequestCompany

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupportDocumentRequestCompany from a JSON string
create_support_document_request_company_instance = CreateSupportDocumentRequestCompany.from_json(json)
# print the JSON string representation of the object
print(CreateSupportDocumentRequestCompany.to_json())

# convert the object into a dict
create_support_document_request_company_dict = create_support_document_request_company_instance.to_dict()
# create an instance of CreateSupportDocumentRequestCompany from a dict
create_support_document_request_company_from_dict = CreateSupportDocumentRequestCompany.from_dict(create_support_document_request_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


