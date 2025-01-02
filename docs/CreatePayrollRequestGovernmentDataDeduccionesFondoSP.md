# CreatePayrollRequestGovernmentDataDeduccionesFondoSP

Objeto con información sobre deducciones por conceptos de fondos de seguridad pensional

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**porcentaje** | **float** | Debe corresponder al porcentaje de deducción de fondo de seguridad pensional que paga el trabajador | [optional] 
**deduccion_sp** | **float** | Todo trabajador que devengue un sueldo que sea igual o superior a 4 salarios mininos, debe aportar un 1% al Fondo de solidaridad pensional. | [optional] 
**porcentaje_sub** | **float** | Se debe colocar el Porcentaje que correspondiente al Fondo de Subsistencia correspondiente | [optional] 
**deduccion_sub** | **float** | Valor Pagado correspondiente a Fondo de Subsistencia por parte del trabajador | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_deducciones_fondo_sp import CreatePayrollRequestGovernmentDataDeduccionesFondoSP

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesFondoSP from a JSON string
create_payroll_request_government_data_deducciones_fondo_sp_instance = CreatePayrollRequestGovernmentDataDeduccionesFondoSP.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDeduccionesFondoSP.to_json())

# convert the object into a dict
create_payroll_request_government_data_deducciones_fondo_sp_dict = create_payroll_request_government_data_deducciones_fondo_sp_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesFondoSP from a dict
create_payroll_request_government_data_deducciones_fondo_sp_from_dict = CreatePayrollRequestGovernmentDataDeduccionesFondoSP.from_dict(create_payroll_request_government_data_deducciones_fondo_sp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


