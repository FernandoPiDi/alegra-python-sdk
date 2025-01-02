# CreateInvoiceRequestItemsInnerAllOfThirdPartyInformation

Objeto que contiene la información que describen el mandante/tercero de la operación de venta. Aplica solo para mandatos, y se debe informar a nivel de ítem. Tipo de documento de identificación del mandante/tercero. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN. <br><i>Grupo de información oficial DIAN &lt;InformationContentProviderParty&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identification_type** | **str** | Tipo de documento de identificación del mandante/tercero. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PartyIdentification&amp;gt;&lt;/i&gt; | 
**identification_number** | **str** | Número de identificación del mandante/tercero. Tipo de documento de identificación del mandante/tercero. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PartyIdentification&amp;gt;&lt;/i&gt; | 
**dv** | **str** | DV del NIT del mandante/tercero. Tipo de documento de identificación del mandante/tercero. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PartyIdentification&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_invoice_request_items_inner_all_of_third_party_information import CreateInvoiceRequestItemsInnerAllOfThirdPartyInformation

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestItemsInnerAllOfThirdPartyInformation from a JSON string
create_invoice_request_items_inner_all_of_third_party_information_instance = CreateInvoiceRequestItemsInnerAllOfThirdPartyInformation.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestItemsInnerAllOfThirdPartyInformation.to_json())

# convert the object into a dict
create_invoice_request_items_inner_all_of_third_party_information_dict = create_invoice_request_items_inner_all_of_third_party_information_instance.to_dict()
# create an instance of CreateInvoiceRequestItemsInnerAllOfThirdPartyInformation from a dict
create_invoice_request_items_inner_all_of_third_party_information_from_dict = CreateInvoiceRequestItemsInnerAllOfThirdPartyInformation.from_dict(create_invoice_request_items_inner_all_of_third_party_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


