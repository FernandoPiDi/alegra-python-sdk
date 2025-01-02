# CreateAdjustmentNoteSupportDocumentRequestDiscrepanciesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **float** | Código de descripción de la corrección, ver lista de valores admitidos por la dian. Valores proibles: &lt;br&gt; - &#x60;1&#x60;: Devolución parcial de los bienes y/o no aceptación parcial del servicio. &lt;br&gt; - &#x60;2&#x60;: Anulación del documento soporte en adquisiciones efectuadas a sujetos no obligados a expedir factura de venta o documento equivalente. &lt;br&gt; - &#x60;3&#x60;: Rebaja  o descuento parcial o total. &lt;br&gt; - &#x60;4&#x60;: Ajuste de precio. &lt;br&gt; - &#x60;5&#x60;: Otros. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ResponseCode&amp;gt;&lt;/i&gt; | 
**description** | **str** | Descripción de la naturaleza de la corrección. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Description&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_support_document_request_discrepancies_inner import CreateAdjustmentNoteSupportDocumentRequestDiscrepanciesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteSupportDocumentRequestDiscrepanciesInner from a JSON string
create_adjustment_note_support_document_request_discrepancies_inner_instance = CreateAdjustmentNoteSupportDocumentRequestDiscrepanciesInner.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteSupportDocumentRequestDiscrepanciesInner.to_json())

# convert the object into a dict
create_adjustment_note_support_document_request_discrepancies_inner_dict = create_adjustment_note_support_document_request_discrepancies_inner_instance.to_dict()
# create an instance of CreateAdjustmentNoteSupportDocumentRequestDiscrepanciesInner from a dict
create_adjustment_note_support_document_request_discrepancies_inner_from_dict = CreateAdjustmentNoteSupportDocumentRequestDiscrepanciesInner.from_dict(create_adjustment_note_support_document_request_discrepancies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


