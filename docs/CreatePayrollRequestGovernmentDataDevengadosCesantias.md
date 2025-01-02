# CreatePayrollRequestGovernmentDataDevengadosCesantias

Objeto con información sobre devengados por concepto de cesantías

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pago** | **float** | Valor Pagado por Cesantias | 
**porcentaje** | **float** | Porcentaje que corresponde al Interes de Cesantia de Ley | 
**pago_intereses** | **float** | Pago de los Intereses de Cesantia otorgada por Ley. | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_cesantias import CreatePayrollRequestGovernmentDataDevengadosCesantias

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosCesantias from a JSON string
create_payroll_request_government_data_devengados_cesantias_instance = CreatePayrollRequestGovernmentDataDevengadosCesantias.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosCesantias.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_cesantias_dict = create_payroll_request_government_data_devengados_cesantias_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosCesantias from a dict
create_payroll_request_government_data_devengados_cesantias_from_dict = CreatePayrollRequestGovernmentDataDevengadosCesantias.from_dict(create_payroll_request_government_data_devengados_cesantias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


