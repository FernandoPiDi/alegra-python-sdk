# CreatePayrollRequestGovernmentData

Objeto que contiene la información de la nómina electrónica en formato JSON según el estándar de la DIAN

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**novedad** | [**CreatePayrollRequestGovernmentDataNovedad**](CreatePayrollRequestGovernmentDataNovedad.md) |  | [optional] 
**periodo** | [**CreatePayrollRequestGovernmentDataPeriodo**](CreatePayrollRequestGovernmentDataPeriodo.md) |  | 
**lugar_generacion_xml** | [**CreatePayrollRequestGovernmentDataLugarGeneracionXML**](CreatePayrollRequestGovernmentDataLugarGeneracionXML.md) |  | 
**informacion_general** | [**CreatePayrollRequestGovernmentDataInformacionGeneral**](CreatePayrollRequestGovernmentDataInformacionGeneral.md) |  | 
**empleador** | [**CreatePayrollRequestGovernmentDataEmpleador**](CreatePayrollRequestGovernmentDataEmpleador.md) |  | 
**trabajador** | [**CreatePayrollRequestGovernmentDataTrabajador**](CreatePayrollRequestGovernmentDataTrabajador.md) |  | 
**pago** | [**CreatePayrollRequestGovernmentDataPago**](CreatePayrollRequestGovernmentDataPago.md) |  | 
**fechas_pagos** | [**CreatePayrollRequestGovernmentDataFechasPagos**](CreatePayrollRequestGovernmentDataFechasPagos.md) |  | 
**devengados** | [**CreatePayrollRequestGovernmentDataDevengados**](CreatePayrollRequestGovernmentDataDevengados.md) |  | 
**deducciones** | [**CreatePayrollRequestGovernmentDataDeducciones**](CreatePayrollRequestGovernmentDataDeducciones.md) |  | 
**redondeo** | **float** | Se utiliza para cuando se utilice el Redondeo en el Documento, Definido en el numeral 1.1.1 | [optional] 
**devengados_total** | **float** | Valor total de la Suma de todos los Devengados del Documento | 
**deducciones_total** | **float** | Valor total de la Suma de todas las Deducciones del Documento | 
**comprobante_total** | **float** | Debe ir el total de: Devengados - Deducciones | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data import CreatePayrollRequestGovernmentData

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentData from a JSON string
create_payroll_request_government_data_instance = CreatePayrollRequestGovernmentData.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentData.to_json())

# convert the object into a dict
create_payroll_request_government_data_dict = create_payroll_request_government_data_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentData from a dict
create_payroll_request_government_data_from_dict = CreatePayrollRequestGovernmentData.from_dict(create_payroll_request_government_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


