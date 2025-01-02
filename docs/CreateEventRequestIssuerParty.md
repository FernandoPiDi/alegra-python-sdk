# CreateEventRequestIssuerParty

Informa quién recibió la factura electrónica o el bien y servicio. Solo es requerido en los eventos Recibo de Factura y Recibo de bienes y/o servicios

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identification_type** | **str** | Tipo de identificador fiscal | [optional] 
**dv** | **str** | Requerido si el tipo de identificador es 31 equivalente a NIT | [optional] 
**identification_number** | **str** | Número de identificación de la persona | [optional] 
**first_name** | **str** | Nombre de la persona que recibió la factura o los bienes y/o servicios | [optional] 
**family_name** | **str** | Apellido de la persona que recibió la factura o los bienes y/o servicios | [optional] 
**job_title** | **str** | Cargo de la persona que recibió la factura o los bienes y/o servicios | [optional] 
**organization_department** | **str** | Area, sección o departamento de la persona que recibió la factura o los bienes y/o servicios | [optional] 

## Example

```python
from openapi_client.models.create_event_request_issuer_party import CreateEventRequestIssuerParty

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventRequestIssuerParty from a JSON string
create_event_request_issuer_party_instance = CreateEventRequestIssuerParty.from_json(json)
# print the JSON string representation of the object
print(CreateEventRequestIssuerParty.to_json())

# convert the object into a dict
create_event_request_issuer_party_dict = create_event_request_issuer_party_instance.to_dict()
# create an instance of CreateEventRequestIssuerParty from a dict
create_event_request_issuer_party_from_dict = CreateEventRequestIssuerParty.from_dict(create_event_request_issuer_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


