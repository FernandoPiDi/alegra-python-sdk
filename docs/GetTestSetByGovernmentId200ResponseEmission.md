# GetTestSetByGovernmentId200ResponseEmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id de nómina electrónica | [optional] 
**var_date** | **datetime** | Fecha de emisión de nómina electrónica | [optional] 
**status** | **str** | Estado de la nómina electrónica | [optional] 
**legal_status** | **str** | Estado legal de la nómina electrónica ante la DIAN | [optional] 
**company_identification** | **str** | Identificación de la empresa empleadora | [optional] 
**employee_identification** | **str** | Identificación del empleado | [optional] 
**cune** | **str** | Código único de nómina electrónica asignado para el documento | [optional] 
**prefix** | **str** | Prefijo de nómina electrónica | [optional] 
**number** | **float** | Número de nómina electrónica | [optional] 
**full_number** | **str** | Número de nómina electrónica (Incluye prefijo y número) | [optional] 
**government_response** | [**GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse**](GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse.md) |  | [optional] 
**xml_file_name** | **str** | Nombre del archivo XML que se envió a la DIAN | [optional] 
**zip_file_name** | **str** | Nombre del archivo Zip que se envió a la DIAN | [optional] 

## Example

```python
from openapi_client.models.get_test_set_by_government_id200_response_emission import GetTestSetByGovernmentId200ResponseEmission

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestSetByGovernmentId200ResponseEmission from a JSON string
get_test_set_by_government_id200_response_emission_instance = GetTestSetByGovernmentId200ResponseEmission.from_json(json)
# print the JSON string representation of the object
print(GetTestSetByGovernmentId200ResponseEmission.to_json())

# convert the object into a dict
get_test_set_by_government_id200_response_emission_dict = get_test_set_by_government_id200_response_emission_instance.to_dict()
# create an instance of GetTestSetByGovernmentId200ResponseEmission from a dict
get_test_set_by_government_id200_response_emission_from_dict = GetTestSetByGovernmentId200ResponseEmission.from_dict(get_test_set_by_government_id200_response_emission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


