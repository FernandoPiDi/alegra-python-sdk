# GetCompanies200ResponseCompaniesInnerTaxCode

Objeto que contiene el grupo de detalles tributarios del Emisor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identificador del tributo. | 
**name** | **str** | Nombre del tributo o nombre de la figura tributaria. Se debe enviar en caso de que el identificador del tributo sea &#39;ZZ&#39; | [optional] 

## Example

```python
from openapi_client.models.get_companies200_response_companies_inner_tax_code import GetCompanies200ResponseCompaniesInnerTaxCode

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanies200ResponseCompaniesInnerTaxCode from a JSON string
get_companies200_response_companies_inner_tax_code_instance = GetCompanies200ResponseCompaniesInnerTaxCode.from_json(json)
# print the JSON string representation of the object
print(GetCompanies200ResponseCompaniesInnerTaxCode.to_json())

# convert the object into a dict
get_companies200_response_companies_inner_tax_code_dict = get_companies200_response_companies_inner_tax_code_instance.to_dict()
# create an instance of GetCompanies200ResponseCompaniesInnerTaxCode from a dict
get_companies200_response_companies_inner_tax_code_from_dict = GetCompanies200ResponseCompaniesInnerTaxCode.from_dict(get_companies200_response_companies_inner_tax_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


