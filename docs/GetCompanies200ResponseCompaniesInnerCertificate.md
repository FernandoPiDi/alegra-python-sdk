# GetCompanies200ResponseCompaniesInnerCertificate

Objeto que contiene la información del certificado, obligatorio únicamente si el atributo useAlegraCertificate es false

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre del archivo | 
**extension** | **str** | Extensión del archivo | 
**content** | **bytearray** | Archivo de certificado en base 64 | 
**password** | **str** | Contraseña del certificado | 

## Example

```python
from openapi_client.models.get_companies200_response_companies_inner_certificate import GetCompanies200ResponseCompaniesInnerCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanies200ResponseCompaniesInnerCertificate from a JSON string
get_companies200_response_companies_inner_certificate_instance = GetCompanies200ResponseCompaniesInnerCertificate.from_json(json)
# print the JSON string representation of the object
print(GetCompanies200ResponseCompaniesInnerCertificate.to_json())

# convert the object into a dict
get_companies200_response_companies_inner_certificate_dict = get_companies200_response_companies_inner_certificate_instance.to_dict()
# create an instance of GetCompanies200ResponseCompaniesInnerCertificate from a dict
get_companies200_response_companies_inner_certificate_from_dict = GetCompanies200ResponseCompaniesInnerCertificate.from_dict(get_companies200_response_companies_inner_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


