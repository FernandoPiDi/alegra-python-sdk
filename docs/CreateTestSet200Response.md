# CreateTestSet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_sets** | [**List[CreateTestSet200ResponseTestSetsInner]**](CreateTestSet200ResponseTestSetsInner.md) | Array con sets de pruebas | [optional] 

## Example

```python
from openapi_client.models.create_test_set200_response import CreateTestSet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTestSet200Response from a JSON string
create_test_set200_response_instance = CreateTestSet200Response.from_json(json)
# print the JSON string representation of the object
print(CreateTestSet200Response.to_json())

# convert the object into a dict
create_test_set200_response_dict = create_test_set200_response_instance.to_dict()
# create an instance of CreateTestSet200Response from a dict
create_test_set200_response_from_dict = CreateTestSet200Response.from_dict(create_test_set200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


