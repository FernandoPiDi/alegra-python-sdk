# CreateCompanyRequestAllOfWebhooksDebitNotes

Objeto con webhooks de notas débito electrónicas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emission_finished** | [**GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished**](GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_company_request_all_of_webhooks_debit_notes import CreateCompanyRequestAllOfWebhooksDebitNotes

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequestAllOfWebhooksDebitNotes from a JSON string
create_company_request_all_of_webhooks_debit_notes_instance = CreateCompanyRequestAllOfWebhooksDebitNotes.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequestAllOfWebhooksDebitNotes.to_json())

# convert the object into a dict
create_company_request_all_of_webhooks_debit_notes_dict = create_company_request_all_of_webhooks_debit_notes_instance.to_dict()
# create an instance of CreateCompanyRequestAllOfWebhooksDebitNotes from a dict
create_company_request_all_of_webhooks_debit_notes_from_dict = CreateCompanyRequestAllOfWebhooksDebitNotes.from_dict(create_company_request_all_of_webhooks_debit_notes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


