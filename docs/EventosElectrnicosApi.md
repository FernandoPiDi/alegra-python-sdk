# openapi_client.EventosElectrnicosApi

All URIs are relative to *https://sandbox-api.alegra.com/e-provider/col/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event**](EventosElectrnicosApi.md#create_event) | **POST** /events | Endpoint para emitir un evento relacionado a una factura electrónica
[**create_event_from_xml**](EventosElectrnicosApi.md#create_event_from_xml) | **POST** /events/from-xml | Endpoint para emitir un evento relacionado a una factura electrónica a partir de su AttachedDocument
[**get_event**](EventosElectrnicosApi.md#get_event) | **GET** /events/{id} | Endpoint para consultar la información de un evento por su id
[**get_event_file**](EventosElectrnicosApi.md#get_event_file) | **GET** /events/{id}/files/{fileType} | Endpoint para obtener un archivo asociado a un evento electrónico
[**get_invoice_events**](EventosElectrnicosApi.md#get_invoice_events) | **GET** /events/invoice/{cufe} | Endpoint para consultar los eventos asociados a una factura hasta la fecha


# **create_event**
> CreateEvent200Response create_event(create_event_request)

Endpoint para emitir un evento relacionado a una factura electrónica

Endpoint para emitir un evento relacionado a una factura electrónico a partir de los datos recibidos en la petición

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_event200_response import CreateEvent200Response
from openapi_client.models.create_event_request import CreateEventRequest
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
    api_instance = openapi_client.EventosElectrnicosApi(api_client)
    create_event_request = {"number":"IR01","type":"030","associatedDocument":{"prefix":"ACR","number":"990000564","uuid":"295fc4d0469f4afdcb02c0b900826314a221500c5ae30bf76054eee64b6093edeebad4a16e35b9e35e5981b21e7bb745"},"receiverParty":{"name":"Pruebas Company","identificationNumber":"900373979","identificationType":"31","dv":"5","organizationType":1,"taxCode":"01"},"issuerParty":{"identificationType":"13","identificationNumber":"1289846132","firstName":"Pablo","familyName":"Perez","jobTitle":"Revisor Fiscal","organizationDepartment":"Jurídica"}} # CreateEventRequest | Objeto con la información requerida para el emisión del evento

    try:
        # Endpoint para emitir un evento relacionado a una factura electrónica
        api_response = api_instance.create_event(create_event_request)
        print("The response of EventosElectrnicosApi->create_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventosElectrnicosApi->create_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_event_request** | [**CreateEventRequest**](CreateEventRequest.md)| Objeto con la información requerida para el emisión del evento | 

### Return type

[**CreateEvent200Response**](CreateEvent200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta de la API cuando se emite un evento electronico a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_from_xml**
> CreateEvent200Response create_event_from_xml(create_event_from_xml_request)

Endpoint para emitir un evento relacionado a una factura electrónica a partir de su AttachedDocument

Endpoint para emitir un evento relacionado a una factura electrónica a partir del documento XML AttachedDocument que se genera con la factura, el contenido del XML debe ser enviado en base64 junto con los datos extra requeridos en cada evento

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_event200_response import CreateEvent200Response
from openapi_client.models.create_event_from_xml_request import CreateEventFromXmlRequest
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
    api_instance = openapi_client.EventosElectrnicosApi(api_client)
    create_event_from_xml_request = {"number":"IR01","type":"030","xmlContent":"PEF0dGFjvYXNppzcG....0dHA6Ly93d3cudzMub3JnLzIwMDAvM","issuerParty":{"identificationType":"13","identificationNumber":"1289846132","firstName":"Pablo","familyName":"Perez","jobTitle":"Revisor Fiscal","organizationDepartment":"Jurídica"}} # CreateEventFromXmlRequest | Objeto donde viene el attachedDocument de la factura en base64 y la información extra necesaria para la emisión del evento

    try:
        # Endpoint para emitir un evento relacionado a una factura electrónica a partir de su AttachedDocument
        api_response = api_instance.create_event_from_xml(create_event_from_xml_request)
        print("The response of EventosElectrnicosApi->create_event_from_xml:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventosElectrnicosApi->create_event_from_xml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_event_from_xml_request** | [**CreateEventFromXmlRequest**](CreateEventFromXmlRequest.md)| Objeto donde viene el attachedDocument de la factura en base64 y la información extra necesaria para la emisión del evento | 

### Return type

[**CreateEvent200Response**](CreateEvent200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta de la API cuando se emite un evento electronico a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event**
> CreateEvent200Response get_event(id)

Endpoint para consultar la información de un evento por su id

Endpoint para recibir la información relacionada a un evento electrónico a partir del id del evento enviado en la url

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_event200_response import CreateEvent200Response
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
    api_instance = openapi_client.EventosElectrnicosApi(api_client)
    id = 'id_example' # str | Id del evento al ser emitido

    try:
        # Endpoint para consultar la información de un evento por su id
        api_response = api_instance.get_event(id)
        print("The response of EventosElectrnicosApi->get_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventosElectrnicosApi->get_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id del evento al ser emitido | 

### Return type

[**CreateEvent200Response**](CreateEvent200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta de la API cuando se emite un evento electronico a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_file**
> GetPayrollFile200Response get_event_file(id, file_type)

Endpoint para obtener un archivo asociado a un evento electrónico

Retorna el archivo asociado a un evento electrónico codificado en base 64

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
    api_instance = openapi_client.EventosElectrnicosApi(api_client)
    id = 'id_example' # str | Id del evento electrónico
    file_type = 'file_type_example' # str | Tipo de archivo que se desea obtener

    try:
        # Endpoint para obtener un archivo asociado a un evento electrónico
        api_response = api_instance.get_event_file(id, file_type)
        print("The response of EventosElectrnicosApi->get_event_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventosElectrnicosApi->get_event_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id del evento electrónico | 
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

# **get_invoice_events**
> GetInvoiceEvents200Response get_invoice_events(cufe, xmlbase64=xmlbase64)

Endpoint para consultar los eventos asociados a una factura hasta la fecha

Devuelve un objeto JSON donde se muestra la información relacionada a cada evento asociado

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_invoice_events200_response import GetInvoiceEvents200Response
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
    api_instance = openapi_client.EventosElectrnicosApi(api_client)
    cufe = 'cufe_example' # str | CUFE o UUID de la factura electrónica
    xmlbase64 = 'xmlbase64_example' # str | Indica si se quiere recibir el documento que regresa la dian decodificado en la respuesta (optional)

    try:
        # Endpoint para consultar los eventos asociados a una factura hasta la fecha
        api_response = api_instance.get_invoice_events(cufe, xmlbase64=xmlbase64)
        print("The response of EventosElectrnicosApi->get_invoice_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventosElectrnicosApi->get_invoice_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cufe** | **str**| CUFE o UUID de la factura electrónica | 
 **xmlbase64** | **str**| Indica si se quiere recibir el documento que regresa la dian decodificado en la respuesta | [optional] 

### Return type

[**GetInvoiceEvents200Response**](GetInvoiceEvents200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que muestra las posibles respuestas de la API cuando se consultan los eventos asociados a una factura electrónica |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |
**503** | Objecto que representa una respuesta de error cuando ha ocurrido un error de comunicación con la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

