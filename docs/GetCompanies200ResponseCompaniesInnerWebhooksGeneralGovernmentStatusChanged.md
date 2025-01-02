# GetCompanies200ResponseCompaniesInnerWebhooksGeneralGovernmentStatusChanged

Objeto con la información para el webhook que se dispara cuando cambia el estado de la compañía ante la DIAN

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Url a la cual notificará el webhook | 
**headers** | **object** | Objeto con headers personalizados que serán enviados en el request al webhook configurado | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_companies200_response_companies_inner_webhooks_general_government_status_changed import GetCompanies200ResponseCompaniesInnerWebhooksGeneralGovernmentStatusChanged

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooksGeneralGovernmentStatusChanged from a JSON string
get_companies200_response_companies_inner_webhooks_general_government_status_changed_instance = GetCompanies200ResponseCompaniesInnerWebhooksGeneralGovernmentStatusChanged.from_json(json)
# print the JSON string representation of the object
print(GetCompanies200ResponseCompaniesInnerWebhooksGeneralGovernmentStatusChanged.to_json())

# convert the object into a dict
get_companies200_response_companies_inner_webhooks_general_government_status_changed_dict = get_companies200_response_companies_inner_webhooks_general_government_status_changed_instance.to_dict()
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooksGeneralGovernmentStatusChanged from a dict
get_companies200_response_companies_inner_webhooks_general_government_status_changed_from_dict = GetCompanies200ResponseCompaniesInnerWebhooksGeneralGovernmentStatusChanged.from_dict(get_companies200_response_companies_inner_webhooks_general_government_status_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


