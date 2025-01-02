# CreateEventFromXmlRequestCompany

Objeto para indicar la companía que está emitiendo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id de la compañía emisora. En caso de no existir este parámetro, se utilizará la compañía principal del usuario | [optional] 

## Example

```python
from openapi_client.models.create_event_from_xml_request_company import CreateEventFromXmlRequestCompany

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventFromXmlRequestCompany from a JSON string
create_event_from_xml_request_company_instance = CreateEventFromXmlRequestCompany.from_json(json)
# print the JSON string representation of the object
print(CreateEventFromXmlRequestCompany.to_json())

# convert the object into a dict
create_event_from_xml_request_company_dict = create_event_from_xml_request_company_instance.to_dict()
# create an instance of CreateEventFromXmlRequestCompany from a dict
create_event_from_xml_request_company_from_dict = CreateEventFromXmlRequestCompany.from_dict(create_event_from_xml_request_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


