# GetCompanies200ResponseCompaniesInnerWebhooksPayrolls

Objeto con información de webhooks para nóminas electrónicas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emission_finished** | [**GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished**](GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished.md) |  | 

## Example

```python
from openapi_client.models.get_companies200_response_companies_inner_webhooks_payrolls import GetCompanies200ResponseCompaniesInnerWebhooksPayrolls

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooksPayrolls from a JSON string
get_companies200_response_companies_inner_webhooks_payrolls_instance = GetCompanies200ResponseCompaniesInnerWebhooksPayrolls.from_json(json)
# print the JSON string representation of the object
print(GetCompanies200ResponseCompaniesInnerWebhooksPayrolls.to_json())

# convert the object into a dict
get_companies200_response_companies_inner_webhooks_payrolls_dict = get_companies200_response_companies_inner_webhooks_payrolls_instance.to_dict()
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooksPayrolls from a dict
get_companies200_response_companies_inner_webhooks_payrolls_from_dict = GetCompanies200ResponseCompaniesInnerWebhooksPayrolls.from_dict(get_companies200_response_companies_inner_webhooks_payrolls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


