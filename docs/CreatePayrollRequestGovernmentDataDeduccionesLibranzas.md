# CreatePayrollRequestGovernmentDataDeduccionesLibranzas

Objeto con la información de deducciones por concepto de libranzas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**libranza** | [**List[CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner]**](CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner.md) | Array con información sobre deducciones por concepto de libranzas | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_deducciones_libranzas import CreatePayrollRequestGovernmentDataDeduccionesLibranzas

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesLibranzas from a JSON string
create_payroll_request_government_data_deducciones_libranzas_instance = CreatePayrollRequestGovernmentDataDeduccionesLibranzas.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDeduccionesLibranzas.to_json())

# convert the object into a dict
create_payroll_request_government_data_deducciones_libranzas_dict = create_payroll_request_government_data_deducciones_libranzas_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesLibranzas from a dict
create_payroll_request_government_data_deducciones_libranzas_from_dict = CreatePayrollRequestGovernmentDataDeduccionesLibranzas.from_dict(create_payroll_request_government_data_deducciones_libranzas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


