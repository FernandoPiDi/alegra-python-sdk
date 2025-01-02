# CreatePayrollRequestGovernmentDataDevengadosHuelgasLegales

Objeto con la información devengada por concepto de huelgas legales

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**huelga_legal** | [**List[CreatePayrollRequestGovernmentDataDevengadosHuelgasLegalesHuelgaLegalInner]**](CreatePayrollRequestGovernmentDataDevengadosHuelgasLegalesHuelgaLegalInner.md) | Array con información sobre devengados por concepto de huelgas legales | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_huelgas_legales import CreatePayrollRequestGovernmentDataDevengadosHuelgasLegales

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHuelgasLegales from a JSON string
create_payroll_request_government_data_devengados_huelgas_legales_instance = CreatePayrollRequestGovernmentDataDevengadosHuelgasLegales.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosHuelgasLegales.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_huelgas_legales_dict = create_payroll_request_government_data_devengados_huelgas_legales_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHuelgasLegales from a dict
create_payroll_request_government_data_devengados_huelgas_legales_from_dict = CreatePayrollRequestGovernmentDataDevengadosHuelgasLegales.from_dict(create_payroll_request_government_data_devengados_huelgas_legales_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


