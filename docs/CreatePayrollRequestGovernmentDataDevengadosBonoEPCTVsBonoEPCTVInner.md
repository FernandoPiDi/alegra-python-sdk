# CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVsBonoEPCTVInner

Objeto con información sobre devengados por concepto de Bonos Electronicos o de Papel de Servicio, Cheques, Tarjetas, Vales, etc

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pago_s** | **float** | Valor que el trabajador recibe como contraprestación por el trabajo realizado, por medio de bonos electrónicos, recargas, cheques, vales. es decir, todo pago realizado en un medio diferente a dinero en efectivo o consignación de cuenta bancaria (Salarial). | [optional] 
**pago_ns** | **float** | Valor que el trabajador recibe como concepto no salarial, por medio de bonos electrónicos, recargas, cheques, vales. es decir, todo pago realizado en un medio diferente a dinero en efectivo o consignación de cuenta bancaria (No Salarial). | [optional] 
**pago_alimentacion_s** | **float** | Valor que el trabajador recibe como concepto no salarial, por medio de bonos electrónicos, recargas, cheques, vales. es decir, todo pago realizado en un medio diferente a dinero en efectivo o consignación de cuenta bancaria (Para Alimentación Salarial). | [optional] 
**pago_alimentacion_ns** | **float** | Valor que el trabajador recibe como concepto no salarial, por medio de bonos electrónicos, recargas, cheques, vales. es decir, todo pago realizado en un medio diferente a dinero en efectivo o consignación de cuenta bancaria (Para Alimentación No Salarial). | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_bono_epctvs_bono_epctv_inner import CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVsBonoEPCTVInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVsBonoEPCTVInner from a JSON string
create_payroll_request_government_data_devengados_bono_epctvs_bono_epctv_inner_instance = CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVsBonoEPCTVInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVsBonoEPCTVInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_bono_epctvs_bono_epctv_inner_dict = create_payroll_request_government_data_devengados_bono_epctvs_bono_epctv_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVsBonoEPCTVInner from a dict
create_payroll_request_government_data_devengados_bono_epctvs_bono_epctv_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVsBonoEPCTVInner.from_dict(create_payroll_request_government_data_devengados_bono_epctvs_bono_epctv_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


