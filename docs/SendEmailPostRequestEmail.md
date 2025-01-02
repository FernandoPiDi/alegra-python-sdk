# SendEmailPostRequestEmail

Objeto opcional, si no es enviado se buscará el dato del email en el documento electrónico. Sin embargo, para notificar un evento electrónico, sí es requerido, ya que de este documento no se puede obtener el valor email

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | Dirección de correo electrónico a la cual llega el correo | 
**reply_to** | **str** | Dirección de correo electrónico para que el receptor tenga la opción de comunicarse | 

## Example

```python
from openapi_client.models.send_email_post_request_email import SendEmailPostRequestEmail

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailPostRequestEmail from a JSON string
send_email_post_request_email_instance = SendEmailPostRequestEmail.from_json(json)
# print the JSON string representation of the object
print(SendEmailPostRequestEmail.to_json())

# convert the object into a dict
send_email_post_request_email_dict = send_email_post_request_email_instance.to_dict()
# create an instance of SendEmailPostRequestEmail from a dict
send_email_post_request_email_from_dict = SendEmailPostRequestEmail.from_dict(send_email_post_request_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


