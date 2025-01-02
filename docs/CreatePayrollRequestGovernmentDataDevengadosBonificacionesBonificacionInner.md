# CreatePayrollRequestGovernmentDataDevengadosBonificacionesBonificacionInner

Objeto con información sobre devengados por concepto de bonificacion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonificacion_s** | **float** | Son valores pagados al trabajador en forma de incentivo o recompensa por la contraprestación directa del servicio. | [optional] 
**bonificacion_ns** | **float** | Son valores de incentivos pagados al trabajador de forma ocasional y por mera liberalidad o los pactados entre las partes de forma expresa como pago no salarial. | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_bonificaciones_bonificacion_inner import CreatePayrollRequestGovernmentDataDevengadosBonificacionesBonificacionInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosBonificacionesBonificacionInner from a JSON string
create_payroll_request_government_data_devengados_bonificaciones_bonificacion_inner_instance = CreatePayrollRequestGovernmentDataDevengadosBonificacionesBonificacionInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosBonificacionesBonificacionInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_bonificaciones_bonificacion_inner_dict = create_payroll_request_government_data_devengados_bonificaciones_bonificacion_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosBonificacionesBonificacionInner from a dict
create_payroll_request_government_data_devengados_bonificaciones_bonificacion_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosBonificacionesBonificacionInner.from_dict(create_payroll_request_government_data_devengados_bonificaciones_bonificacion_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


