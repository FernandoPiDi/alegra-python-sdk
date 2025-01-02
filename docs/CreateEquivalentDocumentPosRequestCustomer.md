# CreateEquivalentDocumentPosRequestCustomer

Objeto que contiene la información del adquiriente del documento electrónico. Si el cliente no requiere el documento a su nombre no se deberá enviar el grupo y se emitirá al Consumidor Final. Si se requiere que el documento POS electrónico salga a su nombre se deberán enviar los datos marcados como obligatorios. <br><i>Grupo de información oficial DIAN &lt;AccountingCustomerParty&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre del adquiriente. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Name&amp;gt;&lt;/i&gt; | 
**organization_type** | **float** | Identificador de tipo de organización jurídica de la persona o adquiriente. Se debe colocar el Código que corresponda de la tabla de tipos de organización jurídica de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;AdditionalAccountID&amp;gt;&lt;/i&gt; | [optional] 
**identification_type** | **str** | Tipo de documento de identificación del adquiriente. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;@schemeName&amp;gt;&lt;/i&gt; | 
**identification_number** | **str** | Número de identificación del adquiriente. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**dv** | **str** | DV del NIT del adquiriente. Es obligatorio si identificationType &#x3D; 31. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;@schemeID&amp;gt;&lt;/i&gt; | [optional] 
**regime_code** | **str** | Régimen o tipo de obligación o responsabilidad del adquiriente. Se debe colocar el Código que corresponda de la tabla de tipos de régimen/responsabilidades fiscales de la DIAN. Para reportar varias obligaciones / responsabilidades, se deben reportar separando cada uno de los valores de la lista con &#39;;&#39;. Ejemplo O‐13;O‐15; &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;TaxLevelCode&amp;gt;&lt;/i&gt; | [optional] 
**tax_code** | [**CreateEquivalentDocumentPosRequestCustomerTaxCode**](CreateEquivalentDocumentPosRequestCustomerTaxCode.md) |  | [optional] 
**trade_name** | **str** | Nombre Comercial del adquiriente. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PartyName/Name&amp;gt;&lt;/i&gt; | [optional] 
**email** | **str** | Correo electrónico. El correo de notificación será enviado a esta dirección en caso de tener habilitado notificationByEmail en Compañía. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ElectronicMail&amp;gt;&lt;/i&gt; | [optional] 
**phone** | **str** | Número de teléfono, celular u otro. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Telephone&amp;gt;&lt;/i&gt; | [optional] 
**address** | [**GetCompanies200ResponseCompaniesInnerAddress**](GetCompanies200ResponseCompaniesInnerAddress.md) |  | [optional] 
**contact** | [**CreateEquivalentDocumentPosRequestCustomerContact**](CreateEquivalentDocumentPosRequestCustomerContact.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_equivalent_document_pos_request_customer import CreateEquivalentDocumentPosRequestCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEquivalentDocumentPosRequestCustomer from a JSON string
create_equivalent_document_pos_request_customer_instance = CreateEquivalentDocumentPosRequestCustomer.from_json(json)
# print the JSON string representation of the object
print(CreateEquivalentDocumentPosRequestCustomer.to_json())

# convert the object into a dict
create_equivalent_document_pos_request_customer_dict = create_equivalent_document_pos_request_customer_instance.to_dict()
# create an instance of CreateEquivalentDocumentPosRequestCustomer from a dict
create_equivalent_document_pos_request_customer_from_dict = CreateEquivalentDocumentPosRequestCustomer.from_dict(create_equivalent_document_pos_request_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


