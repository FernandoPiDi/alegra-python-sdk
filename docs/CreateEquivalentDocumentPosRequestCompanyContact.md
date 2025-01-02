# CreateEquivalentDocumentPosRequestCompanyContact

Objeto que contiene la información de contacto del emisor del documento electrónico. <br><i>Campo oficial DIAN &lt;Contact&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre del contacto del emisor. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Name&amp;gt;&lt;/i&gt; | [optional] 
**telefax** | **str** | Número de teléfono, celular u otro del contacto. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Telefax&amp;gt;&lt;/i&gt; | [optional] 
**note** | **str** | Nota adicional del contacto. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Note&amp;gt;&lt;/i&gt; | [optional] 
**commercial_registration_number** | **str** | Número de matrícula mercantil. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;CorporateRegistrationScheme/Name&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_equivalent_document_pos_request_company_contact import CreateEquivalentDocumentPosRequestCompanyContact

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEquivalentDocumentPosRequestCompanyContact from a JSON string
create_equivalent_document_pos_request_company_contact_instance = CreateEquivalentDocumentPosRequestCompanyContact.from_json(json)
# print the JSON string representation of the object
print(CreateEquivalentDocumentPosRequestCompanyContact.to_json())

# convert the object into a dict
create_equivalent_document_pos_request_company_contact_dict = create_equivalent_document_pos_request_company_contact_instance.to_dict()
# create an instance of CreateEquivalentDocumentPosRequestCompanyContact from a dict
create_equivalent_document_pos_request_company_contact_from_dict = CreateEquivalentDocumentPosRequestCompanyContact.from_dict(create_equivalent_document_pos_request_company_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


