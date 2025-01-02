# CreatePayrollRequestGovernmentDataPeriodo

Objeto con la información del periodo de nómina que se desea emitir

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fecha_ingreso** | **date** | Este dato se debe diligenciar solamente en el registro del mes en que el trabajador o aprendiz presenta ingreso o vinculación a la nómina del reportante. (en caso de tener mas de un ingreso en el mes, se debe reportar la primera fecha en la que se presenta esta novedad en el mes que se esta reportando). | 
**tiempo_laborado** | **float** | Cantidad de Tiempo en días que lleva laborando el Trabajador en la empresa | [optional] 
**fecha_retiro** | **date** | Este dato se debe diligenciar solamente en el registro del mes en que el trabajador o aprendiz presenta retiro de la nómina del reportante.(en caso de tener mas de un retiro en el mes, se debe reportar la ultima fecha en la que se presenta esta novedad en el mes que se esta reportando). | [optional] 
**fecha_liquidacion_inicio** | **date** | Fecha de inicio de Liquidación de Nómina | 
**fecha_liquidacion_fin** | **date** | Fecha fin de Liquidación de Nómina | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_periodo import CreatePayrollRequestGovernmentDataPeriodo

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataPeriodo from a JSON string
create_payroll_request_government_data_periodo_instance = CreatePayrollRequestGovernmentDataPeriodo.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataPeriodo.to_json())

# convert the object into a dict
create_payroll_request_government_data_periodo_dict = create_payroll_request_government_data_periodo_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataPeriodo from a dict
create_payroll_request_government_data_periodo_from_dict = CreatePayrollRequestGovernmentDataPeriodo.from_dict(create_payroll_request_government_data_periodo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


