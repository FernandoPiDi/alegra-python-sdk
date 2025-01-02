# GetSupportDocuments200ResponseSupportDocumentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id del documento soporte electrónico | [optional] 
**var_date** | **datetime** | Fecha de emisión del documento soporte electrónico | [optional] 
**status** | **str** | Estado del documento soporte electrónico | [optional] 
**legal_status** | **str** | Estado legal deL documento soporte electrónico ante la DIAN | [optional] 
**company_identification** | **str** | Identificación de la empresa empleadora | [optional] 
**supplier_identification** | **str** | Identificación del proveedor | [optional] 
**cuds** | **str** | Código único del documento soporte electrónico asignado para el documento | [optional] 
**prefix** | **str** | Prefijo del documento soporte electrónico | [optional] 
**number** | **float** | Número del documento soporte electrónico | [optional] 
**full_number** | **str** | Número del documento soporte electrónico (Incluye prefijo y número) | [optional] 
**xml** | **str** | Link de descarga a el XML que se envia a la DIAN. Este enlace solo dura por 60 minutos, para renovar el link solicite nuevamente el documento. | [optional] 
**application_response** | **str** | Link de descarga a el ApplicationResponse obetenido como respuesta de al DIAN al enviar el archivo XML. Este campo solo se añade al tener una respuesta de la DIAN. Este enlace solo dura por 60 minutos, para renovar el link solicite nuevamente el documento. | [optional] 
**government_response** | [**GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse**](GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse.md) |  | [optional] 
**xml_file_name** | **str** | Nombre del archivo XML que se envió a la DIAN | [optional] 
**zip_file_name** | **str** | Nombre del archivo Zip que se envió a la DIAN | [optional] 
**errors** | [**List[CreateEquivalentDocumentPos200ResponseEquivalentDocumentErrorsInner]**](CreateEquivalentDocumentPos200ResponseEquivalentDocumentErrorsInner.md) | Array con mensajes de error generados en el sistema | [optional] 

## Example

```python
from openapi_client.models.get_support_documents200_response_support_documents_inner import GetSupportDocuments200ResponseSupportDocumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSupportDocuments200ResponseSupportDocumentsInner from a JSON string
get_support_documents200_response_support_documents_inner_instance = GetSupportDocuments200ResponseSupportDocumentsInner.from_json(json)
# print the JSON string representation of the object
print(GetSupportDocuments200ResponseSupportDocumentsInner.to_json())

# convert the object into a dict
get_support_documents200_response_support_documents_inner_dict = get_support_documents200_response_support_documents_inner_instance.to_dict()
# create an instance of GetSupportDocuments200ResponseSupportDocumentsInner from a dict
get_support_documents200_response_support_documents_inner_from_dict = GetSupportDocuments200ResponseSupportDocumentsInner.from_dict(get_support_documents200_response_support_documents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


