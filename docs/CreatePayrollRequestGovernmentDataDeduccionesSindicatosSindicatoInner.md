# CreatePayrollRequestGovernmentDataDeduccionesSindicatosSindicatoInner

Objeto con información sobre deducción por concepto de sindicato

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**porcentaje** | **float** | Porcentaje establecido en la ley o por estatutos del sindicato. | 
**deduccion** | **float** | Las cuotas que los trabajadores sindicalizados deben aportar al sindicato al que estén afiliados, y siempre que medie autorización del empleado | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_deducciones_sindicatos_sindicato_inner import CreatePayrollRequestGovernmentDataDeduccionesSindicatosSindicatoInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesSindicatosSindicatoInner from a JSON string
create_payroll_request_government_data_deducciones_sindicatos_sindicato_inner_instance = CreatePayrollRequestGovernmentDataDeduccionesSindicatosSindicatoInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDeduccionesSindicatosSindicatoInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_deducciones_sindicatos_sindicato_inner_dict = create_payroll_request_government_data_deducciones_sindicatos_sindicato_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesSindicatosSindicatoInner from a dict
create_payroll_request_government_data_deducciones_sindicatos_sindicato_inner_from_dict = CreatePayrollRequestGovernmentDataDeduccionesSindicatosSindicatoInner.from_dict(create_payroll_request_government_data_deducciones_sindicatos_sindicato_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


