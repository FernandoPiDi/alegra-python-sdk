# CreateEvent200ResponseEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id del evento emitido | [optional] 
**type** | [**CreateEvent200ResponseEventType**](CreateEvent200ResponseEventType.md) |  | [optional] 
**var_date** | **datetime** | Fecha de emisión del evento | [optional] 
**legal_status** | **str** | Estado legal del evento ante la DIAN | [optional] 
**company_identification** | **float** | Identificación del emisor del evento | [optional] 
**cude** | **str** | del documento electrónico del evento | [optional] 
**associated_document_id** | **str** | Código único de la factura electrónica asociada al evento | [optional] 
**receiver** | [**CreateEvent200ResponseEventReceiver**](CreateEvent200ResponseEventReceiver.md) |  | [optional] 
**prefix** | **str** | Prefijo del evento electrónico | [optional] 
**number** | **float** | Número de evento electronico | [optional] 
**full_number** | **str** | Número de nota débito electrónica (Incluye prefijo y número) | [optional] 
**government_response** | [**GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse**](GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse.md) |  | [optional] 
**xml_file_name** | **str** | Nombre del archivo XML que se envió a la DIAN | [optional] 
**zip_file_name** | **str** | Nombre del archivo Zip que se envió a la DIAN | [optional] 
**status** | **str** | Estado del evento electrónico | [optional] 

## Example

```python
from openapi_client.models.create_event200_response_event import CreateEvent200ResponseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEvent200ResponseEvent from a JSON string
create_event200_response_event_instance = CreateEvent200ResponseEvent.from_json(json)
# print the JSON string representation of the object
print(CreateEvent200ResponseEvent.to_json())

# convert the object into a dict
create_event200_response_event_dict = create_event200_response_event_instance.to_dict()
# create an instance of CreateEvent200ResponseEvent from a dict
create_event200_response_event_from_dict = CreateEvent200ResponseEvent.from_dict(create_event200_response_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


