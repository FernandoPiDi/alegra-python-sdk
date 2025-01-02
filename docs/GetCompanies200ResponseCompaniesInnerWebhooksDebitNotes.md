# GetCompanies200ResponseCompaniesInnerWebhooksDebitNotes

Objeto con información de webhooks para notas débito electrónicas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emission_finished** | [**GetCompanies200ResponseCompaniesInnerWebhooksDebitNotesEmissionFinished**](GetCompanies200ResponseCompaniesInnerWebhooksDebitNotesEmissionFinished.md) |  | 

## Example

```python
from openapi_client.models.get_companies200_response_companies_inner_webhooks_debit_notes import GetCompanies200ResponseCompaniesInnerWebhooksDebitNotes

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooksDebitNotes from a JSON string
get_companies200_response_companies_inner_webhooks_debit_notes_instance = GetCompanies200ResponseCompaniesInnerWebhooksDebitNotes.from_json(json)
# print the JSON string representation of the object
print(GetCompanies200ResponseCompaniesInnerWebhooksDebitNotes.to_json())

# convert the object into a dict
get_companies200_response_companies_inner_webhooks_debit_notes_dict = get_companies200_response_companies_inner_webhooks_debit_notes_instance.to_dict()
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooksDebitNotes from a dict
get_companies200_response_companies_inner_webhooks_debit_notes_from_dict = GetCompanies200ResponseCompaniesInnerWebhooksDebitNotes.from_dict(get_companies200_response_companies_inner_webhooks_debit_notes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


