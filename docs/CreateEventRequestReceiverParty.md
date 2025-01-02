# CreateEventRequestReceiverParty

Persona o entidad que recibe el evento, necesaria en todos los eventos a excepción de Aceptación Tácita (034)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre o razón social del receptor | 
**organization_type** | **float** | Tipo de organización jurídica. Se debe colocar el Código que corresponda de la tabla de tipos de organización jurídica de la DIAN. Persona Jurídica y asimiladas (1). Persona Natural y asimiladas (2) | 
**identification_number** | **str** | Número de identificación o NIT del receptor, sin guiones ni DV | 
**identification_type** | **str** | Tipo de documento de identificación del receptor. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN | 
**dv** | **str** | DV del NIT del receptor. Es obligatorio si idNumberType &#x3D; 31 | [optional] 
**regime_code** | **str** | Régimen al que pertenece el Emisor. Gran contribuyente (O-13). Autorretenedor (O-15). Agente de retencion IVA (O-23). Régimen simple de tributación (O-47). No aplica - Otros (R-99-PN) | [optional] 
**tax_code** | **str** | Código tipo de impuesto según los códigos de la tabla de la DIAN. IVA (01). INC (04). IVA e INC (ZA). No aplica (ZZ) | [optional] 

## Example

```python
from openapi_client.models.create_event_request_receiver_party import CreateEventRequestReceiverParty

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventRequestReceiverParty from a JSON string
create_event_request_receiver_party_instance = CreateEventRequestReceiverParty.from_json(json)
# print the JSON string representation of the object
print(CreateEventRequestReceiverParty.to_json())

# convert the object into a dict
create_event_request_receiver_party_dict = create_event_request_receiver_party_instance.to_dict()
# create an instance of CreateEventRequestReceiverParty from a dict
create_event_request_receiver_party_from_dict = CreateEventRequestReceiverParty.from_dict(create_event_request_receiver_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


