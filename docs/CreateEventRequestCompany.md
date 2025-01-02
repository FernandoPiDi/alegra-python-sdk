# CreateEventRequestCompany

Detalles de la organización que emite el evento, en caso de omitir este objeto se usará la compañia principal asociada al usuario

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id de la empresa | [optional] 
**organization_type** | **float** | Tipo de organización jurídica. Se debe colocar el código que corresponda de la tabla de tipos de organización jurídica de la DIAN. Persona Jurídica y asimiladas (1). Persona Natural y asimiladas (2) | [optional] 
**identification_type** | **str** | Tipo de documento de identificación del emisor. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN | [optional] 
**identification_number** | **str** | Número de identificación o NIT del emisor, sin guiones ni dv | [optional] 
**dv** | **str** | DV del NIT del emisor. Es obligatorio si identificationType &#x3D; 31 | [optional] 
**name** | **str** | Nombre o nombre comercial del emisor | [optional] 
**regime_code** | **str** | Régimen al que pertenece el Emisor. Gran contribuyente (O-13). Autorretenedor (O-15). Agente de retencion IVA (O-23). Régimen simple de tributación (O-47). No aplica - Otros (R-99-PN) | [optional] 
**tax_code** | **str** | Código tipo de impuesto según los códigos de la tabla de la DIAN. IVA (01). INC (04). IVA e INC (ZA). No aplica (ZZ) | [optional] 

## Example

```python
from openapi_client.models.create_event_request_company import CreateEventRequestCompany

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventRequestCompany from a JSON string
create_event_request_company_instance = CreateEventRequestCompany.from_json(json)
# print the JSON string representation of the object
print(CreateEventRequestCompany.to_json())

# convert the object into a dict
create_event_request_company_dict = create_event_request_company_instance.to_dict()
# create an instance of CreateEventRequestCompany from a dict
create_event_request_company_from_dict = CreateEventRequestCompany.from_dict(create_event_request_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


