# GetCompanies200ResponseCompaniesInnerWebhooks

Objeto que contiene la información de los webhooks configurados para la empresa

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**GetCompanies200ResponseCompaniesInnerWebhooksGeneral**](GetCompanies200ResponseCompaniesInnerWebhooksGeneral.md) |  | [optional] 
**payrolls** | [**GetCompanies200ResponseCompaniesInnerWebhooksPayrolls**](GetCompanies200ResponseCompaniesInnerWebhooksPayrolls.md) |  | [optional] 
**invoices** | [**GetCompanies200ResponseCompaniesInnerWebhooksInvoices**](GetCompanies200ResponseCompaniesInnerWebhooksInvoices.md) |  | [optional] 
**credit_notes** | [**GetCompanies200ResponseCompaniesInnerWebhooksCreditNotes**](GetCompanies200ResponseCompaniesInnerWebhooksCreditNotes.md) |  | [optional] 
**debit_notes** | [**GetCompanies200ResponseCompaniesInnerWebhooksDebitNotes**](GetCompanies200ResponseCompaniesInnerWebhooksDebitNotes.md) |  | [optional] 
**equivalent_documents** | [**GetCompanies200ResponseCompaniesInnerWebhooksEquivalentDocuments**](GetCompanies200ResponseCompaniesInnerWebhooksEquivalentDocuments.md) |  | [optional] 
**support_documents** | [**GetCompanies200ResponseCompaniesInnerWebhooksSupportDocuments**](GetCompanies200ResponseCompaniesInnerWebhooksSupportDocuments.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_companies200_response_companies_inner_webhooks import GetCompanies200ResponseCompaniesInnerWebhooks

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooks from a JSON string
get_companies200_response_companies_inner_webhooks_instance = GetCompanies200ResponseCompaniesInnerWebhooks.from_json(json)
# print the JSON string representation of the object
print(GetCompanies200ResponseCompaniesInnerWebhooks.to_json())

# convert the object into a dict
get_companies200_response_companies_inner_webhooks_dict = get_companies200_response_companies_inner_webhooks_instance.to_dict()
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooks from a dict
get_companies200_response_companies_inner_webhooks_from_dict = GetCompanies200ResponseCompaniesInnerWebhooks.from_dict(get_companies200_response_companies_inner_webhooks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


