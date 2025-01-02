# CreateCompanyRequestAllOfWebhooksPayrolls

Objeto con webhooks de nóminas electrónicas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emission_finished** | [**GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished**](GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_company_request_all_of_webhooks_payrolls import CreateCompanyRequestAllOfWebhooksPayrolls

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequestAllOfWebhooksPayrolls from a JSON string
create_company_request_all_of_webhooks_payrolls_instance = CreateCompanyRequestAllOfWebhooksPayrolls.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequestAllOfWebhooksPayrolls.to_json())

# convert the object into a dict
create_company_request_all_of_webhooks_payrolls_dict = create_company_request_all_of_webhooks_payrolls_instance.to_dict()
# create an instance of CreateCompanyRequestAllOfWebhooksPayrolls from a dict
create_company_request_all_of_webhooks_payrolls_from_dict = CreateCompanyRequestAllOfWebhooksPayrolls.from_dict(create_company_request_all_of_webhooks_payrolls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


