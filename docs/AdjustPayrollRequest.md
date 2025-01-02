# AdjustPayrollRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | Prefijo de la nómina electrónica | 
**number** | **float** | Número de la nómina electrónica | 
**government_data** | [**CreatePayrollRequestGovernmentData**](CreatePayrollRequestGovernmentData.md) |  | 

## Example

```python
from openapi_client.models.adjust_payroll_request import AdjustPayrollRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustPayrollRequest from a JSON string
adjust_payroll_request_instance = AdjustPayrollRequest.from_json(json)
# print the JSON string representation of the object
print(AdjustPayrollRequest.to_json())

# convert the object into a dict
adjust_payroll_request_dict = adjust_payroll_request_instance.to_dict()
# create an instance of AdjustPayrollRequest from a dict
adjust_payroll_request_from_dict = AdjustPayrollRequest.from_dict(adjust_payroll_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


