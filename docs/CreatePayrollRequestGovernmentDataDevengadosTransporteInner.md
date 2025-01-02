# CreatePayrollRequestGovernmentDataDevengadosTransporteInner

Objeto con la información devengada por concepto de transporte

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auxilio_transporte** | **float** | Parte de los viáticos pagado al trabajador correspondientes a medios de transporte y/o los gastos de representación. | [optional] 
**viatico_manu_aloj_s** | **float** | Parte de los viáticos pagado al trabajador correspondientes a manutención y/o alojamiento. | [optional] 
**viatico_manu_aloj_ns** | **float** | Parte de los viáticos pagado al trabajador correspondientes a manutención y/o alojamiento No Salariales. | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_transporte_inner import CreatePayrollRequestGovernmentDataDevengadosTransporteInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosTransporteInner from a JSON string
create_payroll_request_government_data_devengados_transporte_inner_instance = CreatePayrollRequestGovernmentDataDevengadosTransporteInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosTransporteInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_transporte_inner_dict = create_payroll_request_government_data_devengados_transporte_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosTransporteInner from a dict
create_payroll_request_government_data_devengados_transporte_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosTransporteInner.from_dict(create_payroll_request_government_data_devengados_transporte_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


