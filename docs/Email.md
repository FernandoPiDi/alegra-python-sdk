# Email

Objeto para enviar un email de recepción de documento

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | Lista de destinatarios separados por coma | [optional] 
**cc** | **str** | Lista de CC (carbon copy) separados por coma | [optional] 
**bcc** | **str** | Lista de BCC (blind carbon copy) separados por coma | [optional] 
**reply_to** | **str** | Dirección de correo a la que se responde el email. | [optional] 

## Example

```python
from openapi_client.models.email import Email

# TODO update the JSON string below
json = "{}"
# create an instance of Email from a JSON string
email_instance = Email.from_json(json)
# print the JSON string representation of the object
print(Email.to_json())

# convert the object into a dict
email_dict = email_instance.to_dict()
# create an instance of Email from a dict
email_from_dict = Email.from_dict(email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


