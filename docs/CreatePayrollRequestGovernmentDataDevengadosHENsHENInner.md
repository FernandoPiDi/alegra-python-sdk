# CreatePayrollRequestGovernmentDataDevengadosHENsHENInner

Objeto con información sobre devengados por concepto de horas extras nocturnas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hora_inicio** | **datetime** | Hora de inicio de Hora Extra Nocturna | [optional] 
**hora_fin** | **datetime** | Hora de fin de Hora Extra Nocturna | [optional] 
**cantidad** | **float** | Cantidad de Horas Extra Nocturna | 
**porcentaje** | **str** | Porcentaje al cual corresponde el calculo de 1 hora Extra Nocturna. Se debe colocar el Porcentaje que corresponda de la tabla de la DIAN para tipos de horas extra | 
**pago** | **float** | Es el valor pagado por el tiempo que se trabaja adicional a la jornada legal o pactada contractualmente. | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_hens_hen_inner import CreatePayrollRequestGovernmentDataDevengadosHENsHENInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHENsHENInner from a JSON string
create_payroll_request_government_data_devengados_hens_hen_inner_instance = CreatePayrollRequestGovernmentDataDevengadosHENsHENInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosHENsHENInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_hens_hen_inner_dict = create_payroll_request_government_data_devengados_hens_hen_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHENsHENInner from a dict
create_payroll_request_government_data_devengados_hens_hen_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosHENsHENInner.from_dict(create_payroll_request_government_data_devengados_hens_hen_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


