# CreatePayrollRequestGovernmentDataDevengadosPrimas

Objeto con información sobre devengados por concepto de primas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cantidad** | **float** | Cantidad de dias trabajados para calculo de Pago de Corte de Prima | 
**pago** | **float** | Valor Pagado por Prima Legal con respecto a Cantidad de Dias | 
**pago_ns** | **float** | Valor Pagado por Prima No Salarial | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_primas import CreatePayrollRequestGovernmentDataDevengadosPrimas

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosPrimas from a JSON string
create_payroll_request_government_data_devengados_primas_instance = CreatePayrollRequestGovernmentDataDevengadosPrimas.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosPrimas.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_primas_dict = create_payroll_request_government_data_devengados_primas_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosPrimas from a dict
create_payroll_request_government_data_devengados_primas_from_dict = CreatePayrollRequestGovernmentDataDevengadosPrimas.from_dict(create_payroll_request_government_data_devengados_primas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


