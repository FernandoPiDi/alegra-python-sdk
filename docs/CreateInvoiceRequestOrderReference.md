# CreateInvoiceRequestOrderReference

Grupo de campos para información que describen una Orden de Pedido para esta factura. <br><i>Grupo de información oficial DIAN &lt;OrderReference&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Prefijo y Número del documento Orden referenciado | 
**issue_date** | **date** | Fecha de emisión: Fecha de emisión de la Orden | [optional] 

## Example

```python
from openapi_client.models.create_invoice_request_order_reference import CreateInvoiceRequestOrderReference

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestOrderReference from a JSON string
create_invoice_request_order_reference_instance = CreateInvoiceRequestOrderReference.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestOrderReference.to_json())

# convert the object into a dict
create_invoice_request_order_reference_dict = create_invoice_request_order_reference_instance.to_dict()
# create an instance of CreateInvoiceRequestOrderReference from a dict
create_invoice_request_order_reference_from_dict = CreateInvoiceRequestOrderReference.from_dict(create_invoice_request_order_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


