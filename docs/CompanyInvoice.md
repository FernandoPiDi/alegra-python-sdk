# CompanyInvoice

Objeto que contiene la información del obligado a facturar o emisor del documento electrónico. <br><i>Grupo de información oficial DIAN &lt;AccountingSupplierParty&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id de la empresa. Id único generado por la API | 
**organization_type** | **float** | Identificador de tipo de organización jurídica de la persona o empresa. Se debe colocar el Código que corresponda de la tabla de tipos de organización jurídica de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;AdditionalAccountID&amp;gt;&lt;/i&gt; | [optional] 
**identification_number** | **str** | Número de identificación o NIT del emisor, sin guiones ni DV. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;CompanyID&amp;gt;&lt;/i&gt; | [optional] 
**dv** | **str** | DV del NIT del emisor. Es obligatorio si identificationType &#x3D; 31. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;@schemeID&amp;gt;&lt;/i&gt; | [optional] 
**name** | **str** | Nombre (Razón Social) del Emisor. Si no se envía, se tomará el Nombre/Razón Social de la compañía. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;RegistrationName&amp;gt;&lt;/i&gt; | [optional] 
**trade_name** | **str** | Nombre Comercial del Emisor. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Name&amp;gt;&lt;/i&gt; | [optional] 
**regime_code** | **str** | Régimen o tipo de obligación o responsabilidad del emisor. Se debe colocar el Código que corresponda de la tabla de tipos de régimen/responsabilidades fiscales de la DIAN. Para reportar varias obligaciones / responsabilidades, se deben reportar separando cada uno de los valores de la lista con &#39;;&#39;. Ejemplo O‐13;O‐15; &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;TaxLevelCode&amp;gt;&lt;/i&gt; | [optional] 
**tax_code** | [**CreateEquivalentDocumentPosRequestCompanyTaxCode**](CreateEquivalentDocumentPosRequestCompanyTaxCode.md) |  | [optional] 
**economic_activities** | **List[str]** | Lista de actividades económicas de la empresa. Debe informar el código según lista CIIU | [optional] 
**email** | **str** | Correo electrónico. Se debe colocar el correo de recepción para documentos e instrumentos electrónicos. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ElectronicMail&amp;gt;&lt;/i&gt; | [optional] 
**phone** | **str** | Número de teléfono, celular u otro. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Telephone&amp;gt;&lt;/i&gt; | [optional] 
**address** | [**GetCompanies200ResponseCompaniesInnerAddress**](GetCompanies200ResponseCompaniesInnerAddress.md) |  | [optional] 
**contact** | [**CreateEquivalentDocumentPosRequestCompanyContact**](CreateEquivalentDocumentPosRequestCompanyContact.md) |  | [optional] 

## Example

```python
from openapi_client.models.company_invoice import CompanyInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInvoice from a JSON string
company_invoice_instance = CompanyInvoice.from_json(json)
# print the JSON string representation of the object
print(CompanyInvoice.to_json())

# convert the object into a dict
company_invoice_dict = company_invoice_instance.to_dict()
# create an instance of CompanyInvoice from a dict
company_invoice_from_dict = CompanyInvoice.from_dict(company_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


