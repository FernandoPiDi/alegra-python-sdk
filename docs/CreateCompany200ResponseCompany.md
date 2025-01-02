# CreateCompany200ResponseCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id de la empresa | [optional] 
**name** | **str** | Nombre/Razón Social de la empresa | 
**trade_name** | **str** | Nombre Comercial de la empresa | [optional] 
**identification** | **str** | Identificación de la empresa | 
**dv** | **str** | Dígito verificador de la identificación de la empresa | 
**use_alegra_certificate** | **bool** | True si deseas usar el certificado de Alegra | 
**government_status** | [**GetCompanies200ResponseCompaniesInnerGovernmentStatus**](GetCompanies200ResponseCompaniesInnerGovernmentStatus.md) |  | [optional] 
**certificate** | [**GetCompanies200ResponseCompaniesInnerCertificate**](GetCompanies200ResponseCompaniesInnerCertificate.md) |  | [optional] 
**notification_by_email** | [**GetCompanies200ResponseCompaniesInnerNotificationByEmail**](GetCompanies200ResponseCompaniesInnerNotificationByEmail.md) |  | [optional] 
**webhooks** | [**GetCompanies200ResponseCompaniesInnerWebhooks**](GetCompanies200ResponseCompaniesInnerWebhooks.md) |  | [optional] 
**organization_type** | **float** | Identificador de tipo de organización jurídica de la persona o empresa. Se debe colocar el Código que corresponda de la tabla de tipos de organización jurídica de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;AdditionalAccountID&amp;gt;&lt;/i&gt; | [optional] 
**identification_type** | **str** | Tipo de documento de identificación de la empresa. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN | [optional] 
**regime_code** | **str** | Régimen al que pertenece la empresa. Se debe colocar el Código que corresponda de la tabla de tipos de régimen/responsabilidades fiscales de la DIAN. Para reportar varias obligaciones / responsabilidades, se deben reportar separando cada uno de los valores de la lista con &#39;;&#39;. Ejemplo O‐13;O‐15; | [optional] 
**tax_code** | [**GetCompanies200ResponseCompaniesInnerTaxCode**](GetCompanies200ResponseCompaniesInnerTaxCode.md) |  | [optional] 
**email** | **str** | Correo electrónico de la empresa. Se debe colocar el correo de recepción para documentos e instrumentos electrónicos | [optional] 
**phone** | **str** | Número de teléfono, celular u otro | [optional] 
**address** | [**GetCompanies200ResponseCompaniesInnerAddress**](GetCompanies200ResponseCompaniesInnerAddress.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_company200_response_company import CreateCompany200ResponseCompany

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompany200ResponseCompany from a JSON string
create_company200_response_company_instance = CreateCompany200ResponseCompany.from_json(json)
# print the JSON string representation of the object
print(CreateCompany200ResponseCompany.to_json())

# convert the object into a dict
create_company200_response_company_dict = create_company200_response_company_instance.to_dict()
# create an instance of CreateCompany200ResponseCompany from a dict
create_company200_response_company_from_dict = CreateCompany200ResponseCompany.from_dict(create_company200_response_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


