# SendEmailPost200ResponseDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Tipo de documento que se está notificando | [optional] 
**number** | **str** | Número del documento que se está notificando | [optional] 
**code** | **str** | Código del documento electrónico en la DIAN. Se requiere para el asunto del correo | [optional] 
**var_date** | **str** | Fecha en la que fue emitido el documento electrónico | [optional] 
**link** | **str** | Link para consultar el documento en la página de la DIAN | [optional] 
**value** | **str** | Si el documento tiene un valor asociado, se mostrará | [optional] 

## Example

```python
from openapi_client.models.send_email_post200_response_data_document import SendEmailPost200ResponseDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailPost200ResponseDataDocument from a JSON string
send_email_post200_response_data_document_instance = SendEmailPost200ResponseDataDocument.from_json(json)
# print the JSON string representation of the object
print(SendEmailPost200ResponseDataDocument.to_json())

# convert the object into a dict
send_email_post200_response_data_document_dict = send_email_post200_response_data_document_instance.to_dict()
# create an instance of SendEmailPost200ResponseDataDocument from a dict
send_email_post200_response_data_document_from_dict = SendEmailPost200ResponseDataDocument.from_dict(send_email_post200_response_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


