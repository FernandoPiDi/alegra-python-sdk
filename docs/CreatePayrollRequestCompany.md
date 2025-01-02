# CreatePayrollRequestCompany

Objeto con información de la empresa con la que se desea emitir la nómina electrónica. Este atributo es opcional, sino se envia este objeto, Alegra tomará la compañía asociada al token de autenticación

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id de la empresa | 

## Example

```python
from openapi_client.models.create_payroll_request_company import CreatePayrollRequestCompany

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestCompany from a JSON string
create_payroll_request_company_instance = CreatePayrollRequestCompany.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestCompany.to_json())

# convert the object into a dict
create_payroll_request_company_dict = create_payroll_request_company_instance.to_dict()
# create an instance of CreatePayrollRequestCompany from a dict
create_payroll_request_company_from_dict = CreatePayrollRequestCompany.from_dict(create_payroll_request_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


