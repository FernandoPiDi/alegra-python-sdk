# CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaRInner

Objeto con información sobre devengados por concepto de licencias remuneradas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fecha_inicio** | **date** | Este dato se debe diligenciar solamente en el registro del mes en que el trabajador o aprendiz inicia algún permiso o licencia remunerada. | [optional] 
**fecha_fin** | **date** | Este dato se debe diligenciar solamente en el registro del mes en que el trabajador o aprendiz termina el permiso o licencia remunerada. | [optional] 
**cantidad** | **float** | Número de días que el trabajador o aprendiz efectivamente estuvo inactivo por permiso o licencia pero que le fueron reconocidos en su pago. | 
**pago** | **float** | Valor pagado al trabajador corresponde a tiempo no laborado, que por ley o por acuerdo con el empleador se le concede | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_licencias_licencia_r_inner import CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaRInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaRInner from a JSON string
create_payroll_request_government_data_devengados_licencias_licencia_r_inner_instance = CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaRInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaRInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_licencias_licencia_r_inner_dict = create_payroll_request_government_data_devengados_licencias_licencia_r_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaRInner from a dict
create_payroll_request_government_data_devengados_licencias_licencia_r_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaRInner.from_dict(create_payroll_request_government_data_devengados_licencias_licencia_r_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


