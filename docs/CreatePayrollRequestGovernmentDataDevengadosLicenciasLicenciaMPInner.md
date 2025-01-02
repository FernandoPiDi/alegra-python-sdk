# CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaMPInner

Objeto con información sobre devengados por concepto de licencias de maternidad

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fecha_inicio** | **date** | Fecha donde da inicio la Licencia de Maternidad o Paternidad | [optional] 
**fecha_fin** | **date** | Fecha donde termina la Licencia de Maternidad o Paternidad | [optional] 
**cantidad** | **float** | Número de días que el trabajador o aprendiz efectivamente estuvo inactivo por licencia de maternidad o paternidad. | 
**pago** | **float** | Valor pagado al trabajador del descanso remunerado que la ley confiere por el nacimiento de un hijo, y que es reconocido y pagado por la EPS a la que está afiliado el padre o la madre, o en su defecto por el empleador. | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_licencias_licencia_mp_inner import CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaMPInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaMPInner from a JSON string
create_payroll_request_government_data_devengados_licencias_licencia_mp_inner_instance = CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaMPInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaMPInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_licencias_licencia_mp_inner_dict = create_payroll_request_government_data_devengados_licencias_licencia_mp_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaMPInner from a dict
create_payroll_request_government_data_devengados_licencias_licencia_mp_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaMPInner.from_dict(create_payroll_request_government_data_devengados_licencias_licencia_mp_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


