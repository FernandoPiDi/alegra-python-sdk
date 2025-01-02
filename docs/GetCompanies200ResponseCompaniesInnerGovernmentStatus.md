# GetCompanies200ResponseCompaniesInnerGovernmentStatus

Objeto que contiene la información de los estados de la compañía ante la DIAN para cada uno de los documentos electrónicos

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payrolls** | **str** | Indica el estado de la compañía ante la DIAN para nómina electrónica | [optional] 
**invoices** | **str** | Indica el estado de la compañía ante la DIAN para factura electrónica | [optional] 

## Example

```python
from openapi_client.models.get_companies200_response_companies_inner_government_status import GetCompanies200ResponseCompaniesInnerGovernmentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanies200ResponseCompaniesInnerGovernmentStatus from a JSON string
get_companies200_response_companies_inner_government_status_instance = GetCompanies200ResponseCompaniesInnerGovernmentStatus.from_json(json)
# print the JSON string representation of the object
print(GetCompanies200ResponseCompaniesInnerGovernmentStatus.to_json())

# convert the object into a dict
get_companies200_response_companies_inner_government_status_dict = get_companies200_response_companies_inner_government_status_instance.to_dict()
# create an instance of GetCompanies200ResponseCompaniesInnerGovernmentStatus from a dict
get_companies200_response_companies_inner_government_status_from_dict = GetCompanies200ResponseCompaniesInnerGovernmentStatus.from_dict(get_companies200_response_companies_inner_government_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


