# CreateEquivalentDocumentPosRequestBuyerBenefits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identification** | **str** | Código o documento de identificación del comprador | 
**name** | **str** | Nombre y apellidos del comprador | 
**points** | **str** | Corresponde a un valor donde se informe la Cantidad de Puntos acumulados por el comprador | 

## Example

```python
from openapi_client.models.create_equivalent_document_pos_request_buyer_benefits import CreateEquivalentDocumentPosRequestBuyerBenefits

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEquivalentDocumentPosRequestBuyerBenefits from a JSON string
create_equivalent_document_pos_request_buyer_benefits_instance = CreateEquivalentDocumentPosRequestBuyerBenefits.from_json(json)
# print the JSON string representation of the object
print(CreateEquivalentDocumentPosRequestBuyerBenefits.to_json())

# convert the object into a dict
create_equivalent_document_pos_request_buyer_benefits_dict = create_equivalent_document_pos_request_buyer_benefits_instance.to_dict()
# create an instance of CreateEquivalentDocumentPosRequestBuyerBenefits from a dict
create_equivalent_document_pos_request_buyer_benefits_from_dict = CreateEquivalentDocumentPosRequestBuyerBenefits.from_dict(create_equivalent_document_pos_request_buyer_benefits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


