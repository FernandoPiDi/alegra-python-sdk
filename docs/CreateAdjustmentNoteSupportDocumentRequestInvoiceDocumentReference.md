# CreateAdjustmentNoteSupportDocumentRequestInvoiceDocumentReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id registrado por la API E-providers, en caso de que el documento de referencia haya sido emitido a través de E-providers solo se necesita este dato para identificar el documento. En caso de que no se especifique los campos &#x60;fullNumber&#x60; y &#x60;cuds&#x60; son obligatorios. | [optional] 
**full_number** | **str** | Número del Documento Soporte al que se hace referencia. (Prefijo + Número). Se indica en caso de que sea un documento equivalente emitido con otro proveedor y/o el id no se especifique. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | [optional] 
**cuds** | **str** | Cude del Documento Soporte relacionado. Se indica en caso de que sea un documento equivalente emitido con otro proveedor y/o el id no se especifique. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;UUID&amp;gt;&lt;/i&gt; | [optional] 
**var_date** | **str** | Fecha del documento referenciado. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;IssueDate&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_support_document_request_invoice_document_reference import CreateAdjustmentNoteSupportDocumentRequestInvoiceDocumentReference

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteSupportDocumentRequestInvoiceDocumentReference from a JSON string
create_adjustment_note_support_document_request_invoice_document_reference_instance = CreateAdjustmentNoteSupportDocumentRequestInvoiceDocumentReference.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteSupportDocumentRequestInvoiceDocumentReference.to_json())

# convert the object into a dict
create_adjustment_note_support_document_request_invoice_document_reference_dict = create_adjustment_note_support_document_request_invoice_document_reference_instance.to_dict()
# create an instance of CreateAdjustmentNoteSupportDocumentRequestInvoiceDocumentReference from a dict
create_adjustment_note_support_document_request_invoice_document_reference_from_dict = CreateAdjustmentNoteSupportDocumentRequestInvoiceDocumentReference.from_dict(create_adjustment_note_support_document_request_invoice_document_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


