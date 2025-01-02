# openapi_client.DocumentosSoporteElectrnicosApi

All URIs are relative to *https://sandbox-api.alegra.com/e-provider/col/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjustment_note_support_document_file**](DocumentosSoporteElectrnicosApi.md#adjustment_note_support_document_file) | **GET** /adjustment-note-support-documents/{id}/files/{fileType} | Endpoint para obtener un archivo asociado a la nota de ajuste al documento soporte electrónico
[**create_adjustment_note_support_document**](DocumentosSoporteElectrnicosApi.md#create_adjustment_note_support_document) | **POST** /adjustment-note-support-documents | Endpoint para emitir una nota de ajuste al documento soporte electrónico a la DIAN
[**create_support_document**](DocumentosSoporteElectrnicosApi.md#create_support_document) | **POST** /support-documents | Endpoint para emitir un documento soporte electrónico a la DIAN
[**get_adjustment_note_support_document**](DocumentosSoporteElectrnicosApi.md#get_adjustment_note_support_document) | **GET** /adjustment-note-support-documents/{id} | Endpoint para consultar una nota de ajuste al documento soporte electrónico
[**get_support_document**](DocumentosSoporteElectrnicosApi.md#get_support_document) | **GET** /support-documents/{id} | Endpoint para consultar un documento soporte electrónico
[**get_support_document_file**](DocumentosSoporteElectrnicosApi.md#get_support_document_file) | **GET** /support-documents/{id}/files/{fileType} | Endpoint para obtener un archivo asociado al documento soporte electrónico
[**get_support_documents**](DocumentosSoporteElectrnicosApi.md#get_support_documents) | **GET** /support-documents | Endpoint para consultar documentos soporte electrónicos


# **adjustment_note_support_document_file**
> GetPayrollFile200Response adjustment_note_support_document_file(id, file_type)

Endpoint para obtener un archivo asociado a la nota de ajuste al documento soporte electrónico

Retorna el archivo asociado a la nota de ajuste al documento soporte electrónico codificado en base 64

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
    api_instance = openapi_client.DocumentosSoporteElectrnicosApi(api_client)
    id = 'id_example' # str | Id de la nota de ajuste al documento soporte electrónico
    file_type = 'file_type_example' # str | Tipo de archivo que se desea obtener

    try:
        # Endpoint para obtener un archivo asociado a la nota de ajuste al documento soporte electrónico
        api_response = api_instance.adjustment_note_support_document_file(id, file_type)
        print("The response of DocumentosSoporteElectrnicosApi->adjustment_note_support_document_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentosSoporteElectrnicosApi->adjustment_note_support_document_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la nota de ajuste al documento soporte electrónico | 
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
**200** | Objeto que representa la respuesta que contiene la información de un archivo asociado al documento soporte electrónico |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_adjustment_note_support_document**
> CreateAdjustmentNoteSupportDocument200Response create_adjustment_note_support_document(create_adjustment_note_support_document_request)

Endpoint para emitir una nota de ajuste al documento soporte electrónico a la DIAN

Este endpoint permite emitir una nota de ajuste al documento soporte electrónico a la DIAN. Recuerda visitar previamente las guías de [Inicio](https://e-provider-docs.alegra.com/docs/gu%C3%ADa-creaci%C3%B3n-de-una-compa%C3%B1%C3%ADa-asociada) y la guía de [Habilitación en la DIAN - Documento Soporte Electrónico](https://e-provider-docs.alegra.com/docs/gu%C3%ADa-del-proceso-de-habilitaci%C3%B3n-en-la-dian-documento-soporte-electr%C3%B3nico)

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_adjustment_note_support_document200_response import CreateAdjustmentNoteSupportDocument200Response
from openapi_client.models.create_adjustment_note_support_document_request import CreateAdjustmentNoteSupportDocumentRequest
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
    api_instance = openapi_client.DocumentosSoporteElectrnicosApi(api_client)
    create_adjustment_note_support_document_request = {"number":990015000,"invoiceDocumentReference":{"id":"01FQS9ZGW84DG8C2ZFDZJZGEV2"},"discrepancies":[{"sectionId":"DSBB02","responseCode":4,"description":"Ajuste de precio"}],"note":"nota de ejmplo","company":{"id":"01FCYA9GSSNT2674KGJV2V0NS9","organizationType":1,"identificationType":"31","identificationNumber":"900559088","dv":"2","name":"Soluciones Alegra S.A.S","regimeCode":"R-99-PN","email":"email@email.com","address":{"address":"Cra. 13 #12-12 Edificio A & A","city":"11001","department":"11","country":"CO"}},"prefix":"NAS","supplier":{"name":"Supplier Name","organizationType":2,"identificationType":"31","identificationNumber":"000000000","dv":"1","email":"","phone":"","address":{"address":"Cra. 13 #12-12 Edificio A & A","city":"11001","department":"11","country":"CO"}},"items":[{"code":"","name":"Botella de M3","description":"This is the ítem de metro cubico M3","price":10000,"discount":0,"discountAmount":0,"quantity":1,"unitCode":"94","subtotal":10000,"taxAmount":1900,"total":11900,"taxes":[{"taxCode":"01","taxAmount":1900,"taxPercentage":"19.00","taxableAmount":10000}]}],"totalAmounts":{"grossTotal":10000,"taxableTotal":10000,"taxTotal":1900,"discountTotal":0,"chargeTotal":0,"advanceTotal":0,"payableTotal":11900,"currencyCode":"COP"},"payments":[{"paymentForm":"1","paymentMethod":"10","paymentDueDate":"2021-08-30"}]} # CreateAdjustmentNoteSupportDocumentRequest | Objeto con la información de una nota de ajuste al documento soporte electrónico

    try:
        # Endpoint para emitir una nota de ajuste al documento soporte electrónico a la DIAN
        api_response = api_instance.create_adjustment_note_support_document(create_adjustment_note_support_document_request)
        print("The response of DocumentosSoporteElectrnicosApi->create_adjustment_note_support_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentosSoporteElectrnicosApi->create_adjustment_note_support_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_adjustment_note_support_document_request** | [**CreateAdjustmentNoteSupportDocumentRequest**](CreateAdjustmentNoteSupportDocumentRequest.md)| Objeto con la información de una nota de ajuste al documento soporte electrónico | 

### Return type

[**CreateAdjustmentNoteSupportDocument200Response**](CreateAdjustmentNoteSupportDocument200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía una una nota de ajuste al documento soporte electrónico a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_support_document**
> CreateSupportDocument200Response create_support_document(create_support_document_request)

Endpoint para emitir un documento soporte electrónico a la DIAN

Este endpoint permite emitir un documento soporte electrónico a la DIAN.  Recuerda visitar previamente las guías de [Inicio](https://e-provider-docs.alegra.com/docs/gu%C3%ADa-creaci%C3%B3n-de-una-compa%C3%B1%C3%ADa-asociada) y la guía de [Habilitación en la DIAN - Documento Soporte Electrónico](https://e-provider-docs.alegra.com/docs/gu%C3%ADa-del-proceso-de-habilitaci%C3%B3n-en-la-dian-documento-soporte-electr%C3%B3nico)

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_support_document200_response import CreateSupportDocument200Response
from openapi_client.models.create_support_document_request import CreateSupportDocumentRequest
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
    api_instance = openapi_client.DocumentosSoporteElectrnicosApi(api_client)
    create_support_document_request = {"number":984000001,"resolution":{"resolutionNumber":"18760000002","prefix":"SEDS","minNumber":984000000,"maxNumber":985000000,"startDate":"2022-01-01","endDate":"2022-12-31"},"company":{"id":"01FCYA9GSSNT2674KGJV2V0NS9","organizationType":1,"identificationNumber":"900559088","dv":"2","name":"Soluciones Alegra S.A.S","regimeCode":"R-99-PN","email":"email@email.com","address":{"address":"Cra. 13 #12-12 Edificio A & A","city":"11001","department":"11","country":"CO"}},"supplier":{"name":"Supplier Name","origin":"10","organizationType":2,"identificationType":"31","identificationNumber":"000000000","dv":"1","regimeCode":"R-99-PN","email":"","phone":"","address":{"address":"Cra. 13 #12-12 Edificio A & A","city":"11001","department":"11","country":"CO"}},"items":[{"code":"","name":"Botella de M3","description":"This is the ítem de metro cubico M3","price":10000,"discount":0,"discountAmount":0,"quantity":1,"unitCode":"94","subtotal":10000,"taxAmount":1900,"total":11900,"taxes":[{"taxCode":"01","taxAmount":1900,"taxPercentage":"19.00","taxableAmount":10000}]}],"payments":[{"paymentForm":"1","paymentMethod":"10","paymentDueDate":"2021-08-30"}],"totalAmounts":{"grossTotal":10000,"taxableTotal":10000,"taxTotal":1900,"discountTotal":0,"chargeTotal":0,"advanceTotal":0,"payableTotal":11900,"currencyCode":"COP"}} # CreateSupportDocumentRequest | Objeto con la información del documento soporte electrónico

    try:
        # Endpoint para emitir un documento soporte electrónico a la DIAN
        api_response = api_instance.create_support_document(create_support_document_request)
        print("The response of DocumentosSoporteElectrnicosApi->create_support_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentosSoporteElectrnicosApi->create_support_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_support_document_request** | [**CreateSupportDocumentRequest**](CreateSupportDocumentRequest.md)| Objeto con la información del documento soporte electrónico | 

### Return type

[**CreateSupportDocument200Response**](CreateSupportDocument200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía un documento soporte electrónico a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_adjustment_note_support_document**
> CreateAdjustmentNoteSupportDocument200Response get_adjustment_note_support_document(id)

Endpoint para consultar una nota de ajuste al documento soporte electrónico

Retorna toda la información asociada a la nota de ajuste a un documento soporte electrónico enviado como parámetro

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_adjustment_note_support_document200_response import CreateAdjustmentNoteSupportDocument200Response
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
    api_instance = openapi_client.DocumentosSoporteElectrnicosApi(api_client)
    id = 'id_example' # str | Id de la nota de ajuste a un documento soporte electrónico

    try:
        # Endpoint para consultar una nota de ajuste al documento soporte electrónico
        api_response = api_instance.get_adjustment_note_support_document(id)
        print("The response of DocumentosSoporteElectrnicosApi->get_adjustment_note_support_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentosSoporteElectrnicosApi->get_adjustment_note_support_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la nota de ajuste a un documento soporte electrónico | 

### Return type

[**CreateAdjustmentNoteSupportDocument200Response**](CreateAdjustmentNoteSupportDocument200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía una una nota de ajuste al documento soporte electrónico a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_support_document**
> CreateSupportDocument200Response get_support_document(id)

Endpoint para consultar un documento soporte electrónico

Retorna toda la información asociada al documento soporte electrónico enviado como parámetro

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_support_document200_response import CreateSupportDocument200Response
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
    api_instance = openapi_client.DocumentosSoporteElectrnicosApi(api_client)
    id = 'id_example' # str | Id del documento soporte electrónico

    try:
        # Endpoint para consultar un documento soporte electrónico
        api_response = api_instance.get_support_document(id)
        print("The response of DocumentosSoporteElectrnicosApi->get_support_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentosSoporteElectrnicosApi->get_support_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id del documento soporte electrónico | 

### Return type

[**CreateSupportDocument200Response**](CreateSupportDocument200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía un documento soporte electrónico a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_support_document_file**
> GetPayrollFile200Response get_support_document_file(id, file_type)

Endpoint para obtener un archivo asociado al documento soporte electrónico

Retorna el archivo asociado al documento soporte electrónico codificado en base 64

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
    api_instance = openapi_client.DocumentosSoporteElectrnicosApi(api_client)
    id = 'id_example' # str | Id del documento soporte electrónico
    file_type = 'file_type_example' # str | Tipo de archivo que se desea obtener

    try:
        # Endpoint para obtener un archivo asociado al documento soporte electrónico
        api_response = api_instance.get_support_document_file(id, file_type)
        print("The response of DocumentosSoporteElectrnicosApi->get_support_document_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentosSoporteElectrnicosApi->get_support_document_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id del documento soporte electrónico | 
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
**200** | Objeto que representa la respuesta que contiene la información de un archivo asociado al documento soporte electrónico |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_support_documents**
> GetSupportDocuments200Response get_support_documents(limit=limit, type=type, var_from=var_from, id_company=id_company, prefix=prefix, number=number, status=status, legal_status=legal_status)

Endpoint para consultar documentos soporte electrónicos

Este endpoint permite consultar todos los documentos soporte electrónicas de una empresa

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_support_documents200_response import GetSupportDocuments200Response
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
    api_instance = openapi_client.DocumentosSoporteElectrnicosApi(api_client)
    limit = 56 # int | Cantidad de resultados a obtener, por defecto es 50. (optional)
    type = 'type_example' # str | Filtrar facturas por tipo. Este parámetro es opcional, sino se envia este valor, Alegra listará los documentos de tipo 'STANDARD'. (optional)
    var_from = 'var_from_example' # str | Id del documento a partir del cuál se desea iniciar la consulta. (optional)
    id_company = 'id_company_example' # str | Id de la empresa. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la empresa asociada al token de autenticación (optional)
    prefix = 'prefix_example' # str | Filtrar facturas por prefijo (optional)
    number = 'number_example' # str | Filtrar facturas por número, para usar este filtro es obligatorio enviar el de prefijo (optional)
    status = 'status_example' # str | Filtrar facturas por estado (optional)
    legal_status = 'legal_status_example' # str | Filtrar facturas por estado legal (optional)

    try:
        # Endpoint para consultar documentos soporte electrónicos
        api_response = api_instance.get_support_documents(limit=limit, type=type, var_from=var_from, id_company=id_company, prefix=prefix, number=number, status=status, legal_status=legal_status)
        print("The response of DocumentosSoporteElectrnicosApi->get_support_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentosSoporteElectrnicosApi->get_support_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Cantidad de resultados a obtener, por defecto es 50. | [optional] 
 **type** | **str**| Filtrar facturas por tipo. Este parámetro es opcional, sino se envia este valor, Alegra listará los documentos de tipo &#39;STANDARD&#39;. | [optional] 
 **var_from** | **str**| Id del documento a partir del cuál se desea iniciar la consulta. | [optional] 
 **id_company** | **str**| Id de la empresa. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la empresa asociada al token de autenticación | [optional] 
 **prefix** | **str**| Filtrar facturas por prefijo | [optional] 
 **number** | **str**| Filtrar facturas por número, para usar este filtro es obligatorio enviar el de prefijo | [optional] 
 **status** | **str**| Filtrar facturas por estado | [optional] 
 **legal_status** | **str**| Filtrar facturas por estado legal | [optional] 

### Return type

[**GetSupportDocuments200Response**](GetSupportDocuments200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se consultan los documentos soporte electrónicos |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

