# CreateSupportDocumentRequestItemsInnerInvoicePeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description_code** | **float** | Este campo permite indicar la forma de generación y transmisión de la información, utilizando los siguientes códigos: 1 &#x3D; Por operación o 2 &#x3D; Acumulado semanal. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;DescriptionCode&amp;gt;&lt;/i&gt; | 
**start_date** | **date** | Aplica para las compras con reporte semanal. Indica la fecha en la que se realizó la transacción, y se incluirá dentro del acumulado correspondiente al reporte semanal. Este campo pasa a ser obligatorio cuando &#x60;descriptionCode&#x60; es igual a &#x60;2&#x60;. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;StartDate&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_support_document_request_items_inner_invoice_period import CreateSupportDocumentRequestItemsInnerInvoicePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupportDocumentRequestItemsInnerInvoicePeriod from a JSON string
create_support_document_request_items_inner_invoice_period_instance = CreateSupportDocumentRequestItemsInnerInvoicePeriod.from_json(json)
# print the JSON string representation of the object
print(CreateSupportDocumentRequestItemsInnerInvoicePeriod.to_json())

# convert the object into a dict
create_support_document_request_items_inner_invoice_period_dict = create_support_document_request_items_inner_invoice_period_instance.to_dict()
# create an instance of CreateSupportDocumentRequestItemsInnerInvoicePeriod from a dict
create_support_document_request_items_inner_invoice_period_from_dict = CreateSupportDocumentRequestItemsInnerInvoicePeriod.from_dict(create_support_document_request_items_inner_invoice_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


