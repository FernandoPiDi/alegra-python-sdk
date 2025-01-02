# CreatePayrollRequestGovernmentDataDevengadosPagosTerceros

Objeto con la información devengada por concepto de pagos a terceros

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pago_tercero** | **List[float]** | Array con información sobre devengados por concepto de pagos a terceros | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_pagos_terceros import CreatePayrollRequestGovernmentDataDevengadosPagosTerceros

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosPagosTerceros from a JSON string
create_payroll_request_government_data_devengados_pagos_terceros_instance = CreatePayrollRequestGovernmentDataDevengadosPagosTerceros.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosPagosTerceros.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_pagos_terceros_dict = create_payroll_request_government_data_devengados_pagos_terceros_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosPagosTerceros from a dict
create_payroll_request_government_data_devengados_pagos_terceros_from_dict = CreatePayrollRequestGovernmentDataDevengadosPagosTerceros.from_dict(create_payroll_request_government_data_devengados_pagos_terceros_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


