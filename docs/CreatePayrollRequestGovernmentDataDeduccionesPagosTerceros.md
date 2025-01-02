# CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros

Objeto con la información de deducciones por concepto de pagos a terceros

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pago_tercero** | **List[float]** | Array con información sobre deducciones por concepto de pagos a terceros | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_deducciones_pagos_terceros import CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros from a JSON string
create_payroll_request_government_data_deducciones_pagos_terceros_instance = CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros.to_json())

# convert the object into a dict
create_payroll_request_government_data_deducciones_pagos_terceros_dict = create_payroll_request_government_data_deducciones_pagos_terceros_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros from a dict
create_payroll_request_government_data_deducciones_pagos_terceros_from_dict = CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros.from_dict(create_payroll_request_government_data_deducciones_pagos_terceros_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


