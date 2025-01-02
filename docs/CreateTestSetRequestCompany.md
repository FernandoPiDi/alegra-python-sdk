# CreateTestSetRequestCompany

Objeto con información de la empresa con la que se desea crear el set de pruebas. Este atributo es opcional, sino se envia este objeto, Alegra tomará la compañía asociada al token de autenticación

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id de la empresa | 

## Example

```python
from openapi_client.models.create_test_set_request_company import CreateTestSetRequestCompany

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTestSetRequestCompany from a JSON string
create_test_set_request_company_instance = CreateTestSetRequestCompany.from_json(json)
# print the JSON string representation of the object
print(CreateTestSetRequestCompany.to_json())

# convert the object into a dict
create_test_set_request_company_dict = create_test_set_request_company_instance.to_dict()
# create an instance of CreateTestSetRequestCompany from a dict
create_test_set_request_company_from_dict = CreateTestSetRequestCompany.from_dict(create_test_set_request_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


