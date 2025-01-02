# CreateEquivalentDocumentPos200ResponseEquivalentDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id del documento equivalente electrónico | [optional] 
**var_date** | **datetime** | Fecha de emisión del documento equivalente electrónico | [optional] 
**status** | **str** | Estado del documento equivalente electrónico | [optional] 
**legal_status** | **str** | Estado legal del documento equivalente electrónico ante la DIAN | [optional] 
**company_identification** | **str** | Identificación de la empresa emisora | [optional] 
**cude** | **str** | Código único de documento equivalente electrónico asignado para el documento | [optional] 
**prefix** | **str** | Prefijo de documento equivalente electrónico | [optional] 
**number** | **float** | Número de documento equivalente electrónico | [optional] 
**full_number** | **str** | Número de documento equivalente electrónico (Incluye prefijo y número) | [optional] 
**government_response** | [**GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse**](GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse.md) |  | [optional] 
**xml_file_name** | **str** | Nombre del archivo XML que se envió a la DIAN | [optional] 
**zip_file_name** | **str** | Nombre del archivo Zip que se envió a la DIAN | [optional] 
**qr_code_content** | **str** | Contenido para la construcción del Código QR | [optional] 
**errors** | [**List[CreateEquivalentDocumentPos200ResponseEquivalentDocumentErrorsInner]**](CreateEquivalentDocumentPos200ResponseEquivalentDocumentErrorsInner.md) | Array con mensajes de error generados en el sistema | [optional] 

## Example

```python
from openapi_client.models.create_equivalent_document_pos200_response_equivalent_document import CreateEquivalentDocumentPos200ResponseEquivalentDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEquivalentDocumentPos200ResponseEquivalentDocument from a JSON string
create_equivalent_document_pos200_response_equivalent_document_instance = CreateEquivalentDocumentPos200ResponseEquivalentDocument.from_json(json)
# print the JSON string representation of the object
print(CreateEquivalentDocumentPos200ResponseEquivalentDocument.to_json())

# convert the object into a dict
create_equivalent_document_pos200_response_equivalent_document_dict = create_equivalent_document_pos200_response_equivalent_document_instance.to_dict()
# create an instance of CreateEquivalentDocumentPos200ResponseEquivalentDocument from a dict
create_equivalent_document_pos200_response_equivalent_document_from_dict = CreateEquivalentDocumentPos200ResponseEquivalentDocument.from_dict(create_equivalent_document_pos200_response_equivalent_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


