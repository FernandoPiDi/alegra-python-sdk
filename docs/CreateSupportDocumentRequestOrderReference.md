# CreateSupportDocumentRequestOrderReference

**Grupo de campos para la información de la orden de pedido**: Este grupo contiene los campos que describen una orden de compra/pedido asociada al Documento Soporte Electrónico (DSE). Incluye detalles como el número de la orden, la fecha de emisión, y cualquier referencia adicional que sea relevante para el documento. <br><i>Campo oficial DIAN &lt;OrderReference&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Prefijo y Número del documento orden referenciado en el DSE. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**issue_date** | **date** | Corresponde a la fecha en que se generó la orden de compra/pedido. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_support_document_request_order_reference import CreateSupportDocumentRequestOrderReference

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupportDocumentRequestOrderReference from a JSON string
create_support_document_request_order_reference_instance = CreateSupportDocumentRequestOrderReference.from_json(json)
# print the JSON string representation of the object
print(CreateSupportDocumentRequestOrderReference.to_json())

# convert the object into a dict
create_support_document_request_order_reference_dict = create_support_document_request_order_reference_instance.to_dict()
# create an instance of CreateSupportDocumentRequestOrderReference from a dict
create_support_document_request_order_reference_from_dict = CreateSupportDocumentRequestOrderReference.from_dict(create_support_document_request_order_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


