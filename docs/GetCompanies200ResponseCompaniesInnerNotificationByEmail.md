# GetCompanies200ResponseCompaniesInnerNotificationByEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indica si se quiere enviar un email de notificación automáticamente después de que la empresa genere un documento electrónico valido. Valido para Factura Electrónica, Nota Débito y Nota Crédito. Por defecto es false | 
**message** | **str** | Mensaje (opcional) que será añadido al final de la plantilla del correo | [optional] 

## Example

```python
from openapi_client.models.get_companies200_response_companies_inner_notification_by_email import GetCompanies200ResponseCompaniesInnerNotificationByEmail

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanies200ResponseCompaniesInnerNotificationByEmail from a JSON string
get_companies200_response_companies_inner_notification_by_email_instance = GetCompanies200ResponseCompaniesInnerNotificationByEmail.from_json(json)
# print the JSON string representation of the object
print(GetCompanies200ResponseCompaniesInnerNotificationByEmail.to_json())

# convert the object into a dict
get_companies200_response_companies_inner_notification_by_email_dict = get_companies200_response_companies_inner_notification_by_email_instance.to_dict()
# create an instance of GetCompanies200ResponseCompaniesInnerNotificationByEmail from a dict
get_companies200_response_companies_inner_notification_by_email_from_dict = GetCompanies200ResponseCompaniesInnerNotificationByEmail.from_dict(get_companies200_response_companies_inner_notification_by_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


