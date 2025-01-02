# CreatePayrollRequestGovernmentDataDeduccionesSancionesSancionInner

Objeto con información sobre deducción por concepto de sanción

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sancion_public** | **float** | Valor por el del incumplimiento de una regla o norma de conducta obligatoria (Publica) | 
**sancion_priv** | **float** | Valor por el del incumplimiento de una regla o norma de conducta obligatoria (Privada o Ordinaria) | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_deducciones_sanciones_sancion_inner import CreatePayrollRequestGovernmentDataDeduccionesSancionesSancionInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesSancionesSancionInner from a JSON string
create_payroll_request_government_data_deducciones_sanciones_sancion_inner_instance = CreatePayrollRequestGovernmentDataDeduccionesSancionesSancionInner.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDeduccionesSancionesSancionInner.to_json())

# convert the object into a dict
create_payroll_request_government_data_deducciones_sanciones_sancion_inner_dict = create_payroll_request_government_data_deducciones_sanciones_sancion_inner_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDeduccionesSancionesSancionInner from a dict
create_payroll_request_government_data_deducciones_sanciones_sancion_inner_from_dict = CreatePayrollRequestGovernmentDataDeduccionesSancionesSancionInner.from_dict(create_payroll_request_government_data_deducciones_sanciones_sancion_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


