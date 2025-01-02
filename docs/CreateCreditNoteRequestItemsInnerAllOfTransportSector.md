# CreateCreditNoteRequestItemsInnerAllOfTransportSector

Objeto que contiene los campos adicionales que hacen referencia al sector transporte de carga. Aplica solo para facturas de transporte, y se debe informar a nivel de ítem.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_registered_in_rndc** | **bool** | True si el Bien o Servicio “B/S” reportado corresponde o no a una línea registrada en el RNDC.&lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;@schemeID&amp;gt;&lt;/i&gt; | [optional] 
**number_rndc** | **float** | Número Radicado de Aceptación de la Remesa. Hace referencia al consecutivo único nacional que controla y entrega el RNDC. | [optional] 
**number_remesa** | **str** | Número de Remesa. Hace referencia al número del consecutivo de la Remesa según codificación interna de cada empresa de transporte. | [optional] 
**freight_amount** | **float** | Valor del flete a cobrar por el servicio de transporte de la remesa. | [optional] 
**quantity_transported** | **float** | Cantidad transportada. | [optional] 
**unit_code** | **str** | Unidad de medida. Se utilizará alguna de las dos codificaciones permitidas por el estándar. KGM: Kilogramos y GLL: Galones. | [optional] 

## Example

```python
from openapi_client.models.create_credit_note_request_items_inner_all_of_transport_sector import CreateCreditNoteRequestItemsInnerAllOfTransportSector

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCreditNoteRequestItemsInnerAllOfTransportSector from a JSON string
create_credit_note_request_items_inner_all_of_transport_sector_instance = CreateCreditNoteRequestItemsInnerAllOfTransportSector.from_json(json)
# print the JSON string representation of the object
print(CreateCreditNoteRequestItemsInnerAllOfTransportSector.to_json())

# convert the object into a dict
create_credit_note_request_items_inner_all_of_transport_sector_dict = create_credit_note_request_items_inner_all_of_transport_sector_instance.to_dict()
# create an instance of CreateCreditNoteRequestItemsInnerAllOfTransportSector from a dict
create_credit_note_request_items_inner_all_of_transport_sector_from_dict = CreateCreditNoteRequestItemsInnerAllOfTransportSector.from_dict(create_credit_note_request_items_inner_all_of_transport_sector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


