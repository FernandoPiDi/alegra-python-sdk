# CreateCompany200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | [**CreateCompany200ResponseCompany**](CreateCompany200ResponseCompany.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_company200_response import CreateCompany200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompany200Response from a JSON string
create_company200_response_instance = CreateCompany200Response.from_json(json)
# print the JSON string representation of the object
print(CreateCompany200Response.to_json())

# convert the object into a dict
create_company200_response_dict = create_company200_response_instance.to_dict()
# create an instance of CreateCompany200Response from a dict
create_company200_response_from_dict = CreateCompany200Response.from_dict(create_company200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


