# CreateSupportDocumentRequestTotalAmounts

Objeto que contiene la información de totales relacionados con el documento

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gross_total** | **float** | Total valor bruto antes de tributos. Suma de todos los subtotales correspondientes a los árticulos y/o servicios. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;LegalMonetaryTotal&amp;gt;&lt;/i&gt; | 
**taxable_total** | **float** | Total valor base imponible. Base imponible para el cálculo de los tributos. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;TaxExclusiveAmount&amp;gt;&lt;/i&gt; | 
**tax_total** | **float** | Total valor tributos/impuestos. &lt;br&gt;&lt;i&gt;Valor asociado en el calculo del campo oficial DIAN &amp;lt;TaxInclusiveAmount&amp;gt;&lt;/i&gt; | 
**discount_total** | **float** | Total valor descuentos. Suma de todos los descuentos aplicados al total de la factura. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;AllowanceTotalAmount&amp;gt;&lt;/i&gt; | [optional] 
**charge_total** | **float** | Total valor cargos. Suma de todos los cargos aplicados al total de la factura. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ChargeTotalAmount&amp;gt;&lt;/i&gt; | [optional] 
**payable_total** | **float** | Total valor factura. Valor total de ítems (incluyendo cargos y descuentos a nivel de ítems) + valor tributos + valor cargos – valor descuentos. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PayableAmount&amp;gt;&lt;/i&gt; | 

## Example

```python
from openapi_client.models.create_support_document_request_total_amounts import CreateSupportDocumentRequestTotalAmounts

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupportDocumentRequestTotalAmounts from a JSON string
create_support_document_request_total_amounts_instance = CreateSupportDocumentRequestTotalAmounts.from_json(json)
# print the JSON string representation of the object
print(CreateSupportDocumentRequestTotalAmounts.to_json())

# convert the object into a dict
create_support_document_request_total_amounts_dict = create_support_document_request_total_amounts_instance.to_dict()
# create an instance of CreateSupportDocumentRequestTotalAmounts from a dict
create_support_document_request_total_amounts_from_dict = CreateSupportDocumentRequestTotalAmounts.from_dict(create_support_document_request_total_amounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


