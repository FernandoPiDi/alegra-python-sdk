# CreateEquivalentDocumentPosRequestCashRegister


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plate** | **str** | Corresponde a la placa de inventario de la caja | 
**location** | **str** | Corresponde a la ubicación de la caja. ALMACEN | 
**cashier** | **str** | Corresponde los nombres y apellidos del cajero o vendedor | 
**type** | **str** | Corresponde al tipo de caja | 
**sale_code** | **str** | Corresponde al código de la venta | 
**subtotal** | **str** | Corresponde al subtotal de la venta | 

## Example

```python
from openapi_client.models.create_equivalent_document_pos_request_cash_register import CreateEquivalentDocumentPosRequestCashRegister

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEquivalentDocumentPosRequestCashRegister from a JSON string
create_equivalent_document_pos_request_cash_register_instance = CreateEquivalentDocumentPosRequestCashRegister.from_json(json)
# print the JSON string representation of the object
print(CreateEquivalentDocumentPosRequestCashRegister.to_json())

# convert the object into a dict
create_equivalent_document_pos_request_cash_register_dict = create_equivalent_document_pos_request_cash_register_instance.to_dict()
# create an instance of CreateEquivalentDocumentPosRequestCashRegister from a dict
create_equivalent_document_pos_request_cash_register_from_dict = CreateEquivalentDocumentPosRequestCashRegister.from_dict(create_equivalent_document_pos_request_cash_register_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


