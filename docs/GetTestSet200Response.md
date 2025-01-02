# GetTestSet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_set** | [**CreateTestSet200ResponseTestSetsInner**](CreateTestSet200ResponseTestSetsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_test_set200_response import GetTestSet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestSet200Response from a JSON string
get_test_set200_response_instance = GetTestSet200Response.from_json(json)
# print the JSON string representation of the object
print(GetTestSet200Response.to_json())

# convert the object into a dict
get_test_set200_response_dict = get_test_set200_response_instance.to_dict()
# create an instance of GetTestSet200Response from a dict
get_test_set200_response_from_dict = GetTestSet200Response.from_dict(get_test_set200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


