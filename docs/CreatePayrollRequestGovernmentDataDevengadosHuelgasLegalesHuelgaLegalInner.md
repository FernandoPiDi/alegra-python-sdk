# CreatePayrollRequestGovernmentDataDevengadosHuelgasLegalesHuelgaLegalInner

Objeto con información sobre devengados por concepto de huelga legal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fecha_inicio** | **date** | Este dato se debe diligenciar solamente en el registro del mes en que el trabajador inicia la huelga legalmente declarada. | [optional] 
**fecha_fin** | **date** | Este dato se debe diligenciar solamente en el registro del mes en que el trabajador termina la huelga legalmente declarada. | [optional] 
**cantidad** | **float** | Número de días en los que el trabajador estuvo inactivo por huelga legalmente declarada. | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_huelgas_legales_huelga_legal_inner import CreatePayrollRequestGovernmentDataDevengadosHuelgasLegalesHuelgaLegalInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHuelgasLegalesHuelgaLegalInner from a JSON string
create_payroll_request_government_data_devengados_huelgas_legales_huelga_legal_inner_instance = CreatePayrollRequestGovernmentDataDevengadosHuelgasLegalesHuelgaLegalInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosHuelgasLegalesHuelgaLegalInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_huelgas_legales_huelga_legal_inner_dict = create_payroll_request_government_data_devengados_huelgas_legales_huelga_legal_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosHuelgasLegalesHuelgaLegalInner from a dict
create_payroll_request_government_data_devengados_huelgas_legales_huelga_legal_inner_from_dict = CreatePayrollRequestGovernmentDataDevengadosHuelgasLegalesHuelgaLegalInner.from_dict(create_payroll_request_government_data_devengados_huelgas_legales_huelga_legal_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


