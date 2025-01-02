# CreateTestSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | [**CreateTestSetRequestCompany**](CreateTestSetRequestCompany.md) |  | [optional] 
**type** | **str** | Tipo de set de pruebas | 
**government_id** | **str** | Identificador del set de pruebas (TestSetld) | 

## Example

```python
from openapi_client.models.create_test_set_request import CreateTestSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTestSetRequest from a JSON string
create_test_set_request_instance = CreateTestSetRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTestSetRequest.to_json())

# convert the object into a dict
create_test_set_request_dict = create_test_set_request_instance.to_dict()
# create an instance of CreateTestSetRequest from a dict
create_test_set_request_from_dict = CreateTestSetRequest.from_dict(create_test_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


