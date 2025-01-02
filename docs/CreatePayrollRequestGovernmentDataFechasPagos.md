# CreatePayrollRequestGovernmentDataFechasPagos

Objeto con la información de fechas de pago del documento

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fecha_pago** | **List[date]** | Array con fechas de Pago de la Nómina | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_fechas_pagos import CreatePayrollRequestGovernmentDataFechasPagos

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataFechasPagos from a JSON string
create_payroll_request_government_data_fechas_pagos_instance = CreatePayrollRequestGovernmentDataFechasPagos.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataFechasPagos.to_json())

# convert the object into a dict
create_payroll_request_government_data_fechas_pagos_dict = create_payroll_request_government_data_fechas_pagos_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataFechasPagos from a dict
create_payroll_request_government_data_fechas_pagos_from_dict = CreatePayrollRequestGovernmentDataFechasPagos.from_dict(create_payroll_request_government_data_fechas_pagos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


