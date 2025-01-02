# CreatePayrollRequestGovernmentDataDevengadosBasico

Objeto con la información basica de los devengados

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dias_trabajados** | **float** | Número de días que el trabajador o aprendiz efectivamente estuvo ejecutando sus labores en la empresa. | 
**sueldo_trabajado** | **float** | Corresponde al valor que el empleador paga de forma periódica al trabajador como contraprestación por el trabajo realizado, este puede ser fijo o variable de acuerdo a la unidad de tiempo en que las partes hayan acordado el pago, teniendo como base el día o la hora trabajada. | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_basico import CreatePayrollRequestGovernmentDataDevengadosBasico

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosBasico from a JSON string
create_payroll_request_government_data_devengados_basico_instance = CreatePayrollRequestGovernmentDataDevengadosBasico.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosBasico.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_basico_dict = create_payroll_request_government_data_devengados_basico_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosBasico from a dict
create_payroll_request_government_data_devengados_basico_from_dict = CreatePayrollRequestGovernmentDataDevengadosBasico.from_dict(create_payroll_request_government_data_devengados_basico_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


