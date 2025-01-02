# SendEmailPost200ResponseDataReceiver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre del receptor del correo de notificación | [optional] 
**email** | **str** | Email al cual se enviará la notificación | [optional] 

## Example

```python
from openapi_client.models.send_email_post200_response_data_receiver import SendEmailPost200ResponseDataReceiver

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailPost200ResponseDataReceiver from a JSON string
send_email_post200_response_data_receiver_instance = SendEmailPost200ResponseDataReceiver.from_json(json)
# print the JSON string representation of the object
print(SendEmailPost200ResponseDataReceiver.to_json())

# convert the object into a dict
send_email_post200_response_data_receiver_dict = send_email_post200_response_data_receiver_instance.to_dict()
# create an instance of SendEmailPost200ResponseDataReceiver from a dict
send_email_post200_response_data_receiver_from_dict = SendEmailPost200ResponseDataReceiver.from_dict(send_email_post200_response_data_receiver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


