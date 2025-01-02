# CreateInvoiceRequestCompany

Objeto que contiene la información del obligado a facturar o emisor del documento electrónico. <br><i>Grupo de información oficial DIAN &lt;AccountingSupplierParty&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id de la empresa. Id único generado por la API | 
**organization_type** | **float** | Identificador de tipo de organización jurídica de la de persona, puede ser una de las siguientes opciones: &#x60;1&#x60; Persona Jurídica y asimiladas; &#x60;2&#x60; Persona Natural y asimiladas. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;AdditionalAccountID&amp;gt;&lt;/i&gt; | [optional] 
**identification_number** | **str** | Número de identificación o NIT del emisor, sin guiones ni DV. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;CompanyID&amp;gt;&lt;/i&gt; | [optional] 
**dv** | **str** | DV del NIT del emisor. Es obligatorio si identificationType &#x3D; 31. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;@schemeID&amp;gt;&lt;/i&gt; | [optional] 
**name** | **str** | Nombre (Razón Social) del Emisor. Si no se envía, se tomará el Nombre/Razón Social de la compañía. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;RegistrationName&amp;gt;&lt;/i&gt; | [optional] 
**trade_name** | **str** | Nombre Comercial del Emisor. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Name&amp;gt;&lt;/i&gt; | [optional] 
**regime_code** | **str** | Obligaciones o responsabilidades tributarias del emisor. El elemento acepta las siguientes opciones: &#x60;O-13&#x60; Gran contribuyente; &#x60;O-15&#x60; Autorretenedor; &#x60;O-23&#x60; Agente de retención IVA; &#x60;O-47&#x60; Régimen simple de tributación; &#x60;R-99-PN&#x60; No aplica – Otros. Para reportar varias obligaciones / responsabilidades se deben separar los valores con &#39;;&#39;. Ejemplo O‐13;O‐15; &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;TaxLevelCode&amp;gt;&lt;/i&gt; | [optional] 
**tax_code** | [**CreateInvoiceRequestCompanyTaxCode**](CreateInvoiceRequestCompanyTaxCode.md) |  | [optional] 
**economic_activities** | **List[str]** | Lista de actividades económicas de la empresa. Debe informar el código según lista CIIU | [optional] 
**email** | **str** | Correo electrónico. Se debe colocar el correo de recepción para documentos e instrumentos electrónicos. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ElectronicMail&amp;gt;&lt;/i&gt; | [optional] 
**phone** | **str** | Número de teléfono, celular u otro. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Telephone&amp;gt;&lt;/i&gt; | [optional] 
**address** | **object** | Objeto que contiene la información con respeto a la dirección del lugar físico donde se expidió el documento. Si no se envía el objeto &#39;taxAddress&#39;, la información de este objeto se usará también para &#39;taxAddress&#39; por defecto. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;PhysicalLocation&amp;gt;&lt;/i&gt; | [optional] 
**tax_address** | **object** | Objeto que contiene la información con respeto a la dirección fiscal del emisor. Si no se envía este objeto se replicará la información que se envía en &#39;address&#39;. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;RegistrationAddress&amp;gt;&lt;/i&gt; | [optional] 
**shareholders** | [**List[CreateInvoiceRequestCompanyShareholdersInner]**](CreateInvoiceRequestCompanyShareholdersInner.md) | Grupo de elementos que permiten registrar la información de los participantes de un **Consorcio o Unión temporal**. Se debe completar un grupo de elementos por cada participante del consorcio. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;ShareholderParty&amp;gt;&lt;/i&gt; | [optional] 
**contact** | [**CreateEquivalentDocumentPosRequestCompanyContact**](CreateEquivalentDocumentPosRequestCompanyContact.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_invoice_request_company import CreateInvoiceRequestCompany

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestCompany from a JSON string
create_invoice_request_company_instance = CreateInvoiceRequestCompany.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestCompany.to_json())

# convert the object into a dict
create_invoice_request_company_dict = create_invoice_request_company_instance.to_dict()
# create an instance of CreateInvoiceRequestCompany from a dict
create_invoice_request_company_from_dict = CreateInvoiceRequestCompany.from_dict(create_invoice_request_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


