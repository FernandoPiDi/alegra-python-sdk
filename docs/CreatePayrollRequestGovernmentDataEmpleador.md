# CreatePayrollRequestGovernmentDataEmpleador

Objeto con la información del empleador

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**razon_social** | **str** | Debe corresponder al Nombre de la Razón Social del Empleador | [optional] 
**primer_apellido** | **str** | Primer Apellido del empleador | [optional] 
**segundo_apellido** | **str** | Segundo Apellido del empleador | [optional] 
**primer_nombre** | **str** | Primer Nombre del empleador | [optional] 
**otros_nombres** | **str** | Otros Nombres del empleador | [optional] 
**nit** | **float** | Debe corresponder al NIT del Empleador que realiza el documento, sin guiones ni DV | 
**dv** | **float** | Debe corresponder al DV del NIT del Empleador que realiza el documento | 
**pais** | **str** | Código del país donde se encuentra ubicada la empresa del empleador en el mes que se esta reportando. Se debe colocar el Codigo que corresponda de la tabla de paises de la DIAN | 
**municipio_ciudad** | **str** | Código del municipio o ciudad donde se encuentra ubicada la empresa del empleador en el mes que se esta reportando. Se debe colocar el Codigo que corresponda de la tabla de municipios de la DIAN | 
**direccion** | **str** | Debe corresponder a la dirección del lugar físico de expedición del documento. | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_empleador import CreatePayrollRequestGovernmentDataEmpleador

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataEmpleador from a JSON string
create_payroll_request_government_data_empleador_instance = CreatePayrollRequestGovernmentDataEmpleador.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataEmpleador.to_json())

# convert the object into a dict
create_payroll_request_government_data_empleador_dict = create_payroll_request_government_data_empleador_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataEmpleador from a dict
create_payroll_request_government_data_empleador_from_dict = CreatePayrollRequestGovernmentDataEmpleador.from_dict(create_payroll_request_government_data_empleador_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


