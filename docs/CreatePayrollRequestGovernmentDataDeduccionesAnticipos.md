# CreatePayrollRequestGovernmentDataDeduccionesAnticipos

Objeto con la información de deducciones por concepto de anticipos

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anticipo** | **List[float]** | Array con información sobre deducciones por concepto de anticipos | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_deducciones_anticipos import CreatePayrollRequestGovernmentDataDeduccionesAnticipos

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesAnticipos from a JSON string
create_payroll_request_government_data_deducciones_anticipos_instance = CreatePayrollRequestGovernmentDataDeduccionesAnticipos.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDeduccionesAnticipos.to_json())

# convert the object into a dict
create_payroll_request_government_data_deducciones_anticipos_dict = create_payroll_request_government_data_deducciones_anticipos_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesAnticipos from a dict
create_payroll_request_government_data_deducciones_anticipos_from_dict = CreatePayrollRequestGovernmentDataDeduccionesAnticipos.from_dict(create_payroll_request_government_data_deducciones_anticipos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


