# CreatePayrollRequestGovernmentDataDevengadosOtrosConceptosOtroConceptoInner

Objeto con información sobre devengados por otro concepto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descripcion_concepto** | **str** | Nombre del Concepto que corresponde a los demás pagos fijos o variables realizados al trabajador que remuneren en dinero o en especie como contraprestación directa del servicio, sea cualquiera la forma o denominación que se adopte. | 
**concepto_s** | **float** | Valor de los demás pagos fijos o variables realizados al trabajador que remuneren en dinero o en especie como contraprestación directa del servicio, sea cualquiera la forma o denominación que se adopte (Salarial). | [optional] 
**concepto_ns** | **float** | Valor de los demás pagos que ocasionalmente y por mera liberalidad recibe el trabajador del empleador, en dinero o en especie no para su beneficio, ni para enriquecer su patrimonio, sino para desempeñar a cabalidad sus funciones (No Salarial). | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_otros_conceptos_otro_concepto_inner import CreatePayrollRequestGovernmentDataDevengadosOtrosConceptosOtroConceptoInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosOtrosConceptosOtroConceptoInner from a JSON string
create_payroll_request_government_data_devengados_otros_conceptos_otro_concepto_inner_instance = CreatePayrollRequestGovernmentDataDevengadosOtrosConceptosOtroConceptoInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosOtrosConceptosOtroConceptoInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_otros_conceptos_otro_concepto_inner_dict = create_payroll_request_government_data_devengados_otros_conceptos_otro_concepto_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosOtrosConceptosOtroConceptoInner from a dict
create_payroll_request_government_data_devengados_otros_conceptos_otro_concepto_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosOtrosConceptosOtroConceptoInner.from_dict(create_payroll_request_government_data_devengados_otros_conceptos_otro_concepto_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


