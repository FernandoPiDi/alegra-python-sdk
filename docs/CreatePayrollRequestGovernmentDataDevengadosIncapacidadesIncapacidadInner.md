# CreatePayrollRequestGovernmentDataDevengadosIncapacidadesIncapacidadInner

Objeto con información sobre devengados por concepto de incapacidades

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fecha_inicio** | **date** | Este dato se debe diligenciar solamente en el registro del mes en que el trabajador presenta o da por iniciada su Incapacidad. | [optional] 
**fecha_fin** | **date** | Este dato se debe diligenciar solamente en el registro del mes en que el trabajador presenta o da por terminada su Incapacidad. | [optional] 
**cantidad** | **float** | Número de días que el trabajador o aprendiz estuvo inactivo por incapacidad (sin importar su origen). | 
**tipo** | **float** | Se debe indicar el codigo al cual corresponda el tipo de incapacidad del Empleado. Se debe colocar el Codigo que corresponda de la tabla de tipos de incapacidades de la DIAN | 
**pago** | **float** | Valor de la prestación económica pagada al trabajador por consecuencia de la falta de capacidad laboral sin importar su origen. | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_incapacidades_incapacidad_inner import CreatePayrollRequestGovernmentDataDevengadosIncapacidadesIncapacidadInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosIncapacidadesIncapacidadInner from a JSON string
create_payroll_request_government_data_devengados_incapacidades_incapacidad_inner_instance = CreatePayrollRequestGovernmentDataDevengadosIncapacidadesIncapacidadInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosIncapacidadesIncapacidadInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_incapacidades_incapacidad_inner_dict = create_payroll_request_government_data_devengados_incapacidades_incapacidad_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosIncapacidadesIncapacidadInner from a dict
create_payroll_request_government_data_devengados_incapacidades_incapacidad_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosIncapacidadesIncapacidadInner.from_dict(create_payroll_request_government_data_devengados_incapacidades_incapacidad_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


