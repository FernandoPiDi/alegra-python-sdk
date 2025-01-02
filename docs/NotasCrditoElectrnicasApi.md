# openapi_client.NotasCrditoElectrnicasApi

All URIs are relative to *https://sandbox-api.alegra.com/e-provider/col/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credit_note**](NotasCrditoElectrnicasApi.md#create_credit_note) | **POST** /credit-notes | Endpoint para emitir una nota crédito electrónica a la DIAN
[**get_credit_note**](NotasCrditoElectrnicasApi.md#get_credit_note) | **GET** /credit-notes/{id} | Endpoint para consultar una nota crédito electrónica
[**get_credit_note_file**](NotasCrditoElectrnicasApi.md#get_credit_note_file) | **GET** /credit-notes/{id}/files/{fileType} | Endpoint para obtener un archivo asociado a la nota crédito electrónica
[**get_credit_notes**](NotasCrditoElectrnicasApi.md#get_credit_notes) | **GET** /credit-notes | Endpoint para consultar notas crédito electrónicas


# **create_credit_note**
> GetCreditNotes200Response create_credit_note(create_credit_note_request)

Endpoint para emitir una nota crédito electrónica a la DIAN

Este endpoint permite emitir una nota crédito electrónica a la DIAN.  Recuerda visitar previamente las guías de [Inicio](https://e-provider-docs.alegra.com/docs/gu%C3%ADa-creaci%C3%B3n-de-una-compa%C3%B1%C3%ADa-asociada) y la guía de [Habilitación en la DIAN - Factura Electronica](https://e-provider-docs.alegra.com/docs/proceso-de-habilitaci%C3%B3n-en-la-dian)

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_credit_note_request import CreateCreditNoteRequest
from openapi_client.models.get_credit_notes200_response import GetCreditNotes200Response
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
    api_instance = openapi_client.NotasCrditoElectrnicasApi(api_client)
    create_credit_note_request = {"prefix":"NC","number":100000001,"conceptCode":"1","note":"Nota relativa al documento","associatedDocuments":[{"date":"2021-06-30","documentType":"01","number":990000564,"prefix":"SETP","uuid":"295fc4d0469f4afdcb02c0b900826314a221500c5ae30bf76054eee64b6093edeebad4a16e35b9e35e5981b21e7bb745"}],"company":{"id":"01FCYA9GSSNT2674KGJV2V0NS9","organizationType":1,"identificationNumber":"900559088","dv":"2","name":"Soluciones Alegra S.A.S","regimeCode":"R-99-PN","email":"email@email.com","address":{"address":"Cra. 13 #12-12 Edificio A & A","city":"11001","department":"11","country":"CO"}},"customer":{"name":"Customer Name","organizationType":2,"identificationType":"13","identificationNumber":"222222222222","dv":"2","email":"","phone":"","address":{"address":"Cra. 13 #12-12 Edificio A & A","city":"11001","department":"11","country":"CO"}},"items":[{"code":"","name":"Botella de M3","description":"This is the ítem de metro cubico M3","price":10000,"discount":0,"discountAmount":0,"quantity":1,"unitCode":"94","subtotal":10000,"taxAmount":1900,"total":11900,"taxes":[{"taxCode":"01","taxAmount":1900,"taxPercentage":"19.00","taxableAmount":10000}]}],"totalAmounts":{"grossTotal":10000,"taxableTotal":10000,"taxTotal":1900,"discountTotal":0,"chargeTotal":0,"advanceTotal":0,"payableTotal":11900,"currencyCode":"COP"},"payments":[{"paymentForm":"1","paymentMethod":"10","paymentDueDate":"2021-08-30"}]} # CreateCreditNoteRequest | Objeto con la información de la nota crédito electrónica

    try:
        # Endpoint para emitir una nota crédito electrónica a la DIAN
        api_response = api_instance.create_credit_note(create_credit_note_request)
        print("The response of NotasCrditoElectrnicasApi->create_credit_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotasCrditoElectrnicasApi->create_credit_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_credit_note_request** | [**CreateCreditNoteRequest**](CreateCreditNoteRequest.md)| Objeto con la información de la nota crédito electrónica | 

### Return type

[**GetCreditNotes200Response**](GetCreditNotes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se consultan las notas crédito electrónicas |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note**
> GetCreditNote200Response get_credit_note(id)

Endpoint para consultar una nota crédito electrónica

Retorna toda la información asociada a la nota crédito electrónica enviada como parámetro

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_credit_note200_response import GetCreditNote200Response
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
    api_instance = openapi_client.NotasCrditoElectrnicasApi(api_client)
    id = 'id_example' # str | Id de la nota crédito electrónica

    try:
        # Endpoint para consultar una nota crédito electrónica
        api_response = api_instance.get_credit_note(id)
        print("The response of NotasCrditoElectrnicasApi->get_credit_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotasCrditoElectrnicasApi->get_credit_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la nota crédito electrónica | 

### Return type

[**GetCreditNote200Response**](GetCreditNote200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía una nota crédito electrónica a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_file**
> GetPayrollFile200Response get_credit_note_file(id, file_type)

Endpoint para obtener un archivo asociado a la nota crédito electrónica

Retorna el archivo asociado a la nota crédito electrónica codificado en base 64

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
    api_instance = openapi_client.NotasCrditoElectrnicasApi(api_client)
    id = 'id_example' # str | Id de la nota crédito electrónica
    file_type = 'file_type_example' # str | Tipo de archivo que se desea obtener

    try:
        # Endpoint para obtener un archivo asociado a la nota crédito electrónica
        api_response = api_instance.get_credit_note_file(id, file_type)
        print("The response of NotasCrditoElectrnicasApi->get_credit_note_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotasCrditoElectrnicasApi->get_credit_note_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la nota crédito electrónica | 
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

# **get_credit_notes**
> GetCreditNotes200Response get_credit_notes(limit=limit, type=type, var_from=var_from, id_company=id_company, prefix=prefix, number=number, status=status, legal_status=legal_status)

Endpoint para consultar notas crédito electrónicas

Este endpoint permite consultar todas las notas crédito electrónicas de una empresa

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_credit_notes200_response import GetCreditNotes200Response
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
    api_instance = openapi_client.NotasCrditoElectrnicasApi(api_client)
    limit = 56 # int | Cantidad de resultados a obtener, por defecto es 50. (optional)
    type = 'type_example' # str | Filtrar documentos por tipo. Este parámetro es opcional, sino se envia este valor, Alegra listará los documentos de tipo 'STANDARD'. (optional)
    var_from = 'var_from_example' # str | Id de la Nota Crédito a partir de la cuál se desea iniciar la consulta. (optional)
    id_company = 'id_company_example' # str | Id de la empresa. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la empresa asociada al token de autenticación (optional)
    prefix = 'prefix_example' # str | Filtrar notas crédito por prefijo (optional)
    number = 'number_example' # str | Filtrar notas crédito por número, para usar este filtro es obligatorio enviar el de prefijo (optional)
    status = 'status_example' # str | Filtrar notas crédito por estado (optional)
    legal_status = 'legal_status_example' # str | Filtrar notas crédito por estado legal (optional)

    try:
        # Endpoint para consultar notas crédito electrónicas
        api_response = api_instance.get_credit_notes(limit=limit, type=type, var_from=var_from, id_company=id_company, prefix=prefix, number=number, status=status, legal_status=legal_status)
        print("The response of NotasCrditoElectrnicasApi->get_credit_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotasCrditoElectrnicasApi->get_credit_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Cantidad de resultados a obtener, por defecto es 50. | [optional] 
 **type** | **str**| Filtrar documentos por tipo. Este parámetro es opcional, sino se envia este valor, Alegra listará los documentos de tipo &#39;STANDARD&#39;. | [optional] 
 **var_from** | **str**| Id de la Nota Crédito a partir de la cuál se desea iniciar la consulta. | [optional] 
 **id_company** | **str**| Id de la empresa. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la empresa asociada al token de autenticación | [optional] 
 **prefix** | **str**| Filtrar notas crédito por prefijo | [optional] 
 **number** | **str**| Filtrar notas crédito por número, para usar este filtro es obligatorio enviar el de prefijo | [optional] 
 **status** | **str**| Filtrar notas crédito por estado | [optional] 
 **legal_status** | **str**| Filtrar notas crédito por estado legal | [optional] 

### Return type

[**GetCreditNotes200Response**](GetCreditNotes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se consultan las notas crédito electrónicas |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

