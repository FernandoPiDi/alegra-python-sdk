# CreateCompanyRequestAllOfNotificationByEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indica si se quiere enviar un email de notificación automáticamente después de que la empresa genere un documento electrónico valido. Valido para Factura Electrónica, Nota Débito y Nota Crédito | 
**message** | **str** | Mensaje (opcional) que será añadido al final de la plantilla del correo | [optional] 

## Example

```python
from openapi_client.models.create_company_request_all_of_notification_by_email import CreateCompanyRequestAllOfNotificationByEmail

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequestAllOfNotificationByEmail from a JSON string
create_company_request_all_of_notification_by_email_instance = CreateCompanyRequestAllOfNotificationByEmail.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequestAllOfNotificationByEmail.to_json())

# convert the object into a dict
create_company_request_all_of_notification_by_email_dict = create_company_request_all_of_notification_by_email_instance.to_dict()
# create an instance of CreateCompanyRequestAllOfNotificationByEmail from a dict
create_company_request_all_of_notification_by_email_from_dict = CreateCompanyRequestAllOfNotificationByEmail.from_dict(create_company_request_all_of_notification_by_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


