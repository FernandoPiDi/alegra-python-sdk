# CreateSupportDocumentRequestDocumentCurrency

La divisa aplicable al documento soporte debe enviarse a través de este objeto. Si no se incluye, se utilizará COP (Peso Colombiano) como moneda predeterminada.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Código de moneda de la transacción. Ver el listado disponible en la tabla DIAN - Monedas (&#x60;currencies&#x60;)  Esta moneda se aplica a todo el documento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;@currencyID&amp;gt;&lt;/i&gt; | 
**rate_value** | **float** | Valor de la tasa de cambio de la moneda utilizada en el documento en el campo &#39;currencyCode&#39; a Pesos Colombianos. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;CalculationRate&amp;gt;&lt;/i&gt; | 
**rate_date** | **date** | Fecha en la que se fijó o acordó la tasa de cambio. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Date&amp;gt;&lt;/i&gt; | 

## Example

```python
from openapi_client.models.create_support_document_request_document_currency import CreateSupportDocumentRequestDocumentCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupportDocumentRequestDocumentCurrency from a JSON string
create_support_document_request_document_currency_instance = CreateSupportDocumentRequestDocumentCurrency.from_json(json)
# print the JSON string representation of the object
print(CreateSupportDocumentRequestDocumentCurrency.to_json())

# convert the object into a dict
create_support_document_request_document_currency_dict = create_support_document_request_document_currency_instance.to_dict()
# create an instance of CreateSupportDocumentRequestDocumentCurrency from a dict
create_support_document_request_document_currency_from_dict = CreateSupportDocumentRequestDocumentCurrency.from_dict(create_support_document_request_document_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


