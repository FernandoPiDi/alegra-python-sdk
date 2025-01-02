# CreatePayrollRequestGovernmentDataDevengadosCompensaciones

Objeto con la información devengada por concepto de compensaciones

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compensacion** | [**List[CreatePayrollRequestGovernmentDataDevengadosCompensacionesCompensacionInner]**](CreatePayrollRequestGovernmentDataDevengadosCompensacionesCompensacionInner.md) | Array con información sobre devengados por concepto de compensaciones | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_compensaciones import CreatePayrollRequestGovernmentDataDevengadosCompensaciones

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosCompensaciones from a JSON string
create_payroll_request_government_data_devengados_compensaciones_instance = CreatePayrollRequestGovernmentDataDevengadosCompensaciones.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosCompensaciones.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_compensaciones_dict = create_payroll_request_government_data_devengados_compensaciones_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosCompensaciones from a dict
create_payroll_request_government_data_devengados_compensaciones_from_dict = CreatePayrollRequestGovernmentDataDevengadosCompensaciones.from_dict(create_payroll_request_government_data_devengados_compensaciones_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


