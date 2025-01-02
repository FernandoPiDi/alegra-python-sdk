# SendEmailPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Mensaje de confirmación con los datos del documento | [optional] 
**data** | [**SendEmailPost200ResponseData**](SendEmailPost200ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.send_email_post200_response import SendEmailPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailPost200Response from a JSON string
send_email_post200_response_instance = SendEmailPost200Response.from_json(json)
# print the JSON string representation of the object
print(SendEmailPost200Response.to_json())

# convert the object into a dict
send_email_post200_response_dict = send_email_post200_response_instance.to_dict()
# create an instance of SendEmailPost200Response from a dict
send_email_post200_response_from_dict = SendEmailPost200Response.from_dict(send_email_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


