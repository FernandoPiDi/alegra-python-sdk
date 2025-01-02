# GetPayrollCancellations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**GetPayrolls200ResponseMetadata**](GetPayrolls200ResponseMetadata.md) |  | [optional] 
**payroll_cancellations** | [**List[GetTestSetByGovernmentId200ResponseEmission]**](GetTestSetByGovernmentId200ResponseEmission.md) | Array con cancelaciones de nómina | [optional] 

## Example

```python
from openapi_client.models.get_payroll_cancellations200_response import GetPayrollCancellations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayrollCancellations200Response from a JSON string
get_payroll_cancellations200_response_instance = GetPayrollCancellations200Response.from_json(json)
# print the JSON string representation of the object
print(GetPayrollCancellations200Response.to_json())

# convert the object into a dict
get_payroll_cancellations200_response_dict = get_payroll_cancellations200_response_instance.to_dict()
# create an instance of GetPayrollCancellations200Response from a dict
get_payroll_cancellations200_response_from_dict = GetPayrollCancellations200Response.from_dict(get_payroll_cancellations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


