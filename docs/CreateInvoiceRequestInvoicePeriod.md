# CreateInvoiceRequestInvoicePeriod

Objeto que contiene un grupo de campos relativos al periodo de facturación: Intervalo de fechas a las que hace referencia la factura, por ejemplo, en servicios públicos. <br><i>Campo oficial DIAN &lt;InvoicePeriod&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Fecha de inicio del periodo de facturación. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;StartDate&amp;gt;&lt;/i&gt; | 
**start_time** | **str** | Hora de inicio del periodo de facturación. Formato HH:MM:SS, se agregará &#x60;-05:00&#x60; al final en caso de enviarse. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;StartTime&amp;gt;&lt;/i&gt; | [optional] 
**end_date** | **date** | Fecha de fin del periodo de facturación. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;EndDate&amp;gt;&lt;/i&gt; | 
**end_time** | **str** | Hora de fin del periodo de facturación. Formato HH:MM:SS, se agregará &#x60;-05:00&#x60; al final en caso de enviarse. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;EndTime&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_invoice_request_invoice_period import CreateInvoiceRequestInvoicePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestInvoicePeriod from a JSON string
create_invoice_request_invoice_period_instance = CreateInvoiceRequestInvoicePeriod.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestInvoicePeriod.to_json())

# convert the object into a dict
create_invoice_request_invoice_period_dict = create_invoice_request_invoice_period_instance.to_dict()
# create an instance of CreateInvoiceRequestInvoicePeriod from a dict
create_invoice_request_invoice_period_from_dict = CreateInvoiceRequestInvoicePeriod.from_dict(create_invoice_request_invoice_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


