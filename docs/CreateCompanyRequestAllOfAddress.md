# CreateCompanyRequestAllOfAddress

Objeto que contiene la información relacionada a la dirección. <br><i>Grupo de información oficial DIAN &lt;RegistrationAddress | PhysicalLocation&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Dirección del lugar fisico de la empresa | 
**city** | **str** | Nombre de la Ciudad. Se debe colocar el Código que corresponda de la tabla de municipios disponibles de la DIAN | 
**department** | **str** | Nombre del Departamento. Se debe colocar el Código que corresponda de la tabla de departamentos disponibles de la DIAN | 
**country** | **str** | Nombre del Pais. Se debe colocar el Código que corresponda de la tabla de paises disponibles de la DIAN. Por defecto &#39;CO&#39; | [optional] 

## Example

```python
from openapi_client.models.create_company_request_all_of_address import CreateCompanyRequestAllOfAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequestAllOfAddress from a JSON string
create_company_request_all_of_address_instance = CreateCompanyRequestAllOfAddress.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequestAllOfAddress.to_json())

# convert the object into a dict
create_company_request_all_of_address_dict = create_company_request_all_of_address_instance.to_dict()
# create an instance of CreateCompanyRequestAllOfAddress from a dict
create_company_request_all_of_address_from_dict = CreateCompanyRequestAllOfAddress.from_dict(create_company_request_all_of_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


