# GetPayrolls200ResponseMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Id del objeto a partir del cuál se inicia la consulta | [optional] 
**to** | **str** | Id del último objeto consultado | [optional] 
**results_count** | **int** | Cantidad de resultados retornados en la respuesta | [optional] 

## Example

```python
from openapi_client.models.get_payrolls200_response_metadata import GetPayrolls200ResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayrolls200ResponseMetadata from a JSON string
get_payrolls200_response_metadata_instance = GetPayrolls200ResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(GetPayrolls200ResponseMetadata.to_json())

# convert the object into a dict
get_payrolls200_response_metadata_dict = get_payrolls200_response_metadata_instance.to_dict()
# create an instance of GetPayrolls200ResponseMetadata from a dict
get_payrolls200_response_metadata_from_dict = GetPayrolls200ResponseMetadata.from_dict(get_payrolls200_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


