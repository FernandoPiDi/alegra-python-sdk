# CreatePayrollRequestGovernmentDataDevengadosAuxilios

Objeto con la información devengada por concepto de auxilios

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auxilio** | [**List[CreatePayrollRequestGovernmentDataDevengadosAuxiliosAuxilioInner]**](CreatePayrollRequestGovernmentDataDevengadosAuxiliosAuxilioInner.md) | Array con información sobre devengados por concepto de auxilios | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_auxilios import CreatePayrollRequestGovernmentDataDevengadosAuxilios

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosAuxilios from a JSON string
create_payroll_request_government_data_devengados_auxilios_instance = CreatePayrollRequestGovernmentDataDevengadosAuxilios.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosAuxilios.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_auxilios_dict = create_payroll_request_government_data_devengados_auxilios_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosAuxilios from a dict
create_payroll_request_government_data_devengados_auxilios_from_dict = CreatePayrollRequestGovernmentDataDevengadosAuxilios.from_dict(create_payroll_request_government_data_devengados_auxilios_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


