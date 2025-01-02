# GetInvoices200ResponseInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id de factura electrónica | [optional] 
**var_date** | **datetime** | Fecha de emisión de factura electrónica | [optional] 
**status** | **str** | Estado de la factura electrónica | [optional] 
**legal_status** | **str** | Estado legal de la factura electrónica ante la DIAN | [optional] 
**company_identification** | **str** | Identificación de la empresa empleadora | [optional] 
**customer_identification** | **str** | Identificación del empleado | [optional] 
**cufe** | **str** | Código único de factura electrónica asignado para el documento | [optional] 
**prefix** | **str** | Prefijo de factura electrónica | [optional] 
**number** | **float** | Número de factura electrónica | [optional] 
**full_number** | **str** | Número de factura electrónica (Incluye prefijo y número) | [optional] 
**government_response** | [**GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse**](GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse.md) |  | [optional] 
**xml_file_name** | **str** | Nombre del archivo XML que se envió a la DIAN | [optional] 
**zip_file_name** | **str** | Nombre del archivo Zip que se envió a la DIAN | [optional] 
**zip** | **str** | Link de descarga a el archivo Zip que contiene el PDF de la factura y el AttachedDocument (XML). Este campo solo se añade cuando la factura no esta rechazada. Este enlace solo dura por 60 minutos, para renovar el link solicite nuevamente el documento. | [optional] 
**qr_code_content** | **str** | Contenido para la construcción del Código QR | [optional] 
**errors** | [**List[CreateEquivalentDocumentPos200ResponseEquivalentDocumentErrorsInner]**](CreateEquivalentDocumentPos200ResponseEquivalentDocumentErrorsInner.md) | Array con mensajes de error generados en el sistema | [optional] 

## Example

```python
from openapi_client.models.get_invoices200_response_invoices_inner import GetInvoices200ResponseInvoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoices200ResponseInvoicesInner from a JSON string
get_invoices200_response_invoices_inner_instance = GetInvoices200ResponseInvoicesInner.from_json(json)
# print the JSON string representation of the object
print(GetInvoices200ResponseInvoicesInner.to_json())

# convert the object into a dict
get_invoices200_response_invoices_inner_dict = get_invoices200_response_invoices_inner_instance.to_dict()
# create an instance of GetInvoices200ResponseInvoicesInner from a dict
get_invoices200_response_invoices_inner_from_dict = GetInvoices200ResponseInvoicesInner.from_dict(get_invoices200_response_invoices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


