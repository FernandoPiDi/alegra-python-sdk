# CreateCompanyRequestAllOfCertificate

Objeto que contiene la información del certificado, obligatorio únicamente si el atributo useAlegraCertificate es false

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre del archivo | 
**extension** | **str** | Extensión del archivo | 
**content** | **bytearray** | Contenido del archivo en base64 | 
**password** | **str** | Contraseña del archivo | 

## Example

```python
from openapi_client.models.create_company_request_all_of_certificate import CreateCompanyRequestAllOfCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequestAllOfCertificate from a JSON string
create_company_request_all_of_certificate_instance = CreateCompanyRequestAllOfCertificate.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequestAllOfCertificate.to_json())

# convert the object into a dict
create_company_request_all_of_certificate_dict = create_company_request_all_of_certificate_instance.to_dict()
# create an instance of CreateCompanyRequestAllOfCertificate from a dict
create_company_request_all_of_certificate_from_dict = CreateCompanyRequestAllOfCertificate.from_dict(create_company_request_all_of_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


