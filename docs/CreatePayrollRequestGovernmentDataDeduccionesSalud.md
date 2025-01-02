# CreatePayrollRequestGovernmentDataDeduccionesSalud

Objeto con información sobre deducciones por conceptos de salud

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**porcentaje** | **float** | Debe corresponder al porcentaje de deducción de salud que paga el trabajador | 
**deduccion** | **float** | El trabajador debe estar afiliado al sistema de salud. La cotización por salud que corresponde al 12.5% de la base del aporte, se hace en conjunto con la empresa. Ésta última aporta el 8.5%, y el empleado debe aportar el 4% restante. Ese 4% es el valor que se debe descontar (deducir) del total devengado a cargo del empleado. | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_deducciones_salud import CreatePayrollRequestGovernmentDataDeduccionesSalud

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesSalud from a JSON string
create_payroll_request_government_data_deducciones_salud_instance = CreatePayrollRequestGovernmentDataDeduccionesSalud.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDeduccionesSalud.to_json())

# convert the object into a dict
create_payroll_request_government_data_deducciones_salud_dict = create_payroll_request_government_data_deducciones_salud_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesSalud from a dict
create_payroll_request_government_data_deducciones_salud_from_dict = CreatePayrollRequestGovernmentDataDeduccionesSalud.from_dict(create_payroll_request_government_data_deducciones_salud_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


