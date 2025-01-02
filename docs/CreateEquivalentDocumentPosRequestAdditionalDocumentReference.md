# CreateEquivalentDocumentPosRequestAdditionalDocumentReference

Grupo de campos para información que describen un documento referenciado por el documento equivalente POS electrónico. Este objeto es requerido cuando se generen POS electrónicos en contingencia y deban ser enviados a la DIAN. <i>Grupo de información oficial DIAN &lt;AdditionalDocumentReference&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Prefijo y Número del documento referenciado, para el caso de  documentos POS en contingencia se deberá enviar el número del documento generado. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**issue_date** | **date** | Fecha de emisión del documento referenciado; obligatorio en operaciones en contingencia cuando se quiera referenciar un documento POS físico. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;IssueDate&amp;gt;&lt;/i&gt; | 
**document_type_code** | **str** | Identificador del tipo de documento de referencia, corresponde a una codificación propia de la empresa. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;DocumentTypeCode&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_equivalent_document_pos_request_additional_document_reference import CreateEquivalentDocumentPosRequestAdditionalDocumentReference

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEquivalentDocumentPosRequestAdditionalDocumentReference from a JSON string
create_equivalent_document_pos_request_additional_document_reference_instance = CreateEquivalentDocumentPosRequestAdditionalDocumentReference.from_json(json)
# print the JSON string representation of the object
print(CreateEquivalentDocumentPosRequestAdditionalDocumentReference.to_json())

# convert the object into a dict
create_equivalent_document_pos_request_additional_document_reference_dict = create_equivalent_document_pos_request_additional_document_reference_instance.to_dict()
# create an instance of CreateEquivalentDocumentPosRequestAdditionalDocumentReference from a dict
create_equivalent_document_pos_request_additional_document_reference_from_dict = CreateEquivalentDocumentPosRequestAdditionalDocumentReference.from_dict(create_equivalent_document_pos_request_additional_document_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


