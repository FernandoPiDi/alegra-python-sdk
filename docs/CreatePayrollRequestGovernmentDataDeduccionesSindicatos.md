# CreatePayrollRequestGovernmentDataDeduccionesSindicatos

Objeto con la información de deducciones por concepto de sindicatos

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sindicato** | [**List[CreatePayrollRequestGovernmentDataDeduccionesSindicatosSindicatoInner]**](CreatePayrollRequestGovernmentDataDeduccionesSindicatosSindicatoInner.md) | Array con información sobre deducciones por concepto de sindicatos | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_deducciones_sindicatos import CreatePayrollRequestGovernmentDataDeduccionesSindicatos

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesSindicatos from a JSON string
create_payroll_request_government_data_deducciones_sindicatos_instance = CreatePayrollRequestGovernmentDataDeduccionesSindicatos.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDeduccionesSindicatos.to_json())

# convert the object into a dict
create_payroll_request_government_data_deducciones_sindicatos_dict = create_payroll_request_government_data_deducciones_sindicatos_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesSindicatos from a dict
create_payroll_request_government_data_deducciones_sindicatos_from_dict = CreatePayrollRequestGovernmentDataDeduccionesSindicatos.from_dict(create_payroll_request_government_data_deducciones_sindicatos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


