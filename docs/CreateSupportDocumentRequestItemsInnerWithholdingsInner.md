# CreateSupportDocumentRequestItemsInnerWithholdingsInner

Objeto que contiene la información tributaria del articulo y/o servicio

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_code** | **str** | Código o identificador del impuesto. Se debe colocar el Código que corresponda de la tabla de tipos de tributos/impuestos disponibles de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**tax_amount** | **float** | Valor y/o importe del impuesto. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;TaxAmount&amp;gt;&lt;/i&gt; | 
**tax_percentage** | **str** | Porcentaje o tarifa de retención. Ejemplo: Para indicar la tarifa general asociada al impuesto de ReteIVA, se debe enviar un porcentaje de &#39;100.00&#39; o &#39;15.00&#39;. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Percent&amp;gt;&lt;/i&gt; | 
**taxable_amount** | **float** | Base Imponible sobre la que se calcula el valor del impuesto. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;TaxableAmount&amp;gt;&lt;/i&gt; | 

## Example

```python
from openapi_client.models.create_support_document_request_items_inner_withholdings_inner import CreateSupportDocumentRequestItemsInnerWithholdingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupportDocumentRequestItemsInnerWithholdingsInner from a JSON string
create_support_document_request_items_inner_withholdings_inner_instance = CreateSupportDocumentRequestItemsInnerWithholdingsInner.from_json(json)
# print the JSON string representation of the object
print(CreateSupportDocumentRequestItemsInnerWithholdingsInner.to_json())

# convert the object into a dict
create_support_document_request_items_inner_withholdings_inner_dict = create_support_document_request_items_inner_withholdings_inner_instance.to_dict()
# create an instance of CreateSupportDocumentRequestItemsInnerWithholdingsInner from a dict
create_support_document_request_items_inner_withholdings_inner_from_dict = CreateSupportDocumentRequestItemsInnerWithholdingsInner.from_dict(create_support_document_request_items_inner_withholdings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


