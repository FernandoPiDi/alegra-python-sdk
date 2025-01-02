# GetCreditNotes200ResponseInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id de nota crédito electrónica | [optional] 
**var_date** | **datetime** | Fecha de emisión de nota crédito electrónica | [optional] 
**status** | **str** | Estado de la nota crédito electrónica | [optional] 
**legal_status** | **str** | Estado legal de la nota crédito electrónica ante la DIAN | [optional] 
**company_identification** | **str** | Identificación de la empresa empleadora | [optional] 
**customer_identification** | **str** | Identificación del empleado | [optional] 
**cude** | **str** | Código único de nota crédito electrónica asignado para el documento | [optional] 
**prefix** | **str** | Prefijo de nota crédito electrónica | [optional] 
**number** | **float** | Número de nota crédito electrónica | [optional] 
**full_number** | **str** | Número de nota crédito electrónica (Incluye prefijo y número) | [optional] 
**government_response** | [**GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse**](GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse.md) |  | [optional] 
**xml_file_name** | **str** | Nombre del archivo XML que se envió a la DIAN | [optional] 
**zip_file_name** | **str** | Nombre del archivo Zip que se envió a la DIAN | [optional] 
**qr_code_content** | **str** | Contenido para la construcción del Código QR | [optional] 
**errors** | [**List[CreateEquivalentDocumentPos200ResponseEquivalentDocumentErrorsInner]**](CreateEquivalentDocumentPos200ResponseEquivalentDocumentErrorsInner.md) | Array con mensajes de error generados en el sistema | [optional] 

## Example

```python
from openapi_client.models.get_credit_notes200_response_invoices_inner import GetCreditNotes200ResponseInvoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCreditNotes200ResponseInvoicesInner from a JSON string
get_credit_notes200_response_invoices_inner_instance = GetCreditNotes200ResponseInvoicesInner.from_json(json)
# print the JSON string representation of the object
print(GetCreditNotes200ResponseInvoicesInner.to_json())

# convert the object into a dict
get_credit_notes200_response_invoices_inner_dict = get_credit_notes200_response_invoices_inner_instance.to_dict()
# create an instance of GetCreditNotes200ResponseInvoicesInner from a dict
get_credit_notes200_response_invoices_inner_from_dict = GetCreditNotes200ResponseInvoicesInner.from_dict(get_credit_notes200_response_invoices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


