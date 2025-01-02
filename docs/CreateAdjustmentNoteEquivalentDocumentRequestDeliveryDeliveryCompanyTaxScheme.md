# CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxScheme

Información fiscal/legal de la empresa de envíos

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre registrado en el RUT. Si el transportador es persona jurídica desea también utilizar el nombre comercial en el archivo de la factura | [optional] 
**code** | **str** | Código de TaxSchema. Ver tabla de la DIAN. | [optional] 
**identification** | **str** | NIT del transportador | [optional] 
**identification_type** | **str** | Tipo de documento de identificación del Transportador. Se debe colocar el Código que corresponda a la tabla de tipos de identificación de la DIAN | [optional] 
**dv** | **str** | DV del NIT del transportador | [optional] 
**address** | [**CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxSchemeAddress**](CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxSchemeAddress.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_adjustment_note_equivalent_document_request_delivery_delivery_company_tax_scheme import CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxScheme

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxScheme from a JSON string
create_adjustment_note_equivalent_document_request_delivery_delivery_company_tax_scheme_instance = CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxScheme.from_json(json)
# print the JSON string representation of the object
print(CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxScheme.to_json())

# convert the object into a dict
create_adjustment_note_equivalent_document_request_delivery_delivery_company_tax_scheme_dict = create_adjustment_note_equivalent_document_request_delivery_delivery_company_tax_scheme_instance.to_dict()
# create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxScheme from a dict
create_adjustment_note_equivalent_document_request_delivery_delivery_company_tax_scheme_from_dict = CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxScheme.from_dict(create_adjustment_note_equivalent_document_request_delivery_delivery_company_tax_scheme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


