# CreatePayrollRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | [**CreatePayrollRequestCompany**](CreatePayrollRequestCompany.md) |  | [optional] 
**prefix** | **str** | Prefijo de la nómina electrónica | [optional] 
**number** | **float** | Número de la nómina electrónica | 
**government_data** | [**CreatePayrollRequestGovernmentData**](CreatePayrollRequestGovernmentData.md) |  | 

## Example

```python
from openapi_client.models.create_payroll_request import CreatePayrollRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequest from a JSON string
create_payroll_request_instance = CreatePayrollRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequest.to_json())

# convert the object into a dict
create_payroll_request_dict = create_payroll_request_instance.to_dict()
# create an instance of CreatePayrollRequest from a dict
create_payroll_request_from_dict = CreatePayrollRequest.from_dict(create_payroll_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


