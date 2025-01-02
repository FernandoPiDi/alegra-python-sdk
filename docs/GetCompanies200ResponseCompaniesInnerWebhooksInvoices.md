# GetCompanies200ResponseCompaniesInnerWebhooksInvoices

Objeto con información de webhooks para facturas electrónicas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emission_finished** | [**GetCompanies200ResponseCompaniesInnerWebhooksInvoicesEmissionFinished**](GetCompanies200ResponseCompaniesInnerWebhooksInvoicesEmissionFinished.md) |  | 

## Example

```python
from openapi_client.models.get_companies200_response_companies_inner_webhooks_invoices import GetCompanies200ResponseCompaniesInnerWebhooksInvoices

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooksInvoices from a JSON string
get_companies200_response_companies_inner_webhooks_invoices_instance = GetCompanies200ResponseCompaniesInnerWebhooksInvoices.from_json(json)
# print the JSON string representation of the object
print(GetCompanies200ResponseCompaniesInnerWebhooksInvoices.to_json())

# convert the object into a dict
get_companies200_response_companies_inner_webhooks_invoices_dict = get_companies200_response_companies_inner_webhooks_invoices_instance.to_dict()
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooksInvoices from a dict
get_companies200_response_companies_inner_webhooks_invoices_from_dict = GetCompanies200ResponseCompaniesInnerWebhooksInvoices.from_dict(get_companies200_response_companies_inner_webhooks_invoices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


