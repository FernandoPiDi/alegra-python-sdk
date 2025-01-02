# CreatePayrollRequestGovernmentDataDevengadosIncapacidades

Objeto con la información devengada por concepto de incapacidades

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incapacidad** | [**List[CreatePayrollRequestGovernmentDataDevengadosIncapacidadesIncapacidadInner]**](CreatePayrollRequestGovernmentDataDevengadosIncapacidadesIncapacidadInner.md) | Array con información sobre devengados por concepto de incapacidades | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_incapacidades import CreatePayrollRequestGovernmentDataDevengadosIncapacidades

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosIncapacidades from a JSON string
create_payroll_request_government_data_devengados_incapacidades_instance = CreatePayrollRequestGovernmentDataDevengadosIncapacidades.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosIncapacidades.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_incapacidades_dict = create_payroll_request_government_data_devengados_incapacidades_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosIncapacidades from a dict
create_payroll_request_government_data_devengados_incapacidades_from_dict = CreatePayrollRequestGovernmentDataDevengadosIncapacidades.from_dict(create_payroll_request_government_data_devengados_incapacidades_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


