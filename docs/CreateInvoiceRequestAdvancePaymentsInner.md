# CreateInvoiceRequestAdvancePaymentsInner

Información de un anticipo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advance_id** | **str** | Identificación o código del pago. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**advance_amount** | **float** | Valor del pago/anticipo. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PaidAmount&amp;gt;&lt;/i&gt; | 
**advance_received_date** | **date** | Fecha en la cual el pago/anticipo fue recibido. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ReceivedDate&amp;gt;&lt;/i&gt; | 
**instruction_id** | **str** | Instrucciones relativas al pago. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;InstructionID&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_invoice_request_advance_payments_inner import CreateInvoiceRequestAdvancePaymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestAdvancePaymentsInner from a JSON string
create_invoice_request_advance_payments_inner_instance = CreateInvoiceRequestAdvancePaymentsInner.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestAdvancePaymentsInner.to_json())

# convert the object into a dict
create_invoice_request_advance_payments_inner_dict = create_invoice_request_advance_payments_inner_instance.to_dict()
# create an instance of CreateInvoiceRequestAdvancePaymentsInner from a dict
create_invoice_request_advance_payments_inner_from_dict = CreateInvoiceRequestAdvancePaymentsInner.from_dict(create_invoice_request_advance_payments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


