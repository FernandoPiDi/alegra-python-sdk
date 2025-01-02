# openapi_client.SetsDePruebasApi

All URIs are relative to *https://sandbox-api.alegra.com/e-provider/col/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_test_set**](SetsDePruebasApi.md#create_test_set) | **POST** /test-sets | Endpoint para crear un set de pruebas
[**get_test_set**](SetsDePruebasApi.md#get_test_set) | **GET** /test-sets/{id} | Endpoint para consultar la información de un set de pruebas
[**get_test_set_by_government_id**](SetsDePruebasApi.md#get_test_set_by_government_id) | **GET** /test-sets | Endpoint para consultar un set de pruebas por governmentId


# **create_test_set**
> CreateTestSet200Response create_test_set(create_test_set_request)

Endpoint para crear un set de pruebas

Este endpoint permite crear un set de pruebas y lo envia automaticamente a la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_test_set200_response import CreateTestSet200Response
from openapi_client.models.create_test_set_request import CreateTestSetRequest
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
    api_instance = openapi_client.SetsDePruebasApi(api_client)
    create_test_set_request = {"company":{"id":"01FQS9ZGW84DG8C2ZFDZJZGEV2"},"type":"payrolls","governmentId":"a70562e0-631e-4ceb-aa65-36887b57dc17"} # CreateTestSetRequest | Objeto JSON con la información del set

    try:
        # Endpoint para crear un set de pruebas
        api_response = api_instance.create_test_set(create_test_set_request)
        print("The response of SetsDePruebasApi->create_test_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetsDePruebasApi->create_test_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_test_set_request** | [**CreateTestSetRequest**](CreateTestSetRequest.md)| Objeto JSON con la información del set | 

### Return type

[**CreateTestSet200Response**](CreateTestSet200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta que contiene la información de un set de pruebas |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_set**
> GetTestSet200Response get_test_set(id)

Endpoint para consultar la información de un set de pruebas

Retorna la información del set de pruebas enviado como parámetro

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_test_set200_response import GetTestSet200Response
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
    api_instance = openapi_client.SetsDePruebasApi(api_client)
    id = 'id_example' # str | Id del set de pruebas

    try:
        # Endpoint para consultar la información de un set de pruebas
        api_response = api_instance.get_test_set(id)
        print("The response of SetsDePruebasApi->get_test_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetsDePruebasApi->get_test_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id del set de pruebas | 

### Return type

[**GetTestSet200Response**](GetTestSet200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta que contiene la información de un set de pruebas |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_set_by_government_id**
> GetTestSetByGovernmentId200Response get_test_set_by_government_id(type, government_id, id_company=id_company)

Endpoint para consultar un set de pruebas por governmentId

Retorna toda la información asociada al set de pruebas

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_test_set_by_government_id200_response import GetTestSetByGovernmentId200Response
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
    api_instance = openapi_client.SetsDePruebasApi(api_client)
    type = 'type_example' # str | Tipo de set de pruebas
    government_id = 'government_id_example' # str | Identificador del set de pruebas (TestSetld)
    id_company = 'id_company_example' # str | Id de la compañía asociada al set de pruebas. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la compañía asociada al token de autenticación (optional)

    try:
        # Endpoint para consultar un set de pruebas por governmentId
        api_response = api_instance.get_test_set_by_government_id(type, government_id, id_company=id_company)
        print("The response of SetsDePruebasApi->get_test_set_by_government_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetsDePruebasApi->get_test_set_by_government_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Tipo de set de pruebas | 
 **government_id** | **str**| Identificador del set de pruebas (TestSetld) | 
 **id_company** | **str**| Id de la compañía asociada al set de pruebas. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la compañía asociada al token de autenticación | [optional] 

### Return type

[**GetTestSetByGovernmentId200Response**](GetTestSetByGovernmentId200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía una nómina electrónica a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

