# CreateCompanyRequestAllOfWebhooksInvoices

Objeto con webhooks de facturas electrónicas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emission_finished** | [**GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished**](GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_company_request_all_of_webhooks_invoices import CreateCompanyRequestAllOfWebhooksInvoices

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequestAllOfWebhooksInvoices from a JSON string
create_company_request_all_of_webhooks_invoices_instance = CreateCompanyRequestAllOfWebhooksInvoices.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequestAllOfWebhooksInvoices.to_json())

# convert the object into a dict
create_company_request_all_of_webhooks_invoices_dict = create_company_request_all_of_webhooks_invoices_instance.to_dict()
# create an instance of CreateCompanyRequestAllOfWebhooksInvoices from a dict
create_company_request_all_of_webhooks_invoices_from_dict = CreateCompanyRequestAllOfWebhooksInvoices.from_dict(create_company_request_all_of_webhooks_invoices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


