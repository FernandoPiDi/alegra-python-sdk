# CreateCompanyRequestAllOfWebhooks

Objeto que contiene la información de los webhooks configurados para la empresa. En caso de querer actualizar un webhook, se debe enviar el objeto completo con los webhooks que se desean mantener y los que se desean eliminar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**CreateCompanyRequestAllOfWebhooksGeneral**](CreateCompanyRequestAllOfWebhooksGeneral.md) |  | [optional] 
**payrolls** | [**CreateCompanyRequestAllOfWebhooksPayrolls**](CreateCompanyRequestAllOfWebhooksPayrolls.md) |  | [optional] 
**invoices** | [**CreateCompanyRequestAllOfWebhooksInvoices**](CreateCompanyRequestAllOfWebhooksInvoices.md) |  | [optional] 
**credit_notes** | [**CreateCompanyRequestAllOfWebhooksCreditNotes**](CreateCompanyRequestAllOfWebhooksCreditNotes.md) |  | [optional] 
**debit_notes** | [**CreateCompanyRequestAllOfWebhooksDebitNotes**](CreateCompanyRequestAllOfWebhooksDebitNotes.md) |  | [optional] 
**equivalent_documents** | [**GetCompanies200ResponseCompaniesInnerWebhooksEquivalentDocuments**](GetCompanies200ResponseCompaniesInnerWebhooksEquivalentDocuments.md) |  | [optional] 
**support_documents** | [**GetCompanies200ResponseCompaniesInnerWebhooksSupportDocuments**](GetCompanies200ResponseCompaniesInnerWebhooksSupportDocuments.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_company_request_all_of_webhooks import CreateCompanyRequestAllOfWebhooks

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequestAllOfWebhooks from a JSON string
create_company_request_all_of_webhooks_instance = CreateCompanyRequestAllOfWebhooks.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequestAllOfWebhooks.to_json())

# convert the object into a dict
create_company_request_all_of_webhooks_dict = create_company_request_all_of_webhooks_instance.to_dict()
# create an instance of CreateCompanyRequestAllOfWebhooks from a dict
create_company_request_all_of_webhooks_from_dict = CreateCompanyRequestAllOfWebhooks.from_dict(create_company_request_all_of_webhooks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


