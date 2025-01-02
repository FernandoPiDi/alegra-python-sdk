# ContactCustomer

Objeto que contiene la información de contacto del adquiriente del documento electrónico. <br><i>Campo oficial DIAN &lt;Contact&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre del contacto del adquiriente. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Name&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.contact_customer import ContactCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCustomer from a JSON string
contact_customer_instance = ContactCustomer.from_json(json)
# print the JSON string representation of the object
print(ContactCustomer.to_json())

# convert the object into a dict
contact_customer_dict = contact_customer_instance.to_dict()
# create an instance of ContactCustomer from a dict
contact_customer_from_dict = ContactCustomer.from_dict(contact_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


