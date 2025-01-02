# CreatePayrollRequestGovernmentDataLugarGeneracionXML

Objeto con la información del lugar de generación del documento

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pais** | **str** | Codigo del país donde se genera el documento. Se debe colocar el Codigo que corresponda de la tabla de países de la DIAN | [optional] 
**municipio_ciudad** | **str** | Código del municipio o ciudad donde se genera el documento. Se debe colocar el Codigo que corresponda de la tabla de municipios de la DIAN | 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_lugar_generacion_xml import CreatePayrollRequestGovernmentDataLugarGeneracionXML

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataLugarGeneracionXML from a JSON string
create_payroll_request_government_data_lugar_generacion_xml_instance = CreatePayrollRequestGovernmentDataLugarGeneracionXML.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataLugarGeneracionXML.to_json())

# convert the object into a dict
create_payroll_request_government_data_lugar_generacion_xml_dict = create_payroll_request_government_data_lugar_generacion_xml_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataLugarGeneracionXML from a dict
create_payroll_request_government_data_lugar_generacion_xml_from_dict = CreatePayrollRequestGovernmentDataLugarGeneracionXML.from_dict(create_payroll_request_government_data_lugar_generacion_xml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


