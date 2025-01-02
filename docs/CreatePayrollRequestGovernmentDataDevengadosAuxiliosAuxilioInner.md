# CreatePayrollRequestGovernmentDataDevengadosAuxiliosAuxilioInner

Objeto con información sobre devengados por concepto de auxilios

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auxilio_s** | **float** | Son beneficios, ayudas o apoyos económicos, pagados al trabajador de forma habitual o pactados entre las partes como factor salarial. | [optional] 
**auxilio_ns** | **float** | Son beneficios, ayudas o apoyos económicos, pagados al trabajador de forma ocasional y por mera liberalidad o los pactados entre las partes de forma expresa como pago no salarial. | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_auxilios_auxilio_inner import CreatePayrollRequestGovernmentDataDevengadosAuxiliosAuxilioInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosAuxiliosAuxilioInner from a JSON string
create_payroll_request_government_data_devengados_auxilios_auxilio_inner_instance = CreatePayrollRequestGovernmentDataDevengadosAuxiliosAuxilioInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosAuxiliosAuxilioInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_auxilios_auxilio_inner_dict = create_payroll_request_government_data_devengados_auxilios_auxilio_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosAuxiliosAuxilioInner from a dict
create_payroll_request_government_data_devengados_auxilios_auxilio_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosAuxiliosAuxilioInner.from_dict(create_payroll_request_government_data_devengados_auxilios_auxilio_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


