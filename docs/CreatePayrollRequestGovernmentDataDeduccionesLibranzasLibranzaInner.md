# CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner

Objeto con información sobre deducción por concepto de libranza

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descripcion** | **str** | Nombre de la Libranza que corresponda a las cuotas que el empleado deba pagar a una entidad financiera, para la amortización de un crédito que le haya sido otorgado por libranza | 
**deduccion** | **float** | Las cuotas que el empleado deba pagar a una entidad financiera, para la amortización de un crédito que le haya sido otorgado por libranza | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_deducciones_libranzas_libranza_inner import CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner from a JSON string
create_payroll_request_government_data_deducciones_libranzas_libranza_inner_instance = CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_deducciones_libranzas_libranza_inner_dict = create_payroll_request_government_data_deducciones_libranzas_libranza_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner from a dict
create_payroll_request_government_data_deducciones_libranzas_libranza_inner_from_dict = CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner.from_dict(create_payroll_request_government_data_deducciones_libranzas_libranza_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


