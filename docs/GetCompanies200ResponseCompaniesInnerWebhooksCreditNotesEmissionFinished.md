# GetCompanies200ResponseCompaniesInnerWebhooksCreditNotesEmissionFinished

Objeto con la información para el webhook que se dispara cuando finaliza el proceso de emisión de una nota crédito electrónica

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Url a la cual notificará el webhook | 
**headers** | **object** | Objeto con headers personalizados que serán enviados en el request al webhook configurado | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_companies200_response_companies_inner_webhooks_credit_notes_emission_finished import GetCompanies200ResponseCompaniesInnerWebhooksCreditNotesEmissionFinished

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooksCreditNotesEmissionFinished from a JSON string
get_companies200_response_companies_inner_webhooks_credit_notes_emission_finished_instance = GetCompanies200ResponseCompaniesInnerWebhooksCreditNotesEmissionFinished.from_json(json)
# print the JSON string representation of the object
print(GetCompanies200ResponseCompaniesInnerWebhooksCreditNotesEmissionFinished.to_json())

# convert the object into a dict
get_companies200_response_companies_inner_webhooks_credit_notes_emission_finished_dict = get_companies200_response_companies_inner_webhooks_credit_notes_emission_finished_instance.to_dict()
# create an instance of GetCompanies200ResponseCompaniesInnerWebhooksCreditNotesEmissionFinished from a dict
get_companies200_response_companies_inner_webhooks_credit_notes_emission_finished_from_dict = GetCompanies200ResponseCompaniesInnerWebhooksCreditNotesEmissionFinished.from_dict(get_companies200_response_companies_inner_webhooks_credit_notes_emission_finished_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


