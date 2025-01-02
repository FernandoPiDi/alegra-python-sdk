# CreateInvoiceRequestAdditionalDocumentReference

Grupo de campos para información que describen un documento referenciado por esta factura. Este objeto es requerido para Factura electrónica de Contingencia. <br><i>Grupo de información oficial DIAN &lt;AdditionalDocumentReference&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Prefijo y Número del documento referenciado, para el caso de facturas en contingencia se deberá enviar el número de la factura de talonario o de papel generada y entregada al cliente. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**issue_date** | **str** | Fecha de emisión del documento referenciado. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;IssueDate&amp;gt;&lt;/i&gt; | 
**document_type_code** | **str** | Identificador del tipo de documento de referencia, corresponde a una codificación propia de la empresa. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;DocumentTypeCode&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_invoice_request_additional_document_reference import CreateInvoiceRequestAdditionalDocumentReference

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestAdditionalDocumentReference from a JSON string
create_invoice_request_additional_document_reference_instance = CreateInvoiceRequestAdditionalDocumentReference.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestAdditionalDocumentReference.to_json())

# convert the object into a dict
create_invoice_request_additional_document_reference_dict = create_invoice_request_additional_document_reference_instance.to_dict()
# create an instance of CreateInvoiceRequestAdditionalDocumentReference from a dict
create_invoice_request_additional_document_reference_from_dict = CreateInvoiceRequestAdditionalDocumentReference.from_dict(create_invoice_request_additional_document_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


