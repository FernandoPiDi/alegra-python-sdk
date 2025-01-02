# CreatePayrollRequestGovernmentDataDevengadosHENDFsHENDFInner

Objeto con información sobre devengados por concepto de horas extras nocturnas dominicales y festivas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hora_inicio** | **datetime** | Hora de inicio de Horas Extras Nocturnas Dominical y Festivos | [optional] 
**hora_fin** | **datetime** | Hora de fin de Horas Extras Nocturnas Dominical y Festivos | [optional] 
**cantidad** | **float** | Cantidad de Horas Extras Nocturnas Dominical y Festivos | 
**porcentaje** | **str** | Porcentaje al cual corresponde el calculo de 1 hora Extras Nocturnas Dominical y Festivo. Se debe colocar el Porcentaje que corresponda de la tabla de la DIAN para tipos de horas extra | 
**pago** | **float** | Es el valor pagado por el tiempo que se trabaja adicional a la jornada legal o pactada contractualmente. | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_hendfs_hendf_inner import CreatePayrollRequestGovernmentDataDevengadosHENDFsHENDFInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHENDFsHENDFInner from a JSON string
create_payroll_request_government_data_devengados_hendfs_hendf_inner_instance = CreatePayrollRequestGovernmentDataDevengadosHENDFsHENDFInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosHENDFsHENDFInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_hendfs_hendf_inner_dict = create_payroll_request_government_data_devengados_hendfs_hendf_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHENDFsHENDFInner from a dict
create_payroll_request_government_data_devengados_hendfs_hendf_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosHENDFsHENDFInner.from_dict(create_payroll_request_government_data_devengados_hendfs_hendf_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


