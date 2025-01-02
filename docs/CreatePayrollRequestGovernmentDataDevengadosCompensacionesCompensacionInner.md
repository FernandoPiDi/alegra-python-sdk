# CreatePayrollRequestGovernmentDataDevengadosCompensacionesCompensacionInner

Objeto con información sobre devengados por concepto de compensaciones

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compensacion_o** | **float** | Suma de dinero definido en el régimen de compensaciones como retribución mensual recibido por el asociado por la ejecución de su actividad material o inmaterial, la cual se fija teniendo en cuenta el tipo de labor desempeñada, el rendimiento o la productividad y la cantidad de trabajo aportado. El monto de la compensación ordinaria podrá ser una suma básica igual para todos los asociados (Ordinaria). | 
**compensacion_e** | **float** | Los demás pagos adicionales a la Compensación Ordinaria que recibe el asociado como retribución por su trabajo, definidos en el régimen de compensaciones (Extraordinaria). | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_compensaciones_compensacion_inner import CreatePayrollRequestGovernmentDataDevengadosCompensacionesCompensacionInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosCompensacionesCompensacionInner from a JSON string
create_payroll_request_government_data_devengados_compensaciones_compensacion_inner_instance = CreatePayrollRequestGovernmentDataDevengadosCompensacionesCompensacionInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosCompensacionesCompensacionInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_compensaciones_compensacion_inner_dict = create_payroll_request_government_data_devengados_compensaciones_compensacion_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosCompensacionesCompensacionInner from a dict
create_payroll_request_government_data_devengados_compensaciones_compensacion_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosCompensacionesCompensacionInner.from_dict(create_payroll_request_government_data_devengados_compensaciones_compensacion_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


