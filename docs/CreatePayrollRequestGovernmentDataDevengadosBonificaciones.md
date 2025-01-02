# CreatePayrollRequestGovernmentDataDevengadosBonificaciones

Objeto con la información devengada por concepto de bonificaciones

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonificacion** | [**List[CreatePayrollRequestGovernmentDataDevengadosBonificacionesBonificacionInner]**](CreatePayrollRequestGovernmentDataDevengadosBonificacionesBonificacionInner.md) | Array con información sobre devengados por concepto de bonificaciones | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_bonificaciones import CreatePayrollRequestGovernmentDataDevengadosBonificaciones

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosBonificaciones from a JSON string
create_payroll_request_government_data_devengados_bonificaciones_instance = CreatePayrollRequestGovernmentDataDevengadosBonificaciones.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosBonificaciones.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_bonificaciones_dict = create_payroll_request_government_data_devengados_bonificaciones_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosBonificaciones from a dict
create_payroll_request_government_data_devengados_bonificaciones_from_dict = CreatePayrollRequestGovernmentDataDevengadosBonificaciones.from_dict(create_payroll_request_government_data_devengados_bonificaciones_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


