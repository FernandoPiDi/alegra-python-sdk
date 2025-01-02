# CreatePayrollRequestGovernmentDataDevengadosHEDs

Objeto con la información devengada por concepto de horas extras diarias

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hed** | [**List[CreatePayrollRequestGovernmentDataDevengadosHEDsHEDInner]**](CreatePayrollRequestGovernmentDataDevengadosHEDsHEDInner.md) | Array con información sobre devengados por concepto de horas extras diarias | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_heds import CreatePayrollRequestGovernmentDataDevengadosHEDs

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHEDs from a JSON string
create_payroll_request_government_data_devengados_heds_instance = CreatePayrollRequestGovernmentDataDevengadosHEDs.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosHEDs.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_heds_dict = create_payroll_request_government_data_devengados_heds_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHEDs from a dict
create_payroll_request_government_data_devengados_heds_from_dict = CreatePayrollRequestGovernmentDataDevengadosHEDs.from_dict(create_payroll_request_government_data_devengados_heds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


