# CancelPayroll200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payroll** | [**GetTestSetByGovernmentId200ResponseEmission**](GetTestSetByGovernmentId200ResponseEmission.md) |  | [optional] 
**cancellation** | [**GetTestSetByGovernmentId200ResponseEmission**](GetTestSetByGovernmentId200ResponseEmission.md) |  | [optional] 

## Example

```python
from openapi_client.models.cancel_payroll200_response import CancelPayroll200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CancelPayroll200Response from a JSON string
cancel_payroll200_response_instance = CancelPayroll200Response.from_json(json)
# print the JSON string representation of the object
print(CancelPayroll200Response.to_json())

# convert the object into a dict
cancel_payroll200_response_dict = cancel_payroll200_response_instance.to_dict()
# create an instance of CancelPayroll200Response from a dict
cancel_payroll200_response_from_dict = CancelPayroll200Response.from_dict(cancel_payroll200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


