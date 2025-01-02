# GetReceptionEmails200Response

Objeto con la información del correro electrónico registrado

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identification** | **str** | NIT de la empresa | [optional] 
**email** | **str** | Correo electónico registrado en la DIAN | [optional] 
**registration_date** | **date** | Fecha de registro | [optional] 

## Example

```python
from openapi_client.models.get_reception_emails200_response import GetReceptionEmails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetReceptionEmails200Response from a JSON string
get_reception_emails200_response_instance = GetReceptionEmails200Response.from_json(json)
# print the JSON string representation of the object
print(GetReceptionEmails200Response.to_json())

# convert the object into a dict
get_reception_emails200_response_dict = get_reception_emails200_response_instance.to_dict()
# create an instance of GetReceptionEmails200Response from a dict
get_reception_emails200_response_from_dict = GetReceptionEmails200Response.from_dict(get_reception_emails200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


