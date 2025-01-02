# CreatePayrollRequestGovernmentDataPago

Objeto con la información del pago del documento

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forma** | **str** | Formas de Pago del Documento. Se debe colocar el Codigo que corresponda de la tabla de formas de pago de la DIAN | 
**metodo** | **str** | Metodos de Pago del Documento. Se debe colocar el Codigo que corresponda de la tabla de métodos de pago de la DIAN | 
**banco** | **str** | Si el método de pago se realiza de forma bancaria. Se debe colocar el nombre de la entidad bancaria donde el trabajador tiene su cuenta para pago de nómina. | [optional] 
**tipo_cuenta** | **str** | Tipo de Cuenta Bancaria del Empleado donde se realiza la consignación | [optional] 
**numero_cuenta** | **str** | Numero de Cuenta Bancaria del Empleado donde se realiza la consignación | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_pago import CreatePayrollRequestGovernmentDataPago

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataPago from a JSON string
create_payroll_request_government_data_pago_instance = CreatePayrollRequestGovernmentDataPago.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataPago.to_json())

# convert the object into a dict
create_payroll_request_government_data_pago_dict = create_payroll_request_government_data_pago_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataPago from a dict
create_payroll_request_government_data_pago_from_dict = CreatePayrollRequestGovernmentDataPago.from_dict(create_payroll_request_government_data_pago_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


