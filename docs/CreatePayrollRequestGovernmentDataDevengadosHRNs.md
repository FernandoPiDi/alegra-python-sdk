# CreatePayrollRequestGovernmentDataDevengadosHRNs

Objeto con la información devengada por concepto de horas recargo nocturno

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hrn** | [**List[CreatePayrollRequestGovernmentDataDevengadosHRNsHRNInner]**](CreatePayrollRequestGovernmentDataDevengadosHRNsHRNInner.md) | Array con información sobre devengados por concepto de horas recargo nocturno | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_hrns import CreatePayrollRequestGovernmentDataDevengadosHRNs

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHRNs from a JSON string
create_payroll_request_government_data_devengados_hrns_instance = CreatePayrollRequestGovernmentDataDevengadosHRNs.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosHRNs.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_hrns_dict = create_payroll_request_government_data_devengados_hrns_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHRNs from a dict
create_payroll_request_government_data_devengados_hrns_from_dict = CreatePayrollRequestGovernmentDataDevengadosHRNs.from_dict(create_payroll_request_government_data_devengados_hrns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


