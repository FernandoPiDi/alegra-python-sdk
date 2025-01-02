# CreateEquivalentDocumentPosRequestExchangeRate

Grupo de campos para información relacionada con la tasa de cambio de moneda extranjera a Peso Colombiano (COP). Se debe informar cuando la moneda del documento es diferente a Peso Colombiano (COP). <br><i>Grupo de información oficial DIAN &lt;PaymentExchangeRate&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_value** | **float** | Valor de la tasa de cambio de la moneda utilizada en el documento en el campo &#39;currencyCode&#39; a Pesos Colombianos. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;CalculationRate&amp;gt;&lt;/i&gt; | 
**rate_date** | **date** | Fecha en la que se fijó o acordó la tasa de cambio. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Date&amp;gt;&lt;/i&gt; | 

## Example

```python
from openapi_client.models.create_equivalent_document_pos_request_exchange_rate import CreateEquivalentDocumentPosRequestExchangeRate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEquivalentDocumentPosRequestExchangeRate from a JSON string
create_equivalent_document_pos_request_exchange_rate_instance = CreateEquivalentDocumentPosRequestExchangeRate.from_json(json)
# print the JSON string representation of the object
print(CreateEquivalentDocumentPosRequestExchangeRate.to_json())

# convert the object into a dict
create_equivalent_document_pos_request_exchange_rate_dict = create_equivalent_document_pos_request_exchange_rate_instance.to_dict()
# create an instance of CreateEquivalentDocumentPosRequestExchangeRate from a dict
create_equivalent_document_pos_request_exchange_rate_from_dict = CreateEquivalentDocumentPosRequestExchangeRate.from_dict(create_equivalent_document_pos_request_exchange_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


