# UpdateCompanyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre/Razón Social de la empresa | [optional] 
**trade_name** | **str** | Nombre Comercial de la empresa | [optional] 
**identification** | **str** | Identificación de la empresa | [optional] 
**dv** | **str** | Dígito verificador de la identificación de la empresa | [optional] 
**type** | **str** | Tipo de empresa | [optional] 
**use_alegra_certificate** | **bool** | Indica si se desea usar el certificado de Alegra o no | [optional] 
**certificate** | [**CreateCompanyRequestAllOfCertificate**](CreateCompanyRequestAllOfCertificate.md) |  | [optional] 
**notification_by_email** | [**CreateCompanyRequestAllOfNotificationByEmail**](CreateCompanyRequestAllOfNotificationByEmail.md) |  | [optional] 
**webhooks** | [**CreateCompanyRequestAllOfWebhooks**](CreateCompanyRequestAllOfWebhooks.md) |  | [optional] 
**organization_type** | **float** | Tipo de organización jurídica de la empresa. Se debe colocar el Código que corresponda de la tabla de tipo de organización jurídica de la DIAN | [optional] 
**identification_type** | **str** | Tipo de documento de identificación de la empresa. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN | [optional] 
**regime_code** | **str** | Régimen al que pertenece la empresa. Se debe colocar el Código que corresponda de la tabla de tipos de responsabilidad fiscal de la DIAN. Para reportar varias obligaciones / responsabilidades, se deben reportar separando cada uno de los valores de la lista con &#39;;&#39;. Ejemplo O‐13;O‐15; | [optional] 
**tax_code** | [**GetCompanies200ResponseCompaniesInnerTaxCode**](GetCompanies200ResponseCompaniesInnerTaxCode.md) |  | [optional] 
**economic_activities** | **List[str]** | Lista de actividades económicas de la empresa. Debe informar el código según lista CIIU | [optional] 
**email** | **str** | Correo electrónico de la empresa registrado en la DIAN para la recepción de documentos | [optional] 
**phone** | **str** | Número de teléfono, celular u otro | [optional] 
**address** | [**CreateCompanyRequestAllOfAddress**](CreateCompanyRequestAllOfAddress.md) |  | [optional] 
**logo** | **str** | Imagen del logo en base64 a incluir en todos los documentos PDF ## Consideraciones - El tamaño máximo de la imagen es de 150 KB (aproximadamente 150,000 caracteres en base64). - La validación final del tamaño se realizará en el servidor después de decodificar la imagen. - Si un documento es creado con un logo, este siempre mostrará ese logo. Si el logo es actualizado posteriormente, los documentos creados anteriormente no serán actualizados para mostrar el nuevo logo. Por lo tanto, se recomienda crear documentos con un logo solo después de haber cargado y establecido el logo final. | [optional] 
**other_responsabilities** | **str** | Texto que permite incluir información adicional sobre las responsabilidades fiscales o de otro tipo que la empresa desee reflejar en los documentos emitidos. Esta información se incluirá tanto en el XML como en el PDF de los documentos generados | [optional] 

## Example

```python
from openapi_client.models.update_company_request import UpdateCompanyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCompanyRequest from a JSON string
update_company_request_instance = UpdateCompanyRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCompanyRequest.to_json())

# convert the object into a dict
update_company_request_dict = update_company_request_instance.to_dict()
# create an instance of UpdateCompanyRequest from a dict
update_company_request_from_dict = UpdateCompanyRequest.from_dict(update_company_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


