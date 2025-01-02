# CreatePayrollRequestGovernmentDataDeduccionesSanciones

Objeto con la información de deducciones por concepto de sanciones

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sancion** | [**List[CreatePayrollRequestGovernmentDataDeduccionesSancionesSancionInner]**](CreatePayrollRequestGovernmentDataDeduccionesSancionesSancionInner.md) | Array con información sobre deducciones por concepto de sanciones | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_deducciones_sanciones import CreatePayrollRequestGovernmentDataDeduccionesSanciones

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesSanciones from a JSON string
create_payroll_request_government_data_deducciones_sanciones_instance = CreatePayrollRequestGovernmentDataDeduccionesSanciones.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDeduccionesSanciones.to_json())

# convert the object into a dict
create_payroll_request_government_data_deducciones_sanciones_dict = create_payroll_request_government_data_deducciones_sanciones_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesSanciones from a dict
create_payroll_request_government_data_deducciones_sanciones_from_dict = CreatePayrollRequestGovernmentDataDeduccionesSanciones.from_dict(create_payroll_request_government_data_deducciones_sanciones_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


