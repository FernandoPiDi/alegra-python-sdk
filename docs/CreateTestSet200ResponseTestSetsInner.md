# CreateTestSet200ResponseTestSetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id interno del set de pruebas | [optional] 
**type** | **str** | Tipo de set de pruebas | 
**government_id** | **str** | Identificador del set de pruebas (TestSetld) | 
**status** | **str** | Indica el estado actual de un set de pruebas | [optional] 

## Example

```python
from openapi_client.models.create_test_set200_response_test_sets_inner import CreateTestSet200ResponseTestSetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTestSet200ResponseTestSetsInner from a JSON string
create_test_set200_response_test_sets_inner_instance = CreateTestSet200ResponseTestSetsInner.from_json(json)
# print the JSON string representation of the object
print(CreateTestSet200ResponseTestSetsInner.to_json())

# convert the object into a dict
create_test_set200_response_test_sets_inner_dict = create_test_set200_response_test_sets_inner_instance.to_dict()
# create an instance of CreateTestSet200ResponseTestSetsInner from a dict
create_test_set200_response_test_sets_inner_from_dict = CreateTestSet200ResponseTestSetsInner.from_dict(create_test_set200_response_test_sets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


