# CreateInvoiceRequestCustomer

Objeto que contiene la información del adquiriente del documento electrónico. <br><i>Grupo de información oficial DIAN &lt;AccountingCustomerParty&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre del adquiriente. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Name&amp;gt;&lt;/i&gt; | 
**trade_name** | **str** | NoOpcional si desea agregar el nombre comercial del cliente en la representación gráfica del documento. El nombre del adquiriente persona física y la razón social del adquiriente persona jurídica deben ser informados en el elemento **name**. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Name del grupo PartyName&amp;gt;&lt;/i&gt; | [optional] 
**organization_type** | **float** | Identificador de tipo de organización jurídica del adquiriente, puede ser una de las siguientes opciones: &#x60;1&#x60; Persona Jurídica y asimiladas; &#x60;2&#x60; Persona Natural y asimiladas. Default: &#x60;2&#x60;. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;AdditionalAccountID&amp;gt;&lt;/i&gt; | [optional] 
**identification_type** | **str** | Tipo de documento de identificación del adquiriente. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;@schemeName&amp;gt;&lt;/i&gt; | 
**identification_number** | **str** | Número de identificación del adquiriente. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**dv** | **str** | DV del NIT del adquiriente. Es obligatorio si identificationType &#x3D; 31. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;@schemeID&amp;gt;&lt;/i&gt; | [optional] 
**regime_code** | **str** | Obligaciones o responsabilidades tributarias del adquiriente. El elemento acepta las siguientes opciones: &#x60;O-13&#x60; Gran contribuyente; &#x60;O-15&#x60; Autorretenedor; &#x60;O-23&#x60; Agente de retención IVA; &#x60;O-47&#x60; Régimen simple de tributación; &#x60;R-99-PN&#x60; No aplica – Otros. Para reportar varias obligaciones / responsabilidades se deben separar los valores con &#39;;&#39;. Ejemplo O‐13;O‐15; &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;TaxLevelCode&amp;gt;&lt;/i&gt; | [optional] 
**tax_code** | [**CreateInvoiceRequestCustomerTaxCode**](CreateInvoiceRequestCustomerTaxCode.md) |  | [optional] 
**commercial_registration_number** | **str** | Número de matrícula mercantil del adquiriente. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;CorporateRegistrationScheme/Name&amp;gt;&lt;/i&gt; | [optional] 
**email** | **str** | Correo electrónico. El correo de notificación será enviado a esta dirección en caso de tener habilitado notificationByEmail en Compañía. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ElectronicMail&amp;gt;&lt;/i&gt; | [optional] 
**phone** | **str** | Número de teléfono, celular u otro. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Telephone&amp;gt;&lt;/i&gt; | [optional] 
**address** | [**CreateInvoiceRequestCustomerAddress**](CreateInvoiceRequestCustomerAddress.md) |  | [optional] 
**tax_address** | **object** | Objeto que contiene la información con respeto a la dirección fiscal del adquiriente. Esta información es opcional y se utiliza cuando desea enviar la dirección fiscal registrada en el RUT del cliente. &lt;br&gt;&lt;i&gt;Grupo de información oficial DIAN &amp;lt;RegistrationAddress&amp;gt;&lt;/i&gt; | [optional] 
**contact** | [**CreateInvoiceRequestCustomerContact**](CreateInvoiceRequestCustomerContact.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_invoice_request_customer import CreateInvoiceRequestCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestCustomer from a JSON string
create_invoice_request_customer_instance = CreateInvoiceRequestCustomer.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestCustomer.to_json())

# convert the object into a dict
create_invoice_request_customer_dict = create_invoice_request_customer_instance.to_dict()
# create an instance of CreateInvoiceRequestCustomer from a dict
create_invoice_request_customer_from_dict = CreateInvoiceRequestCustomer.from_dict(create_invoice_request_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


