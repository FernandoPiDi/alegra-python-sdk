# CreatePayrollRequestGovernmentDataDeducciones

Objeto con la información de las deducciones del documento

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**salud** | [**CreatePayrollRequestGovernmentDataDeduccionesSalud**](CreatePayrollRequestGovernmentDataDeduccionesSalud.md) |  | 
**fondo_pension** | [**CreatePayrollRequestGovernmentDataDeduccionesFondoPension**](CreatePayrollRequestGovernmentDataDeduccionesFondoPension.md) |  | 
**fondo_sp** | [**CreatePayrollRequestGovernmentDataDeduccionesFondoSP**](CreatePayrollRequestGovernmentDataDeduccionesFondoSP.md) |  | [optional] 
**sindicatos** | [**CreatePayrollRequestGovernmentDataDeduccionesSindicatos**](CreatePayrollRequestGovernmentDataDeduccionesSindicatos.md) |  | [optional] 
**sanciones** | [**CreatePayrollRequestGovernmentDataDeduccionesSanciones**](CreatePayrollRequestGovernmentDataDeduccionesSanciones.md) |  | [optional] 
**libranzas** | [**CreatePayrollRequestGovernmentDataDeduccionesLibranzas**](CreatePayrollRequestGovernmentDataDeduccionesLibranzas.md) |  | [optional] 
**pagos_terceros** | [**CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros**](CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros.md) |  | [optional] 
**anticipos** | [**CreatePayrollRequestGovernmentDataDeduccionesAnticipos**](CreatePayrollRequestGovernmentDataDeduccionesAnticipos.md) |  | [optional] 
**otras_deducciones** | [**CreatePayrollRequestGovernmentDataDeduccionesOtrasDeducciones**](CreatePayrollRequestGovernmentDataDeduccionesOtrasDeducciones.md) |  | [optional] 
**pension_voluntaria** | **float** | Valor correspondiente al ahorro que hace el trabajador para complementar su pension obligatoria o cumplir metas especificas. | [optional] 
**retencion_fuente** | **float** | Si hubiere lugar, la empresa deberá calcular y retener al empleado el valor correspondiente a retención en la fuente por ingresos laborales. Este valor será declarado y consignado en la respectiva declaración mensual de retención en la fuente. | [optional] 
**afc** | **float** | Corresponde a (Ahorro Fomento a la contruccion) | [optional] 
**cooperativa** | **float** | Las cuotas o aportes que los empleados hagan a las cooperativas legalmente constituidas | [optional] 
**embargo_fiscal** | **float** | Los embargos ordenados por autoridad judicial competente contra los empleados deben ser descontados de la nómina por la empresa y consignarlos en la cuenta que el juez haya ordenado. | [optional] 
**plan_complementarios** | **float** | Valor de planes complementarios de salud al que el trabajador se encuentran afiliado, siempre que medie autorización del empleado. | [optional] 
**educacion** | **float** | Valor de servicios educativos que el trabajador autorice descuento. | [optional] 
**reintegro** | **float** | Valor que le regresa el trabajador a la empresa por un devengo mal realizado en otro pago de nómina | [optional] 
**deuda** | **float** | Valor que se deba pagar por las obligaciones que el empleado tenga con su empresa, como puede ser un crédito que ésta le haya otorgado, o como compensación por algún perjuicio o detrimento económico que el empleado le haya causado a la empresa. | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_deducciones import CreatePayrollRequestGovernmentDataDeducciones

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDeducciones from a JSON string
create_payroll_request_government_data_deducciones_instance = CreatePayrollRequestGovernmentDataDeducciones.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDeducciones.to_json())

# convert the object into a dict
create_payroll_request_government_data_deducciones_dict = create_payroll_request_government_data_deducciones_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDeducciones from a dict
create_payroll_request_government_data_deducciones_from_dict = CreatePayrollRequestGovernmentDataDeducciones.from_dict(create_payroll_request_government_data_deducciones_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


