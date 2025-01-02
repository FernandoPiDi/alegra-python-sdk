# SendEmailPost200ResponseDataCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | NIT de la empresa emisora | [optional] 
**name** | **str** | Nombre o Razon social de la empresa | [optional] 
**email** | **str** | Email donde se puede responder la notificación | [optional] 
**phone** | **str** | Número telefónico que aparecerá en los datos de contacto | [optional] 
**trade_name** | **str** | Nombre comercial que va en el asunto del correo | [optional] 

## Example

```python
from openapi_client.models.send_email_post200_response_data_company import SendEmailPost200ResponseDataCompany

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailPost200ResponseDataCompany from a JSON string
send_email_post200_response_data_company_instance = SendEmailPost200ResponseDataCompany.from_json(json)
# print the JSON string representation of the object
print(SendEmailPost200ResponseDataCompany.to_json())

# convert the object into a dict
send_email_post200_response_data_company_dict = send_email_post200_response_data_company_instance.to_dict()
# create an instance of SendEmailPost200ResponseDataCompany from a dict
send_email_post200_response_data_company_from_dict = SendEmailPost200ResponseDataCompany.from_dict(send_email_post200_response_data_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


