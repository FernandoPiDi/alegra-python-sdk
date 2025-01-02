# CreatePayrollRequestGovernmentDataDevengadosVacaciones

Objeto con la información devengada por concepto de vacaciones

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vacaciones_comunes** | [**List[CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesComunesInner]**](CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesComunesInner.md) | Array con información sobre devengados por concepto de vacaciones comunes | [optional] 
**vacaciones_compensadas** | [**List[CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesCompensadasInner]**](CreatePayrollRequestGovernmentDataDevengadosVacacionesVacacionesCompensadasInner.md) | Array con información sobre devengados por concepto de vacaciones compensadas | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_vacaciones import CreatePayrollRequestGovernmentDataDevengadosVacaciones

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosVacaciones from a JSON string
create_payroll_request_government_data_devengados_vacaciones_instance = CreatePayrollRequestGovernmentDataDevengadosVacaciones.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosVacaciones.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_vacaciones_dict = create_payroll_request_government_data_devengados_vacaciones_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosVacaciones from a dict
create_payroll_request_government_data_devengados_vacaciones_from_dict = CreatePayrollRequestGovernmentDataDevengadosVacaciones.from_dict(create_payroll_request_government_data_devengados_vacaciones_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


