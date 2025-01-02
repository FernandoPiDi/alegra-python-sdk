# CancelPayrollRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | Prefijo de la anulación de la nómina electrónica | 
**number** | **str** | Número consecutivo de la anulación de la nómina electrónica | 

## Example

```python
from openapi_client.models.cancel_payroll_request import CancelPayrollRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelPayrollRequest from a JSON string
cancel_payroll_request_instance = CancelPayrollRequest.from_json(json)
# print the JSON string representation of the object
print(CancelPayrollRequest.to_json())

# convert the object into a dict
cancel_payroll_request_dict = cancel_payroll_request_instance.to_dict()
# create an instance of CancelPayrollRequest from a dict
cancel_payroll_request_from_dict = CancelPayrollRequest.from_dict(cancel_payroll_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


