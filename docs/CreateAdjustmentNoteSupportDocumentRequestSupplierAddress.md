# CreateAdjustmentNoteSupportDocumentRequestSupplierAddress

Objeto que contiene la información relacionada a la dirección. <br><i>Grupo de información oficial DIAN &lt;RegistrationAddress | PhysicalLocation&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Dirección del lugar fisico. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Line&amp;gt;&lt;/i&gt; | 
**city** | **str** | Código de la Ciudad. Se debe colocar el Código que corresponda de la tabla de municipios disponibles de la DIAN. Se debe informar cuando el código del País es &#39;CO&#39;. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**department** | **str** | Código del Departamento. Se debe colocar el Código que corresponda de la tabla de departamentos disponibles de la DIAN. Se debe informar cuando el código del País es &#39;CO&#39;( &#x60;origin&#x60; &#x3D; 10 ). &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;CountrySubentityCode&amp;gt;&lt;/i&gt; | [optional] 
**postal_code** | **str** | Código Postal del lugar físico del proveedor. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PostalZone&amp;gt;&lt;/i&gt; | [optional] 
**country** | **str** | Código identificador del País. Se debe colocar el código que corresponda de la tabla de países disponibles de la DIAN. Por defecto &#39;CO&#39;.Es obligatirio cuando no es un Residente fiscal ( &#x60;origin&#x60; &#x3D; 11 ). &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;IdentificationCode&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_support_document_request_supplier_address import CreateAdjustmentNoteSupportDocumentRequestSupplierAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteSupportDocumentRequestSupplierAddress from a JSON string
create_adjustment_note_support_document_request_supplier_address_instance = CreateAdjustmentNoteSupportDocumentRequestSupplierAddress.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteSupportDocumentRequestSupplierAddress.to_json())

# convert the object into a dict
create_adjustment_note_support_document_request_supplier_address_dict = create_adjustment_note_support_document_request_supplier_address_instance.to_dict()
# create an instance of CreateAdjustmentNoteSupportDocumentRequestSupplierAddress from a dict
create_adjustment_note_support_document_request_supplier_address_from_dict = CreateAdjustmentNoteSupportDocumentRequestSupplierAddress.from_dict(create_adjustment_note_support_document_request_supplier_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


