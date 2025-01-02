# CreatePayrollRequestGovernmentDataDevengados

Objeto con la información de los devengados del documento

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basico** | [**CreatePayrollRequestGovernmentDataDevengadosBasico**](CreatePayrollRequestGovernmentDataDevengadosBasico.md) |  | 
**transporte** | [**List[CreatePayrollRequestGovernmentDataDevengadosTransporteInner]**](CreatePayrollRequestGovernmentDataDevengadosTransporteInner.md) | Array con información sobre devengados por concepto de transporte | [optional] 
**heds** | [**CreatePayrollRequestGovernmentDataDevengadosHEDs**](CreatePayrollRequestGovernmentDataDevengadosHEDs.md) |  | [optional] 
**hens** | [**CreatePayrollRequestGovernmentDataDevengadosHENs**](CreatePayrollRequestGovernmentDataDevengadosHENs.md) |  | [optional] 
**hrns** | [**CreatePayrollRequestGovernmentDataDevengadosHRNs**](CreatePayrollRequestGovernmentDataDevengadosHRNs.md) |  | [optional] 
**heddfs** | [**CreatePayrollRequestGovernmentDataDevengadosHEDDFs**](CreatePayrollRequestGovernmentDataDevengadosHEDDFs.md) |  | [optional] 
**hrddfs** | [**CreatePayrollRequestGovernmentDataDevengadosHRDDFs**](CreatePayrollRequestGovernmentDataDevengadosHRDDFs.md) |  | [optional] 
**hendfs** | [**CreatePayrollRequestGovernmentDataDevengadosHENDFs**](CreatePayrollRequestGovernmentDataDevengadosHENDFs.md) |  | [optional] 
**hrndfs** | [**CreatePayrollRequestGovernmentDataDevengadosHRNDFs**](CreatePayrollRequestGovernmentDataDevengadosHRNDFs.md) |  | [optional] 
**vacaciones** | [**CreatePayrollRequestGovernmentDataDevengadosVacaciones**](CreatePayrollRequestGovernmentDataDevengadosVacaciones.md) |  | [optional] 
**primas** | [**CreatePayrollRequestGovernmentDataDevengadosPrimas**](CreatePayrollRequestGovernmentDataDevengadosPrimas.md) |  | [optional] 
**cesantias** | [**CreatePayrollRequestGovernmentDataDevengadosCesantias**](CreatePayrollRequestGovernmentDataDevengadosCesantias.md) |  | [optional] 
**incapacidades** | [**CreatePayrollRequestGovernmentDataDevengadosIncapacidades**](CreatePayrollRequestGovernmentDataDevengadosIncapacidades.md) |  | [optional] 
**licencias** | [**CreatePayrollRequestGovernmentDataDevengadosLicencias**](CreatePayrollRequestGovernmentDataDevengadosLicencias.md) |  | [optional] 
**bonificaciones** | [**CreatePayrollRequestGovernmentDataDevengadosBonificaciones**](CreatePayrollRequestGovernmentDataDevengadosBonificaciones.md) |  | [optional] 
**auxilios** | [**CreatePayrollRequestGovernmentDataDevengadosAuxilios**](CreatePayrollRequestGovernmentDataDevengadosAuxilios.md) |  | [optional] 
**huelgas_legales** | [**CreatePayrollRequestGovernmentDataDevengadosHuelgasLegales**](CreatePayrollRequestGovernmentDataDevengadosHuelgasLegales.md) |  | [optional] 
**otros_conceptos** | [**CreatePayrollRequestGovernmentDataDevengadosOtrosConceptos**](CreatePayrollRequestGovernmentDataDevengadosOtrosConceptos.md) |  | [optional] 
**compensaciones** | [**CreatePayrollRequestGovernmentDataDevengadosCompensaciones**](CreatePayrollRequestGovernmentDataDevengadosCompensaciones.md) |  | [optional] 
**bono_epctvs** | [**CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVs**](CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVs.md) |  | [optional] 
**comisiones** | [**CreatePayrollRequestGovernmentDataDevengadosComisiones**](CreatePayrollRequestGovernmentDataDevengadosComisiones.md) |  | [optional] 
**pagos_terceros** | [**CreatePayrollRequestGovernmentDataDevengadosPagosTerceros**](CreatePayrollRequestGovernmentDataDevengadosPagosTerceros.md) |  | [optional] 
**anticipos** | [**CreatePayrollRequestGovernmentDataDevengadosAnticipos**](CreatePayrollRequestGovernmentDataDevengadosAnticipos.md) |  | [optional] 
**dotacion** | **float** | De conformidad con lo previsto en el artículo 230 del Código Sustantivo del Trabajo, o la norma que lo modifique, adicione o sustituya, corresponde al valor que el empleador dispone para suministrar la dotación de sus trabajadores. | [optional] 
**apoyo_sost** | **float** | Corresponde al valor no salarial que el patrocinador paga de forma mensual como ayuda o apoyo economía al aprendiz o practicante universitario durante su etapa lectiva y fase practica. | [optional] 
**teletrabajo** | **float** | Valor que debe ser pagado al trabajador cuyo contrato indica expresamente que puede laborar mediante teletrabajo | [optional] 
**bonif_retiro** | **float** | Valor establecido por mutuo acuerdo por retiro del Trabajador | [optional] 
**indemnizacion** | **float** | Valor de Indemnizacion establecido por ley | [optional] 
**reintegro** | **float** | Valor que le regresa la empresa al trabajador por una deducción mal realizada en otro pago de nomina | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados import CreatePayrollRequestGovernmentDataDevengados

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengados from a JSON string
create_payroll_request_government_data_devengados_instance = CreatePayrollRequestGovernmentDataDevengados.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengados.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_dict = create_payroll_request_government_data_devengados_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengados from a dict
create_payroll_request_government_data_devengados_from_dict = CreatePayrollRequestGovernmentDataDevengados.from_dict(create_payroll_request_government_data_devengados_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


