# GetResolutions200ResponseResolutionsInner

Objeto que contiene la información de la Resolución de Numeración de Facturas asociada al emisor de la factura electrónica en formato JSON según el estándar de la DIAN. <br><i>Grupo de información oficial DIAN &lt;InvoiceControl&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution_number** | **str** | Número de Resolución o de Autorización: Número del código de la resolución otorgada para la numeración. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;InvoiceAuthorization&amp;gt;&lt;/i&gt; | 
**prefix** | **str** | Prefijo de la Resolución o Autorización. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Prefix&amp;gt;&lt;/i&gt; | [optional] 
**min_number** | **float** | Valor inicial del rango de numeración. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;From&amp;gt;&lt;/i&gt; | [optional] 
**max_number** | **float** | Valor final del rango de numeración. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;To&amp;gt;&lt;/i&gt; | [optional] 
**start_date** | **date** | Fecha de inicio de la autorización de la numeración. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;StartDate&amp;gt;&lt;/i&gt; | 
**end_date** | **date** | Fecha final de la autorización de la numeración. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;EndDate&amp;gt;&lt;/i&gt; | 
**technical_key** | **str** | Clave técnica del rango de facturación. &lt;br&gt;&lt;i&gt;ClTec: Obligatorio para la generación del CUFE (Código Único de Factura Electrónica)&lt;/i&gt; | 

## Example

```python
from openapi_client.models.get_resolutions200_response_resolutions_inner import GetResolutions200ResponseResolutionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetResolutions200ResponseResolutionsInner from a JSON string
get_resolutions200_response_resolutions_inner_instance = GetResolutions200ResponseResolutionsInner.from_json(json)
# print the JSON string representation of the object
print(GetResolutions200ResponseResolutionsInner.to_json())

# convert the object into a dict
get_resolutions200_response_resolutions_inner_dict = get_resolutions200_response_resolutions_inner_instance.to_dict()
# create an instance of GetResolutions200ResponseResolutionsInner from a dict
get_resolutions200_response_resolutions_inner_from_dict = GetResolutions200ResponseResolutionsInner.from_dict(get_resolutions200_response_resolutions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


