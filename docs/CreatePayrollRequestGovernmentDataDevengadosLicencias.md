# CreatePayrollRequestGovernmentDataDevengadosLicencias

Objeto con la información devengada por concepto de licencias

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**licencia_mp** | [**List[CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaMPInner]**](CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaMPInner.md) | Array con información sobre devengados por concepto de licencias de maternidad | [optional] 
**licencia_r** | [**List[CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaRInner]**](CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaRInner.md) | Array con información sobre devengados por concepto de licencias remuneradas | [optional] 
**licencia_nr** | [**List[CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaNRInner]**](CreatePayrollRequestGovernmentDataDevengadosLicenciasLicenciaNRInner.md) | Array con información sobre devengados por concepto de licencias no remuneradas | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_licencias import CreatePayrollRequestGovernmentDataDevengadosLicencias

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosLicencias from a JSON string
create_payroll_request_government_data_devengados_licencias_instance = CreatePayrollRequestGovernmentDataDevengadosLicencias.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosLicencias.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_licencias_dict = create_payroll_request_government_data_devengados_licencias_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosLicencias from a dict
create_payroll_request_government_data_devengados_licencias_from_dict = CreatePayrollRequestGovernmentDataDevengadosLicencias.from_dict(create_payroll_request_government_data_devengados_licencias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


