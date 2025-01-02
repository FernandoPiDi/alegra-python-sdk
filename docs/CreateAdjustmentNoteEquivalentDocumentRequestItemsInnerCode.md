# CreateAdjustmentNoteEquivalentDocumentRequestItemsInnerCode

Objeto que contiene el grupo de datos de identificación del artículo y/o servicio de acuerdo con un estándar. <br><i>Grupo de información oficial DIAN &lt;StandardItemIdentification&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identification_id** | **str** | Código de artículo de acuerdo con el estándar descrito en el atributo. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | [optional] 
**id** | **str** | Código del estándar. Se debe colocar el Código que corresponda de la tabla de Códigos de Productos disponibles de la DIAN&lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;schemeID&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_equivalent_document_request_items_inner_code import CreateAdjustmentNoteEquivalentDocumentRequestItemsInnerCode

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestItemsInnerCode from a JSON string
create_adjustment_note_equivalent_document_request_items_inner_code_instance = CreateAdjustmentNoteEquivalentDocumentRequestItemsInnerCode.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteEquivalentDocumentRequestItemsInnerCode.to_json())

# convert the object into a dict
create_adjustment_note_equivalent_document_request_items_inner_code_dict = create_adjustment_note_equivalent_document_request_items_inner_code_instance.to_dict()
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestItemsInnerCode from a dict
create_adjustment_note_equivalent_document_request_items_inner_code_from_dict = CreateAdjustmentNoteEquivalentDocumentRequestItemsInnerCode.from_dict(create_adjustment_note_equivalent_document_request_items_inner_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


