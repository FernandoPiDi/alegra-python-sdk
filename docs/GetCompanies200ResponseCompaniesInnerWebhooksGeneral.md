# GetCompanies200ResponseCompaniesInnerWebhooksGeneral

Objeto con información de webhooks generales

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**government_status_changed** | [**GetCompanies200ResponseCompaniesInnerWebhooksGeneralGovernmentStatusChanged**](GetCompanies200ResponseCompaniesInnerWebhooksGeneralGovernmentStatusChanged.md) |  | 

## Example

```python
from openapi_client.models.get_companies200_response_companies_inner_webhooks_general import GetCompanies200ResponseCompaniesInnerWebhooksGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooksGeneral from a JSON string
get_companies200_response_companies_inner_webhooks_general_instance = GetCompanies200ResponseCompaniesInnerWebhooksGeneral.from_json(json)
# print the JSON string representation of the object
print(GetCompanies200ResponseCompaniesInnerWebhooksGeneral.to_json())

# convert the object into a dict
get_companies200_response_companies_inner_webhooks_general_dict = get_companies200_response_companies_inner_webhooks_general_instance.to_dict()
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooksGeneral from a dict
get_companies200_response_companies_inner_webhooks_general_from_dict = GetCompanies200ResponseCompaniesInnerWebhooksGeneral.from_dict(get_companies200_response_companies_inner_webhooks_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


