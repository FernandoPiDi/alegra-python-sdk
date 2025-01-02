# CreateEquivalentDocumentPosRequestCustomerContact

Objeto que contiene la información de contacto del adquiriente del documento electrónico. <br><i>Campo oficial DIAN &lt;Contact&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre del contacto del adquiriente. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Name&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_equivalent_document_pos_request_customer_contact import CreateEquivalentDocumentPosRequestCustomerContact

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEquivalentDocumentPosRequestCustomerContact from a JSON string
create_equivalent_document_pos_request_customer_contact_instance = CreateEquivalentDocumentPosRequestCustomerContact.from_json(json)
# print the JSON string representation of the object
print(CreateEquivalentDocumentPosRequestCustomerContact.to_json())

# convert the object into a dict
create_equivalent_document_pos_request_customer_contact_dict = create_equivalent_document_pos_request_customer_contact_instance.to_dict()
# create an instance of CreateEquivalentDocumentPosRequestCustomerContact from a dict
create_equivalent_document_pos_request_customer_contact_from_dict = CreateEquivalentDocumentPosRequestCustomerContact.from_dict(create_equivalent_document_pos_request_customer_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


