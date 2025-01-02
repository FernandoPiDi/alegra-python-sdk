# openapi_client.FacturasDeVentaElectrnicasApi

All URIs are relative to *https://sandbox-api.alegra.com/e-provider/col/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invoice**](FacturasDeVentaElectrnicasApi.md#create_invoice) | **POST** /invoices | Endpoint para emitir una factura electrónica a la DIAN
[**get_invoice**](FacturasDeVentaElectrnicasApi.md#get_invoice) | **GET** /invoices/{id} | Endpoint para consultar una factura electrónica
[**get_invoice_file**](FacturasDeVentaElectrnicasApi.md#get_invoice_file) | **GET** /invoices/{id}/files/{fileType} | Endpoint para obtener un archivo asociado a la factura electrónica
[**get_invoices**](FacturasDeVentaElectrnicasApi.md#get_invoices) | **GET** /invoices | Endpoint para consultar facturas electrónicas


# **create_invoice**
> CreateInvoice200Response create_invoice(create_invoice_request)

Endpoint para emitir una factura electrónica a la DIAN

Este endpoint permite emitir una factura electrónica a la DIAN.  Recuerda visitar previamente las guías de [Inicio](https://e-provider-docs.alegra.com/docs/gu%C3%ADa-creaci%C3%B3n-de-una-compa%C3%B1%C3%ADa-asociada) y la guía de [Habilitación en la DIAN - Factura Electronica](https://e-provider-docs.alegra.com/docs/proceso-de-habilitaci%C3%B3n-en-la-dian)

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_invoice200_response import CreateInvoice200Response
from openapi_client.models.create_invoice_request import CreateInvoiceRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox-api.alegra.com/e-provider/col/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sandbox-api.alegra.com/e-provider/col/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FacturasDeVentaElectrnicasApi(api_client)
    create_invoice_request = {"documentType":"01","number":990015000,"note":"Nota relativa al documento","resolution":{"resolutionNumber":"18760000001","prefix":"SETP","minNumber":990000000,"maxNumber":995000000,"startDate":"2019-01-19","endDate":"2030-01-19","technicalKey":"fc8eac422eba16e22ffd8c6f94b3f40a6e38162c"},"company":{"id":"01FCYA9GSSNT2674KGJV2V0NS9","organizationType":1,"identificationNumber":"900559088","dv":"2","name":"Soluciones Alegra S.A.S","regimeCode":"R-99-PN","email":"email@email.com","address":{"address":"Cra. 13 #12-12 Edificio A & A","city":"11001","department":"11","country":"CO"}},"customer":{"name":"Customer Name","organizationType":2,"identificationType":"13","identificationNumber":"222222222222","dv":"2","email":"email@email.com","phone":"3223334455","address":{"address":"Cra. 13 #12-12 Edificio A & A","city":"11001","department":"11","country":"CO"}},"items":[{"code":"BM3","standardCode":{"identificationId":"11001","id":"001"},"description":"Botella de M3","price":10000,"discount":0,"discountAmount":0,"quantity":1,"unitCode":"94","subtotal":10000,"taxAmount":1900,"total":11900,"taxes":[{"taxCode":"01","taxAmount":1900,"taxPercentage":"19.00","taxableAmount":10000,"taxBaseUnitMeasure":1,"taxPerUnitAmount":1}]}],"payments":[{"paymentForm":"1","paymentMethod":"10","paymentDueDate":"2021-08-30"}],"totalAmounts":{"grossTotal":10000,"taxableTotal":10000,"taxTotal":1900,"discountTotal":0,"chargeTotal":0,"advanceTotal":0,"payableTotal":11900,"currencyCode":"COP"}} # CreateInvoiceRequest | Objeto con la información de la factura electrónica

    try:
        # Endpoint para emitir una factura electrónica a la DIAN
        api_response = api_instance.create_invoice(create_invoice_request)
        print("The response of FacturasDeVentaElectrnicasApi->create_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FacturasDeVentaElectrnicasApi->create_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_invoice_request** | [**CreateInvoiceRequest**](CreateInvoiceRequest.md)| Objeto con la información de la factura electrónica | 

### Return type

[**CreateInvoice200Response**](CreateInvoice200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía una factura electrónica a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> CreateInvoice200Response get_invoice(id)

Endpoint para consultar una factura electrónica

Retorna toda la información asociada a la factura electrónica enviada como parámetro

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_invoice200_response import CreateInvoice200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox-api.alegra.com/e-provider/col/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sandbox-api.alegra.com/e-provider/col/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FacturasDeVentaElectrnicasApi(api_client)
    id = 'id_example' # str | Id de la factura electrónica

    try:
        # Endpoint para consultar una factura electrónica
        api_response = api_instance.get_invoice(id)
        print("The response of FacturasDeVentaElectrnicasApi->get_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FacturasDeVentaElectrnicasApi->get_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la factura electrónica | 

### Return type

[**CreateInvoice200Response**](CreateInvoice200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía una factura electrónica a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_file**
> GetPayrollFile200Response get_invoice_file(id, file_type)

Endpoint para obtener un archivo asociado a la factura electrónica

Retorna el archivo asociado a la factura electrónica codificado en base 64

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_payroll_file200_response import GetPayrollFile200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox-api.alegra.com/e-provider/col/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sandbox-api.alegra.com/e-provider/col/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FacturasDeVentaElectrnicasApi(api_client)
    id = 'id_example' # str | Id de la factura electrónica
    file_type = 'file_type_example' # str | Tipo de archivo que se desea obtener

    try:
        # Endpoint para obtener un archivo asociado a la factura electrónica
        api_response = api_instance.get_invoice_file(id, file_type)
        print("The response of FacturasDeVentaElectrnicasApi->get_invoice_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FacturasDeVentaElectrnicasApi->get_invoice_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la factura electrónica | 
 **file_type** | **str**| Tipo de archivo que se desea obtener | 

### Return type

[**GetPayrollFile200Response**](GetPayrollFile200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta que contiene la información de un archivo asociado a la factura electrónica |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> GetInvoices200Response get_invoices(limit=limit, type=type, var_from=var_from, id_company=id_company, prefix=prefix, number=number, status=status, legal_status=legal_status)

Endpoint para consultar facturas electrónicas

Este endpoint permite consultar todas las facturas electrónicas de una empresa

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_invoices200_response import GetInvoices200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox-api.alegra.com/e-provider/col/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sandbox-api.alegra.com/e-provider/col/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FacturasDeVentaElectrnicasApi(api_client)
    limit = 56 # int | Cantidad de resultados a obtener, por defecto es 50. (optional)
    type = STANDARD # str | Filtrar facturas por tipo. El valor por defecto es `STANDARD` (optional) (default to STANDARD)
    var_from = 'var_from_example' # str | Id de la factura a partir de la cuál se desea iniciar la consulta. (optional)
    id_company = 'id_company_example' # str | Id de la empresa. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la empresa asociada al token de autenticación (optional)
    prefix = 'prefix_example' # str | Filtrar facturas por prefijo (optional)
    number = 'number_example' # str | Filtrar facturas por número, para usar este filtro es obligatorio enviar el de prefijo (optional)
    status = 'status_example' # str | Filtrar facturas por estado (optional)
    legal_status = 'legal_status_example' # str | Filtrar facturas por estado legal (optional)

    try:
        # Endpoint para consultar facturas electrónicas
        api_response = api_instance.get_invoices(limit=limit, type=type, var_from=var_from, id_company=id_company, prefix=prefix, number=number, status=status, legal_status=legal_status)
        print("The response of FacturasDeVentaElectrnicasApi->get_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FacturasDeVentaElectrnicasApi->get_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Cantidad de resultados a obtener, por defecto es 50. | [optional] 
 **type** | **str**| Filtrar facturas por tipo. El valor por defecto es &#x60;STANDARD&#x60; | [optional] [default to STANDARD]
 **var_from** | **str**| Id de la factura a partir de la cuál se desea iniciar la consulta. | [optional] 
 **id_company** | **str**| Id de la empresa. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la empresa asociada al token de autenticación | [optional] 
 **prefix** | **str**| Filtrar facturas por prefijo | [optional] 
 **number** | **str**| Filtrar facturas por número, para usar este filtro es obligatorio enviar el de prefijo | [optional] 
 **status** | **str**| Filtrar facturas por estado | [optional] 
 **legal_status** | **str**| Filtrar facturas por estado legal | [optional] 

### Return type

[**GetInvoices200Response**](GetInvoices200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se consultan las facturas electrónicas |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

