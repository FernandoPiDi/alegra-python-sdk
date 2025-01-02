# CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaNRInner

Objeto con información sobre devengados por concepto de licencias no remuneradas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fecha_inicio** | **date** | Este dato se debe diligenciar solamente en el registro del mes en que el trabajador o aprendiz inicia alguna suspensión, permiso o licencia NO remunerada. | [optional] 
**fecha_fin** | **date** | Este dato se debe diligenciar solamente en el registro del mes en que el trabajador o aprendiz termina la suspensión, permiso o licencia NO remunerada. | [optional] 
**cantidad** | **float** | Número de días que el trabajador o aprendiz efectivamente estuvo inactivo por suspensión, permiso o licencia y que NO le fueron reconocidos en su pago. | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_licencias_licencia_nr_inner import CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaNRInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaNRInner from a JSON string
create_payroll_request_government_data_devengados_licencias_licencia_nr_inner_instance = CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaNRInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaNRInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_licencias_licencia_nr_inner_dict = create_payroll_request_government_data_devengados_licencias_licencia_nr_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaNRInner from a dict
create_payroll_request_government_data_devengados_licencias_licencia_nr_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaNRInner.from_dict(create_payroll_request_government_data_devengados_licencias_licencia_nr_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


