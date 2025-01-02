# CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesComunesInner

Objeto con información sobre devengados por concepto de vaciones comunes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fecha_inicio** | **date** | Este dato se debe diligenciar solamente en el registro del mes en que el trabajador presenta el inicio del disfrute de sus vacaciones en tiempo. | [optional] 
**fecha_fin** | **date** | Este dato se debe diligenciar solamente en el registro del mes en que el trabajador regresa o termina el disfrute de sus vacaciones. | [optional] 
**cantidad** | **float** | Número de días que el trabajador estuvo inactivo durante el mes por vacaciones | 
**pago** | **float** | Corresponde al valor pagado al trabajador, por el descanso remunerado que tiene derecho por haber trabajado un determinado tiempo. (Vacaciones SI disfrutadas) | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_vacaciones_vacaciones_comunes_inner import CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesComunesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesComunesInner from a JSON string
create_payroll_request_government_data_devengados_vacaciones_vacaciones_comunes_inner_instance = CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesComunesInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesComunesInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_vacaciones_vacaciones_comunes_inner_dict = create_payroll_request_government_data_devengados_vacaciones_vacaciones_comunes_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesComunesInner from a dict
create_payroll_request_government_data_devengados_vacaciones_vacaciones_comunes_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesComunesInner.from_dict(create_payroll_request_government_data_devengados_vacaciones_vacaciones_comunes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


