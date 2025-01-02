# CreatePayrollRequestGovernmentDataInformacionGeneral

Objeto con la información general del documento

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periodo_nomina** | **str** | Corresponde al Codigo de Periodo de Nómina. Se debe colocar el Codigo que corresponda de la tabla de periodos de nómina de la DIAN | 
**tipo_moneda** | **str** | Tipo de Moneda utilizada en el documento. Se debe colocar el Codigo que corresponda de la tabla de monedas de la DIAN | 
**trm** | **float** | Tasa Representativa del mercado. Corresponde a la tasa de cambio de la moneda utilizada en el documento en el Campo “TipoMoneda” a Pesos Colombianos. | [optional] 
**notas** | **str** | Campo de libre uso para Observaciones en el documento | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_informacion_general import CreatePayrollRequestGovernmentDataInformacionGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataInformacionGeneral from a JSON string
create_payroll_request_government_data_informacion_general_instance = CreatePayrollRequestGovernmentDataInformacionGeneral.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataInformacionGeneral.to_json())

# convert the object into a dict
create_payroll_request_government_data_informacion_general_dict = create_payroll_request_government_data_informacion_general_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataInformacionGeneral from a dict
create_payroll_request_government_data_informacion_general_from_dict = CreatePayrollRequestGovernmentDataInformacionGeneral.from_dict(create_payroll_request_government_data_informacion_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


