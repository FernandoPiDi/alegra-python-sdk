# CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVs

Objeto con la información devengada por concepto de Bonos Electronicos o de Papel de Servicio, Cheques, Tarjetas, Vales, etc

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bono_epctv** | [**List[CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVsBonoEPCTVInner]**](CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVsBonoEPCTVInner.md) | Array con información sobre devengados por concepto de Bonos Electronicos o de Papel de Servicio, Cheques, Tarjetas, Vales, etc | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_devengados_bono_epctvs import CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVs

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVs from a JSON string
create_payroll_request_government_data_devengados_bono_epctvs_instance = CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVs.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVs.to_json())

# convert the object into a dict
create_payroll_request_government_data_devengados_bono_epctvs_dict = create_payroll_request_government_data_devengados_bono_epctvs_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVs from a dict
create_payroll_request_government_data_devengados_bono_epctvs_from_dict = CreatePayrollRequestGovernmentDataDevengadosBonoEPCTVs.from_dict(create_payroll_request_government_data_devengados_bono_epctvs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


