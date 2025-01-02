# Tax

Objeto que contiene la información tributaria del articulo y/o servicio 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_code** | **str** | Código o identificador del impuesto. Se debe colocar el Código que corresponda de la tabla de tipos de tributos/impuestos disponibles de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**tax_amount** | **float** | Valor y/o importe del impuesto. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;TaxAmount&amp;gt;&lt;/i&gt; | 
**tax_percentage** | **str** | Porcentaje o tarifa de impuesto. Ejemplo: Para indicar la tarifa general asociada al impuesto de IVA, se debe enviar un porcentaje de 19. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Percent&amp;gt;&lt;/i&gt; | 
**taxable_amount** | **float** | Base Imponible sobre la que se calcula el valor del impuesto. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;TaxableAmount&amp;gt;&lt;/i&gt; | 
**tax_base_unit_measure** | **float** | Unidad de medida base para el tributo. Usado en el caso de que el tributo es un valor fijo por unidad tributada: informar el valor del tributo por unidadtributada. | [optional] 
**tax_per_unit_amount** | **float** | Valor del tributo por unidad. Correspode al valor nominal del tributo por unidad | [optional] 

## Example

```python
from openapi_client.models.tax import Tax

# TODO update the JSON string below
json = "{}"
# create an instance of Tax from a JSON string
tax_instance = Tax.from_json(json)
# print the JSON string representation of the object
print(Tax.to_json())

# convert the object into a dict
tax_dict = tax_instance.to_dict()
# create an instance of Tax from a dict
tax_from_dict = Tax.from_dict(tax_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


