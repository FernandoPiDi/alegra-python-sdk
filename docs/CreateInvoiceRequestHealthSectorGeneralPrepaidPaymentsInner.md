# CreateInvoiceRequestHealthSectorGeneralPrepaidPaymentsInner

Objeto que contiene la información de los pagos anticipados. <br><i>Grupo de información oficial DIAN &lt;PrepaidPayment&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Codigo del pago anticipado, según la tabla &#x60;conceptoRecaudo&#x60;. (01): Copago, (02): Cuota moderadora, (03): Pagos compartidos en planes voluntarios de salud, (04): Anticipo, (05): No aplica | 
**amount** | **float** | Valor del pago | 
**received_date** | **date** | Fecha en la cual el pago fue recibido. Formato AAAA-MM-DD | 

## Example

```python
from openapi_client.models.create_invoice_request_health_sector_general_prepaid_payments_inner import CreateInvoiceRequestHealthSectorGeneralPrepaidPaymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestHealthSectorGeneralPrepaidPaymentsInner from a JSON string
create_invoice_request_health_sector_general_prepaid_payments_inner_instance = CreateInvoiceRequestHealthSectorGeneralPrepaidPaymentsInner.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestHealthSectorGeneralPrepaidPaymentsInner.to_json())

# convert the object into a dict
create_invoice_request_health_sector_general_prepaid_payments_inner_dict = create_invoice_request_health_sector_general_prepaid_payments_inner_instance.to_dict()
# create an instance of CreateInvoiceRequestHealthSectorGeneralPrepaidPaymentsInner from a dict
create_invoice_request_health_sector_general_prepaid_payments_inner_from_dict = CreateInvoiceRequestHealthSectorGeneralPrepaidPaymentsInner.from_dict(create_invoice_request_health_sector_general_prepaid_payments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


