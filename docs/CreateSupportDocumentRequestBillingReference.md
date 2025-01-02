# CreateSupportDocumentRequestBillingReference

Exclusivo para referenciar la Nota de Ajuste que dio origen al presente Documento Soporte Electrónico (DSE). Incluye los datos clave de la Nota de Ajuste, como el número, la fecha de emisión y el motivo del ajuste. <br><i>Campo oficial DIAN &lt;BillingReference&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id registrado por la API E-providers, en caso de que el documento de referencia haya sido emitido a través de E-providers solo se necesita este dato para identificar el documento, de lo contratrio deben enviarse los campos &#x60;fullNumber&#x60;, &#x60;cuds&#x60; y &#x60;date&#x60;. | [optional] 
**full_number** | **str** | Prefijo + Número de la nota de ajuste referenciada. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | [optional] 
**cuds** | **str** | CUDS de la nota de ajuste relacionada. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;UUID&amp;gt;&lt;/i&gt; | [optional] 
**var_date** | **date** | Fecha de generación de la nota de ajuste relacionada. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_support_document_request_billing_reference import CreateSupportDocumentRequestBillingReference

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupportDocumentRequestBillingReference from a JSON string
create_support_document_request_billing_reference_instance = CreateSupportDocumentRequestBillingReference.from_json(json)
# print the JSON string representation of the object
print(CreateSupportDocumentRequestBillingReference.to_json())

# convert the object into a dict
create_support_document_request_billing_reference_dict = create_support_document_request_billing_reference_instance.to_dict()
# create an instance of CreateSupportDocumentRequestBillingReference from a dict
create_support_document_request_billing_reference_from_dict = CreateSupportDocumentRequestBillingReference.from_dict(create_support_document_request_billing_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


