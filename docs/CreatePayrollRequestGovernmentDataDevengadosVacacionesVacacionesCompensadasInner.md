# CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesCompensadasInner

Objeto con información sobre devengados por concepto de vacaciones compensadas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cantidad** | **float** | Número de días que el trabajador estuvo activo durante el mes sin disfrutar sus vacaciones. (Vacaciones NO disfrutadas) | 
**pago** | **float** | Corresponde al valor pagado al trabajador, por el descanso remunerado que no disfrutó y que tiene derecho por haber trabajado un determinado tiempo. (Vacaciones NO disfrutadas) | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_vacaciones_vacaciones_compensadas_inner import CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesCompensadasInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesCompensadasInner from a JSON string
create_payroll_request_government_data_devengados_vacaciones_vacaciones_compensadas_inner_instance = CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesCompensadasInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesCompensadasInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_vacaciones_vacaciones_compensadas_inner_dict = create_payroll_request_government_data_devengados_vacaciones_vacaciones_compensadas_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesCompensadasInner from a dict
create_payroll_request_government_data_devengados_vacaciones_vacaciones_compensadas_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesCompensadasInner.from_dict(create_payroll_request_government_data_devengados_vacaciones_vacaciones_compensadas_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


