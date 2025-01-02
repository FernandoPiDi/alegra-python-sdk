# GetCompanies200ResponseCompaniesInnerAddress

Objeto que contiene la información relacionada a la dirección. <br><i>Grupo de información oficial DIAN &lt;RegistrationAddress | PhysicalLocation&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Dirección del lugar fisico. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Line&amp;gt;&lt;/i&gt; | [optional] 
**city** | **str** | Código de la Ciudad. Se debe colocar el Código que corresponda de la tabla de municipios disponibles de la DIAN. Se debe informar cuando el código del País es &#39;CO&#39;. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | [optional] 
**department** | **str** | Código del Departamento. Se debe colocar el Código que corresponda de la tabla de departamentos disponibles de la DIAN. Se debe informar cuando el código del País es &#39;CO&#39;. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;CountrySubentityCode&amp;gt;&lt;/i&gt; | [optional] 
**country** | **str** | Código identificador del País. Se debe colocar el código que corresponda de la tabla de países disponibles de la DIAN. Por defecto &#39;CO&#39;. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;IdentificationCode&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.get_companies200_response_companies_inner_address import GetCompanies200ResponseCompaniesInnerAddress

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanies200ResponseCompaniesInnerAddress from a JSON string
get_companies200_response_companies_inner_address_instance = GetCompanies200ResponseCompaniesInnerAddress.from_json(json)
# print the JSON string representation of the object
print(GetCompanies200ResponseCompaniesInnerAddress.to_json())

# convert the object into a dict
get_companies200_response_companies_inner_address_dict = get_companies200_response_companies_inner_address_instance.to_dict()
# create an instance of GetCompanies200ResponseCompaniesInnerAddress from a dict
get_companies200_response_companies_inner_address_from_dict = GetCompanies200ResponseCompaniesInnerAddress.from_dict(get_companies200_response_companies_inner_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


