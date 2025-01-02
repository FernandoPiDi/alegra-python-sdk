# CreateSupportDocumentRequestResolution

Objeto que contiene la información de la resolución asociada al emisor del documento soporte electrónica en formato JSON según el estándar de la DIAN. <br><i>Grupo de información oficial DIAN &lt;InvoiceControl&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution_number** | **str** | Número de Resolución o de Autorización: Número del código de la resolución otorgada para la numeración. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;InvoiceAuthorization&amp;gt;&lt;/i&gt; | 
**prefix** | **str** | Prefijo de la Resolución o Autorización. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Prefix&amp;gt;&lt;/i&gt; | [optional] 
**min_number** | **float** | Valor inicial del rango de numeración. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;From&amp;gt;&lt;/i&gt; | 
**max_number** | **float** | Valor final del rango de numeración. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;To&amp;gt;&lt;/i&gt; | 
**start_date** | **date** | Fecha de inicio de la autorización de la numeración. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;StartDate&amp;gt;&lt;/i&gt; | 
**end_date** | **date** | Fecha final de la autorización de la numeración. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;EndDate&amp;gt;&lt;/i&gt; | 

## Example

```python
from openapi_client.models.create_support_document_request_resolution import CreateSupportDocumentRequestResolution

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupportDocumentRequestResolution from a JSON string
create_support_document_request_resolution_instance = CreateSupportDocumentRequestResolution.from_json(json)
# print the JSON string representation of the object
print(CreateSupportDocumentRequestResolution.to_json())

# convert the object into a dict
create_support_document_request_resolution_dict = create_support_document_request_resolution_instance.to_dict()
# create an instance of CreateSupportDocumentRequestResolution from a dict
create_support_document_request_resolution_from_dict = CreateSupportDocumentRequestResolution.from_dict(create_support_document_request_resolution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


