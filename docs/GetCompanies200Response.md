# GetCompanies200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **float** |  | [optional] 
**companies** | [**List[GetCompanies200ResponseCompaniesInner]**](GetCompanies200ResponseCompaniesInner.md) | Array con empresas | [optional] 

## Example

```python
from openapi_client.models.get_companies200_response import GetCompanies200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanies200Response from a JSON string
get_companies200_response_instance = GetCompanies200Response.from_json(json)
# print the JSON string representation of the object
print(GetCompanies200Response.to_json())

# convert the object into a dict
get_companies200_response_dict = get_companies200_response_instance.to_dict()
# create an instance of GetCompanies200Response from a dict
get_companies200_response_from_dict = GetCompanies200Response.from_dict(get_companies200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


