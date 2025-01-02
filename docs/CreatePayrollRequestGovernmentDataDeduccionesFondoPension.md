# CreatePayrollRequestGovernmentDataDeduccionesFondoPension

Objeto con información sobre deducciones por conceptos de fondos de pensión

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**porcentaje** | **float** | Debe corresponder al porcentaje de deducción de fondo de pensión que paga el trabajador | 
**deduccion** | **float** | El trabajador también debe estar afiliado al sistema de pensiones. La cotización por pensión está a cargo tanto de la empresa como del empleado. Del total del aporte (16%), la empresa aporta el 75% (12%) y el trabajador aporta el restante 25% (4%). Como el trabajador debe aportar un 4% por concepto de pensión, este valor se le descuenta (deduce) del valor devengado en el respectivo periodo (mes o quincena). | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_deducciones_fondo_pension import CreatePayrollRequestGovernmentDataDeduccionesFondoPension

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesFondoPension from a JSON string
create_payroll_request_government_data_deducciones_fondo_pension_instance = CreatePayrollRequestGovernmentDataDeduccionesFondoPension.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDeduccionesFondoPension.to_json())

# convert the object into a dict
create_payroll_request_government_data_deducciones_fondo_pension_dict = create_payroll_request_government_data_deducciones_fondo_pension_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesFondoPension from a dict
create_payroll_request_government_data_deducciones_fondo_pension_from_dict = CreatePayrollRequestGovernmentDataDeduccionesFondoPension.from_dict(create_payroll_request_government_data_deducciones_fondo_pension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


