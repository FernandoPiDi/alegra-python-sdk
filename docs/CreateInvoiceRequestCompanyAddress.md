# CreateInvoiceRequestCompanyAddress

Objeto que contiene la información con respeto a la dirección del lugar físico donde se expidió el documento. Si no se envía el objeto 'taxAddress', la información de este objeto se usará también para 'taxAddress' por defecto. <br><i>Grupo de información oficial DIAN &lt;PhysicalLocation&gt;</i>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Dirección del lugar fisico. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;Line&amp;gt;&lt;/i&gt; | 
**city** | **str** | Código de la Ciudad. Se debe colocar el Código que corresponda de la tabla de municipios disponibles de la DIAN. Se debe informar cuando el código del País es &#39;CO&#39;. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;ID&amp;gt;&lt;/i&gt; | 
**department** | **str** | Código del Departamento. Se debe colocar el Código que corresponda de la tabla de departamentos disponibles de la DIAN. Se debe informar cuando el código del País es &#39;CO&#39;. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;CountrySubentityCode&amp;gt;&lt;/i&gt; | 
**postal_code** | **str** | Código Postal del lugar físico del proveedor. &lt;br&gt;&lt;i&gt;Campo oficial DIAN &amp;lt;PostalZone&amp;gt;&lt;/i&gt; | [optional] 

## Example

```python
from openapi_client.models.create_invoice_request_company_address import CreateInvoiceRequestCompanyAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestCompanyAddress from a JSON string
create_invoice_request_company_address_instance = CreateInvoiceRequestCompanyAddress.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestCompanyAddress.to_json())

# convert the object into a dict
create_invoice_request_company_address_dict = create_invoice_request_company_address_instance.to_dict()
# create an instance of CreateInvoiceRequestCompanyAddress from a dict
create_invoice_request_company_address_from_dict = CreateInvoiceRequestCompanyAddress.from_dict(create_invoice_request_company_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


