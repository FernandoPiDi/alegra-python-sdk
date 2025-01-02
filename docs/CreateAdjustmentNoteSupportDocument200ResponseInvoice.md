# CreateAdjustmentNoteSupportDocument200ResponseInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id de la nota de ajuste al documento soporte electrónico | [optional] 
**invoice_document_reference** | **str** | Identificador unico del documento de soporte afectado por la nota de ajuste | [optional] 
**var_date** | **datetime** | Fecha de emisión de una una nota de ajuste al documento soporte electrónico | [optional] 
**status** | **str** | Estado de una una nota de ajuste al documento soporte electrónico | [optional] 
**legal_status** | **str** | Estado legal del documento soporte electrónico ante la DIAN | [optional] 
**company_identification** | **str** | Identificación de la empresa empleadora | [optional] 
**supplier_identification** | **str** | Identificación del proveedor | [optional] 
**cuds** | **str** | Código único de la una nota de ajuste al documento soporte electrónico asignado para el documento | [optional] 
**prefix** | **str** | Prefijo de la una nota de ajuste al documento soporte electrónico | [optional] 
**number** | **float** | Número de la una nota de ajuste al documento soporte electrónico | [optional] 
**full_number** | **str** | Número de la una nota de ajuste al documento soporte electrónico (Incluye prefijo y número) | [optional] 
**government_response** | [**GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse**](GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse.md) |  | [optional] 
**xml_file_name** | **str** | Nombre del archivo XML que se envió a la DIAN | [optional] 
**zip_file_name** | **str** | Nombre del archivo Zip que se envió a la DIAN | [optional] 
**xml** | **str** | Link de descarga a el XML que se envia a la DIAN. Este enlace solo dura por 60 minutos, para renovar el link solicite nuevamente el documento. | [optional] 
**application_response** | **str** | Link de descarga a el ApplicationResponse obetenido como respuesta de al DIAN al enviar el archivo XML. Este campo solo se añade al tener una respuesta de la DIAN. Este enlace solo dura por 60 minutos, para renovar el link solicite nuevamente el documento. | [optional] 
**errors** | [**List[CreateEquivalentDocumentPos200ResponseEquivalentDocumentErrorsInner]**](CreateEquivalentDocumentPos200ResponseEquivalentDocumentErrorsInner.md) | Array con mensajes de error generados en el sistema | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_support_document200_response_invoice import CreateAdjustmentNoteSupportDocument200ResponseInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteSupportDocument200ResponseInvoice from a JSON string
create_adjustment_note_support_document200_response_invoice_instance = CreateAdjustmentNoteSupportDocument200ResponseInvoice.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteSupportDocument200ResponseInvoice.to_json())

# convert the object into a dict
create_adjustment_note_support_document200_response_invoice_dict = create_adjustment_note_support_document200_response_invoice_instance.to_dict()
# create an instance of CreateAdjustmentNoteSupportDocument200ResponseInvoice from a dict
create_adjustment_note_support_document200_response_invoice_from_dict = CreateAdjustmentNoteSupportDocument200ResponseInvoice.from_dict(create_adjustment_note_support_document200_response_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


