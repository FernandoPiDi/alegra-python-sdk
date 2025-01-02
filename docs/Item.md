# Item

Objeto que contiene la información del listado de articulos y/o servicios. <br><i>Grupo de información oficial DIAN &lt;InvoiceLine&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Código del articulo y/o servicio adoptado por el emisor. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;StandardItemIdentification&amp;gt;&lt;/i&gt; | [optional] 
**standard_code** | [**CreateEquivalentDocumentPosRequestItemsInnerCode**](CreateEquivalentDocumentPosRequestItemsInnerCode.md) |  | [optional] 
**description** | **str** | Nombre y descripción del articulo y/o servicio que se está vendiendo en esta linea del documento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Description&amp;gt;&lt;/i&gt; | 
**price** | **float** | Precio del articulo y/o servicio. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PriceAmount&amp;gt;&lt;/i&gt; | 
**price_reference** | [**CreateInvoiceRequestItemsInnerAllOfPriceReference**](CreateInvoiceRequestItemsInnerAllOfPriceReference.md) |  | [optional] 
**discount** | **float** | Porcentaje de descuento del articulo y/o servicio. Se debe informar a nivel de ítem, si y solamente si el descuento afecta la base gravable del ítem. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;/cac:AllowanceCharge/cbc:MultiplierFactorNumeric&amp;gt;&lt;/i&gt; | [optional] 
**discount_amount** | **float** | Valor de descuento del articulo y/o servicio. Se debe informar a nivel de ítem, si y solamente si el descuento afecta la base gravable del ítem. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;/cac:AllowanceCharge/cbc:Amount&amp;gt;&lt;/i&gt; | [optional] 
**quantity** | **float** | Cantidad del articulo y/o servicio. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;InvoicedQuantity&amp;gt;&lt;/i&gt; | 
**unit_code** | **str** | Código de Unidad de medida del articulo y/o servicio. Se debe colocar el Código que corresponda de la tabla de unidades de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;@unitCode&amp;gt;&lt;/i&gt; | 
**note** | **str** | Información Adicional o texto libre para añadir información del articulo y/o servicio. Obligatorio de informarse para el caso de ítems de contratos de servicio tipo AIU para el item Administración. Aquí, se debe empezar por el texto: &#39;Contrato de servicios AIU por concepto de:&#39;. Y el contribuyente debe incluir el objeto del contrato facturado. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Note&amp;gt;&lt;/i&gt; | [optional] 
**subtotal** | **float** | Subtotal del articulo y/o servicio. El subtotal de la línea es igual a la Cantidad x Precio Unidad menos Descuentos más Recargos que apliquen al articulo y/o servicio. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;LineExtensionAmount&amp;gt;&lt;/i&gt; | 
**tax_amount** | **float** | Valor total de los impuestos aplicados al articulo y/o servicio. | 
**taxes** | [**List[CreateInvoiceRequestItemsInnerAllOfTaxesInner]**](CreateInvoiceRequestItemsInnerAllOfTaxesInner.md) | Array que contiene el listado de tributos/impuestos que aplican al articulo y/o servicio | [optional] 
**third_party_information** | [**CreateInvoiceRequestItemsInnerAllOfThirdPartyInformation**](CreateInvoiceRequestItemsInnerAllOfThirdPartyInformation.md) |  | [optional] 
**withholdings** | [**List[CreateInvoiceRequestItemsInnerAllOfTaxesInner]**](CreateInvoiceRequestItemsInnerAllOfTaxesInner.md) | Array con el listado de Retenciones. Grupo de campos que contiene la información de los tributos retenidos. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;WithholdingTaxTotal&amp;gt;&lt;/i&gt; | [optional] 
**pack_size** | **float** | Número de productos por empaque. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PackSizeNumeric&amp;gt;&lt;/i&gt; | [optional] 
**brand_name** | **str** | Marca del artículo. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;BrandName&amp;gt;&lt;/i&gt; | [optional] 
**model_name** | **str** | Modelo del artículo. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ModelName&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


