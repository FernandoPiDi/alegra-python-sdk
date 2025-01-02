# CreateSupportDocumentRequestItemsInnerStandardCode

Este grupo de datos se utiliza para identificar el artículo o servicio de acuerdo con un estándar establecido. <br><i>Grupo de información oficial DIAN &lt;StandardItemIdentification&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identification_id** | **str** | Código de artículo de acuerdo al estándar utilizado. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**id** | **str** | Código del estándar. Deberá contener uno de los siguientes valores posibles de acuerdo al código utilizado para identificar el ítem en el elemento &#x60;identificationId&#x60;:&#x60;001&#x60;: UNSPSC-Colombia Compra Eficiente; &#x60;010&#x60; GTIN-Números Globales de Identificación de Productos – GTIN; &#x60;020&#x60; Partida arancelaria según estatus tributario;&#x60;999&#x60; Estándar de adopción del contribuyente. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;schemeID&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_support_document_request_items_inner_standard_code import CreateSupportDocumentRequestItemsInnerStandardCode

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupportDocumentRequestItemsInnerStandardCode from a JSON string
create_support_document_request_items_inner_standard_code_instance = CreateSupportDocumentRequestItemsInnerStandardCode.from_json(json)
# print the JSON string representation of the object
print(CreateSupportDocumentRequestItemsInnerStandardCode.to_json())

# convert the object into a dict
create_support_document_request_items_inner_standard_code_dict = create_support_document_request_items_inner_standard_code_instance.to_dict()
# create an instance of CreateSupportDocumentRequestItemsInnerStandardCode from a dict
create_support_document_request_items_inner_standard_code_from_dict = CreateSupportDocumentRequestItemsInnerStandardCode.from_dict(create_support_document_request_items_inner_standard_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


