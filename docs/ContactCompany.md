# ContactCompany

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
from openapi_client.models.contact_company import ContactCompany

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCompany from a JSON string
contact_company_instance = ContactCompany.from_json(json)
# print the JSON string representation of the object
print(ContactCompany.to_json())

# convert the object into a dict
contact_company_dict = contact_company_instance.to_dict()
# create an instance of ContactCompany from a dict
contact_company_from_dict = ContactCompany.from_dict(contact_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


