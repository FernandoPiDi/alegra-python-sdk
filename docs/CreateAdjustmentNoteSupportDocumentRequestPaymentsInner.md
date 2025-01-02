# CreateAdjustmentNoteSupportDocumentRequestPaymentsInner

Información de un pago. <br><i>Grupo de información oficial DIAN &lt;PaymentMeans&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_form** | **str** | Forma de pago. Se debe colocar el Código que corresponda de la tabla de formas de pago disponibles de la DIAN. Valores posible: &#x60;1&#x60;: Contado, &#x60;2&#x60;: Crédito &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**payment_method** | **str** | Medio de pago. Se debe colocar el Código que corresponda de la tabla de métodos de pago disponibles de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PaymentMeansCode&amp;gt;&lt;/i&gt; | 
**payment_due_date** | **date** | Fecha de vencimiento de la factura. Si Forma de Pago es igual a 2, este valor debe ser enviado. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PaymentDueDate&amp;gt;&lt;/i&gt; | [optional] 
**payment_id** | **str** | Texto libre para informar datos adicionales sobre el medio de pago. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PaymentID&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_support_document_request_payments_inner import CreateAdjustmentNoteSupportDocumentRequestPaymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteSupportDocumentRequestPaymentsInner from a JSON string
create_adjustment_note_support_document_request_payments_inner_instance = CreateAdjustmentNoteSupportDocumentRequestPaymentsInner.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteSupportDocumentRequestPaymentsInner.to_json())

# convert the object into a dict
create_adjustment_note_support_document_request_payments_inner_dict = create_adjustment_note_support_document_request_payments_inner_instance.to_dict()
# create an instance of CreateAdjustmentNoteSupportDocumentRequestPaymentsInner from a dict
create_adjustment_note_support_document_request_payments_inner_from_dict = CreateAdjustmentNoteSupportDocumentRequestPaymentsInner.from_dict(create_adjustment_note_support_document_request_payments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


