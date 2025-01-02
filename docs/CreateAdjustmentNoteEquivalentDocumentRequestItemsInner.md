# CreateAdjustmentNoteEquivalentDocumentRequestItemsInner

Objeto que contiene la información del listado de articulos y/o servicios. <br><i>Grupo de información oficial DIAN &lt;InvoiceLine&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**CreateAdjustmentNoteEquivalentDocumentRequestItemsInnerCode**](CreateAdjustmentNoteEquivalentDocumentRequestItemsInnerCode.md) |  | [optional] 
**description** | **str** | Nombre y descripción del articulo y/o servicio que se está vendiendo en esta linea del documento. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Description&amp;gt;&lt;/i&gt; | 
**price** | **float** | Precio del articulo y/o servicio. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PriceAmount&amp;gt;&lt;/i&gt; | 
**price_reference** | **float** | Precio de referencia del articulo y/o servicio que no contiene valor comercial. Si se informa, entonces el atributo &#39;price&#39; debe ser cero (0.00), ya que se trata de una muestra o regalo comercial. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PriceAmount&amp;gt;&lt;/i&gt; | [optional] 
**discount** | **float** | Porcentaje de descuento del articulo y/o servicio. Se debe informar a nivel de ítem, si y solamente si el descuento afecta la base gravable del ítem. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;/cac:AllowanceCharge/cbc:MultiplierFactorNumeric&amp;gt;&lt;/i&gt; | [optional] 
**discount_amount** | **float** | Valor de descuento del articulo y/o servicio. Se debe informar a nivel de ítem, si y solamente si el descuento afecta la base gravable del ítem. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;/cac:AllowanceCharge/cbc:Amount&amp;gt;&lt;/i&gt; | [optional] 
**charge** | **float** | Porcentaje de cargo adicional aplicado articulo y/o servicio | [optional] 
**charge_amount** | **float** | Valor del cargo adicional del articulo y/o servicio | [optional] 
**quantity** | **float** | Cantidad del articulo y/o servicio. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;InvoicedQuantity&amp;gt;&lt;/i&gt; | 
**unit_code** | **str** | Código de Unidad de medida del articulo y/o servicio. Se debe colocar el Código que corresponda de la tabla de unidades de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;@unitCode&amp;gt;&lt;/i&gt; | 
**note** | **str** | Información Adicional o texto libre para añadir información del articulo y/o servicio. Obligatorio de informarse para el caso de ítems de contratos de servicio tipo AIU para el item Administración. Aquí, se debe empezar por el texto: &#39;Contrato de servicios AIU por concepto de:&#39;. Y el contribuyente debe incluir el objeto del contrato facturado. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Note&amp;gt;&lt;/i&gt; | [optional] 
**subtotal** | **float** | Subtotal del articulo y/o servicio. El subtotal de la línea es igual a la Cantidad x Precio Unidad menos Descuentos más Recargos que apliquen al articulo y/o servicio. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;LineExtensionAmount&amp;gt;&lt;/i&gt; | 
**tax_amount** | **float** | Valor total de los impuestos aplicados al articulo y/o servicio. | 
**total** | **float** | Valor total del articulo y/o servicio. | 
**taxes** | [**List[CreateEquivalentDocumentPosRequestItemsInnerTaxesInner]**](CreateEquivalentDocumentPosRequestItemsInnerTaxesInner.md) | Array que contiene el listado de tributos/impuestos que aplican al articulo y/o servicio | [optional] 
**pack_size** | **float** | Número de productos por empaque. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PackSizeNumeric&amp;gt;&lt;/i&gt; | [optional] 
**brand_name** | **str** | Marca del artículo. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;BrandName&amp;gt;&lt;/i&gt; | [optional] 
**model_name** | **str** | Modelo del artículo. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ModelName&amp;gt;&lt;/i&gt; | [optional] 
**additional_item_properties** | [**List[CreateEquivalentDocumentPosRequestItemsInnerAdditionalItemPropertiesInner]**](CreateEquivalentDocumentPosRequestItemsInnerAdditionalItemPropertiesInner.md) | Array que contiene el grupo de información para adicionar información específica del ítem que puede ser solicitada por autoridades o entidades diferentes a la DIAN | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_equivalent_document_request_items_inner import CreateAdjustmentNoteEquivalentDocumentRequestItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestItemsInner from a JSON string
create_adjustment_note_equivalent_document_request_items_inner_instance = CreateAdjustmentNoteEquivalentDocumentRequestItemsInner.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteEquivalentDocumentRequestItemsInner.to_json())

# convert the object into a dict
create_adjustment_note_equivalent_document_request_items_inner_dict = create_adjustment_note_equivalent_document_request_items_inner_instance.to_dict()
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestItemsInner from a dict
create_adjustment_note_equivalent_document_request_items_inner_from_dict = CreateAdjustmentNoteEquivalentDocumentRequestItemsInner.from_dict(create_adjustment_note_equivalent_document_request_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


