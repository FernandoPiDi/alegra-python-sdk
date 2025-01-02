# SendEmailPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | [**SendEmailPost200ResponseDataCompany**](SendEmailPost200ResponseDataCompany.md) |  | [optional] 
**receiver** | [**SendEmailPost200ResponseDataReceiver**](SendEmailPost200ResponseDataReceiver.md) |  | [optional] 
**document** | [**SendEmailPost200ResponseDataDocument**](SendEmailPost200ResponseDataDocument.md) |  | [optional] 
**attached_documents** | **str** | Mensaje que indica que un archivo adjunto fue agregado | [optional] 

## Example

```python
from openapi_client.models.send_email_post200_response_data import SendEmailPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailPost200ResponseData from a JSON string
send_email_post200_response_data_instance = SendEmailPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print(SendEmailPost200ResponseData.to_json())

# convert the object into a dict
send_email_post200_response_data_dict = send_email_post200_response_data_instance.to_dict()
# create an instance of SendEmailPost200ResponseData from a dict
send_email_post200_response_data_from_dict = SendEmailPost200ResponseData.from_dict(send_email_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


