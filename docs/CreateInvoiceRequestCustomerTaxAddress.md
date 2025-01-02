# CreateInvoiceRequestCustomerTaxAddress

Objeto que contiene la información con respeto a la dirección fiscal del adquiriente. Esta información es opcional y se utiliza cuando desea enviar la dirección fiscal registrada en el RUT del cliente. <br><i>Grupo de información oficial DIAN &lt;RegistrationAddress&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Dirección del lugar fisico. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Line&amp;gt;&lt;/i&gt; | 
**city** | **str** | Código de la Ciudad. Se debe colocar el Código que corresponda de la tabla de municipios disponibles de la DIAN. Se debe informar cuando el código del País es &#39;CO&#39;. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**department** | **str** | Código del Departamento. Se debe colocar el Código que corresponda de la tabla de departamentos disponibles de la DIAN. Se debe informar cuando el código del País es &#39;CO&#39;. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;CountrySubentityCode&amp;gt;&lt;/i&gt; | 
**postal_code** | **str** | Código Postal del lugar físico del proveedor. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PostalZone&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_invoice_request_customer_tax_address import CreateInvoiceRequestCustomerTaxAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestCustomerTaxAddress from a JSON string
create_invoice_request_customer_tax_address_instance = CreateInvoiceRequestCustomerTaxAddress.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestCustomerTaxAddress.to_json())

# convert the object into a dict
create_invoice_request_customer_tax_address_dict = create_invoice_request_customer_tax_address_instance.to_dict()
# create an instance of CreateInvoiceRequestCustomerTaxAddress from a dict
create_invoice_request_customer_tax_address_from_dict = CreateInvoiceRequestCustomerTaxAddress.from_dict(create_invoice_request_customer_tax_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


