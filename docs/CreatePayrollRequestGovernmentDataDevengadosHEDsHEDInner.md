# CreatePayrollRequestGovernmentDataDevengadosHEDsHEDInner

Objeto con información sobre devengados por concepto de horas extras diarias

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hora_inicio** | **datetime** | Hora de inicio de Hora Extra Diurna | [optional] 
**hora_fin** | **datetime** | Hora de fin de Hora Extra Diurna | [optional] 
**cantidad** | **float** | Cantidad de Horas Extra Diurna | 
**porcentaje** | **str** | Porcentaje al cual corresponde el calculo de 1 hora Extra Diurna. Se debe colocar el Porcentaje que corresponda de la tabla de la DIAN para tipos de horas extra | 
**pago** | **float** | Es el valor pagado por el tiempo que se trabaja adicional a la jornada legal o pactada contractualmente. | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_heds_hed_inner import CreatePayrollRequestGovernmentDataDevengadosHEDsHEDInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHEDsHEDInner from a JSON string
create_payroll_request_government_data_devengados_heds_hed_inner_instance = CreatePayrollRequestGovernmentDataDevengadosHEDsHEDInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosHEDsHEDInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_heds_hed_inner_dict = create_payroll_request_government_data_devengados_heds_hed_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHEDsHEDInner from a dict
create_payroll_request_government_data_devengados_heds_hed_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosHEDsHEDInner.from_dict(create_payroll_request_government_data_devengados_heds_hed_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


