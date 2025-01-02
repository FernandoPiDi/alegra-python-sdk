# CreateCompanyRequestAllOfWebhooksGeneral

Objeto con webhooks generales

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**government_status_changed** | [**CreateCompanyRequestAllOfWebhooksGeneralGovernmentStatusChanged**](CreateCompanyRequestAllOfWebhooksGeneralGovernmentStatusChanged.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_company_request_all_of_webhooks_general import CreateCompanyRequestAllOfWebhooksGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequestAllOfWebhooksGeneral from a JSON string
create_company_request_all_of_webhooks_general_instance = CreateCompanyRequestAllOfWebhooksGeneral.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequestAllOfWebhooksGeneral.to_json())

# convert the object into a dict
create_company_request_all_of_webhooks_general_dict = create_company_request_all_of_webhooks_general_instance.to_dict()
# create an instance of CreateCompanyRequestAllOfWebhooksGeneral from a dict
create_company_request_all_of_webhooks_general_from_dict = CreateCompanyRequestAllOfWebhooksGeneral.from_dict(create_company_request_all_of_webhooks_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


