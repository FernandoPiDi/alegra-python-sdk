# CreateEventFromXmlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Número del evento que se emite, el valor es alfanumérico y único por evento dentro de la misma compañía | 
**type** | **str** | Código relacionado al tipo de evento que se quiere emitir. Recibo de Factura (030). Reclamo de la Factura Electrónica de Venta (031). Recibo Bienes y Servicios (032). Aceptación Expresa (033). Aceptación Tácita (034) | 
**xml_content** | **str** | Contenido en bas64 del XML AttachedDocument de la factura electrónica | 
**company** | [**CreateEventFromXmlRequestCompany**](CreateEventFromXmlRequestCompany.md) |  | [optional] 
**issuer_party** | [**CreateEventRequestIssuerParty**](CreateEventRequestIssuerParty.md) |  | [optional] 
**claim_code** | **str** | Código del motivo de rechazo según la tabla DIAN. Documento con inconsistencias (01). Mercancía no entregada totalmente (02). Mercancía no entregada parcialmente (03). Servicio no prestado (04). Campo requerido únicamente en los eventos de rechazo de factura o documento electrónico | [optional] 
**email** | [**CreateEventRequestEmail**](CreateEventRequestEmail.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_event_from_xml_request import CreateEventFromXmlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventFromXmlRequest from a JSON string
create_event_from_xml_request_instance = CreateEventFromXmlRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEventFromXmlRequest.to_json())

# convert the object into a dict
create_event_from_xml_request_dict = create_event_from_xml_request_instance.to_dict()
# create an instance of CreateEventFromXmlRequest from a dict
create_event_from_xml_request_from_dict = CreateEventFromXmlRequest.from_dict(create_event_from_xml_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


