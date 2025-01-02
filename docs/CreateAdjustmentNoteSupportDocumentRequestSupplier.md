# CreateAdjustmentNoteSupportDocumentRequestSupplier

Objeto que contiene la información del proveedor del documento electrónico

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre del proveedor | 
**origin** | **str** | Indicador de procedencia del vendedor (Residente fiscal en Colombia [&#x60;10&#x60;] o No residente fiscal [&#x60;11&#x60;]). Se debe colocar el Código que corresponda de la tabla de tipos de procedencia del vendedor de la DIAN | [optional] 
**organization_type** | **float** | Tipo de organización jurídica. Se debe colocar el Código que corresponda de la tabla de tipos de organización jurídica de la DIAN | 
**identification_type** | **str** | Tipo de documento de identificación del proveedor. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN | 
**identification_number** | **str** | Número de indentificación del proveedor | 
**dv** | **str** | DV del NIT del proveedor. Es obligatorio si identificationType &#x3D; 31 | [optional] 
**regime_code** | **str** | Régimen al que pertenece el proveedor. Se debe colocar el Código que corresponda de la tabla de tipos de régimen/responsabilidades fiscales de la DIAN. Para reportar varias obligaciones / responsabilidades, se deben reportar separando cada uno de los valores de la lista con &#39;;&#39;. Ejemplo O‐13;O‐15; | [optional] 
**tax_code** | **str** | Identificador del tributo. Se debe colocar el Código que corresponda de la tabla de tipos de tributos de la DIAN. Valores posibles: &#x60;ZZ&#x60;: &#39;No Aplica&#39;(&lt;i&gt;Valor default&lt;/i&gt;), &#x60;01&#x60;: IVA. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;TaxScheme&amp;gt;&lt;/i&gt; | [optional] 
**address** | [**CreateAdjustmentNoteSupportDocumentRequestSupplierAddress**](CreateAdjustmentNoteSupportDocumentRequestSupplierAddress.md) |  | 

## Example

```python
from openapi_client.models.create_adjustment_note_support_document_request_supplier import CreateAdjustmentNoteSupportDocumentRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteSupportDocumentRequestSupplier from a JSON string
create_adjustment_note_support_document_request_supplier_instance = CreateAdjustmentNoteSupportDocumentRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteSupportDocumentRequestSupplier.to_json())

# convert the object into a dict
create_adjustment_note_support_document_request_supplier_dict = create_adjustment_note_support_document_request_supplier_instance.to_dict()
# create an instance of CreateAdjustmentNoteSupportDocumentRequestSupplier from a dict
create_adjustment_note_support_document_request_supplier_from_dict = CreateAdjustmentNoteSupportDocumentRequestSupplier.from_dict(create_adjustment_note_support_document_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


