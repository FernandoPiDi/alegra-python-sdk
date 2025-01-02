# openapi_client.EmpresasApi

All URIs are relative to *https://sandbox-api.alegra.com/e-provider/col/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_company**](EmpresasApi.md#create_company) | **POST** /companies | Endpoint para dar de alta a una empresa
[**get_companies**](EmpresasApi.md#get_companies) | **GET** /companies | Endpoint para consultar el listado de empresas
[**get_company**](EmpresasApi.md#get_company) | **GET** /companies/{id} | Endpoint para consultar la información de una empresa
[**get_self_company**](EmpresasApi.md#get_self_company) | **GET** /company | Endpoint para consultar la información de la empresa asociada al token
[**update_company**](EmpresasApi.md#update_company) | **PATCH** /companies/{id} | Endpoint para actualizar la información de una empresa
[**update_self_company**](EmpresasApi.md#update_self_company) | **PATCH** /company | Endpoint para actualizar la información de la empresa asociada al token


# **create_company**
> CreateCompany200Response create_company(create_company_request)

Endpoint para dar de alta a una empresa

Este endpoint permite dar de alta empresas en la API con las configuraciones necesarias para enviar documentos a la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_company200_response import CreateCompany200Response
from openapi_client.models.create_company_request import CreateCompanyRequest
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
    api_instance = openapi_client.EmpresasApi(api_client)
    create_company_request = {"name":"Soluciones Alegra S.A.S","identification":"11111111","dv":"2","econimicActivities":["0161","0150"],"useAlegraCertificate":"false","certificate":{"name":"certificado digital","extension":"pfx","content":"MIIdAgIBAzCCHMgGCSqGSIb3DQEHAaCCHLkEghy1.....A=","password":"12345"},"webhooks":{"general":{"governmentStatusChanged":{"url":"https://my-webhook-test.com","headers":{"x-api-key":"test-api-key"},"status":"active"}},"payrolls":{"emissionFinished":{"url":"https://my-webhook-test.com","headers":{"x-api-key":"test-api-key"},"status":"active"}},"invoices":{"emissionFinished":{"url":"https://my-webhook-test-fe.com","headers":{"x-api-key":"test-api-key"},"status":"active"}},"creditNotes":{"emissionFinished":{"url":"https://my-webhook-test-nc.com","headers":{"x-api-key":"test-api-key"},"status":"active"}},"debitNotes":{"emissionFinished":{"url":"https://my-webhook-test-nd.com","headers":{"x-api-key":"test-api-key"},"status":"active"}},"equivalentDocuments":{"emissionFinished":{"url":"https://my-webhook-test-de.com","headers":{"x-api-key":"test-api-key"},"status":"active"}},"supportDocuments":{"emissionFinished":{"url":"https://my-webhook-test-de.com","headers":{"x-api-key":"test-api-key"},"status":"active"}}},"organizationType":1,"regimeCode":"R-99-PN","taxCode":{"id":"01"},"email":"email@email.com","address":{"address":"Cra. 13 #12-12 Edificio A & A","city":"11001","department":"11","country":"CO"}} # CreateCompanyRequest | Objeto JSON con la información de la empresa

    try:
        # Endpoint para dar de alta a una empresa
        api_response = api_instance.create_company(create_company_request)
        print("The response of EmpresasApi->create_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmpresasApi->create_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_company_request** | [**CreateCompanyRequest**](CreateCompanyRequest.md)| Objeto JSON con la información de la empresa | 

### Return type

[**CreateCompany200Response**](CreateCompany200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta que contiene la información de una empresa |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_companies**
> GetCompanies200Response get_companies()

Endpoint para consultar el listado de empresas

Retorna el listado de empresas asociadas al token

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_companies200_response import GetCompanies200Response
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
    api_instance = openapi_client.EmpresasApi(api_client)

    try:
        # Endpoint para consultar el listado de empresas
        api_response = api_instance.get_companies()
        print("The response of EmpresasApi->get_companies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmpresasApi->get_companies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetCompanies200Response**](GetCompanies200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se consultan el listado de empresas |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company**
> CreateCompany200Response get_company(id)

Endpoint para consultar la información de una empresa

Retorna la información de la empresa enviada como parámetro

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_company200_response import CreateCompany200Response
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
    api_instance = openapi_client.EmpresasApi(api_client)
    id = 'id_example' # str | Id de la empresa

    try:
        # Endpoint para consultar la información de una empresa
        api_response = api_instance.get_company(id)
        print("The response of EmpresasApi->get_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmpresasApi->get_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la empresa | 

### Return type

[**CreateCompany200Response**](CreateCompany200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta que contiene la información de una empresa |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_company**
> CreateCompany200Response get_self_company()

Endpoint para consultar la información de la empresa asociada al token

Retorna la información de la empresa asociada al token

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_company200_response import CreateCompany200Response
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
    api_instance = openapi_client.EmpresasApi(api_client)

    try:
        # Endpoint para consultar la información de la empresa asociada al token
        api_response = api_instance.get_self_company()
        print("The response of EmpresasApi->get_self_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmpresasApi->get_self_company: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateCompany200Response**](CreateCompany200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta que contiene la información de una empresa |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company**
> CreateCompany200Response update_company(id, update_company_request)

Endpoint para actualizar la información de una empresa

Este endpoint permite actualizar la información de la empresa enviada cómo parámetro, ten en cuenta que únicamente se actualizará la información enviada y por lo tanto no es necesario enviar toda la información de la empresa

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_company200_response import CreateCompany200Response
from openapi_client.models.update_company_request import UpdateCompanyRequest
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
    api_instance = openapi_client.EmpresasApi(api_client)
    id = 'id_example' # str | Id de la empresa
    update_company_request = {"certificate":{"name":"certificado digital 2","extension":"pfx","content":"MIIdAgIBAzCCHMgGCSqGSIb3DQEHAaCCHLkEghy1.....A=","password":"12345"}} # UpdateCompanyRequest | Objeto JSON con la información de la empresa que se desea actualizar

    try:
        # Endpoint para actualizar la información de una empresa
        api_response = api_instance.update_company(id, update_company_request)
        print("The response of EmpresasApi->update_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmpresasApi->update_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la empresa | 
 **update_company_request** | [**UpdateCompanyRequest**](UpdateCompanyRequest.md)| Objeto JSON con la información de la empresa que se desea actualizar | 

### Return type

[**CreateCompany200Response**](CreateCompany200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta que contiene la información de una empresa |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_self_company**
> CreateCompany200Response update_self_company(update_company_request)

Endpoint para actualizar la información de la empresa asociada al token

Este endpoint permite actualizar la información de la empresa asociada al token, ten en cuenta que únicamente se actualizará la información enviada y por lo tanto no es necesario enviar toda la información de la empresa

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_company200_response import CreateCompany200Response
from openapi_client.models.update_company_request import UpdateCompanyRequest
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
    api_instance = openapi_client.EmpresasApi(api_client)
    update_company_request = {"certificate":{"name":"certificado digital 2","extension":"pfx","content":"MIIdAgIBAzCCHMgGCSqGSIb3DQEHAaCCHLkEghy1.....A=","password":"12345"}} # UpdateCompanyRequest | Objeto JSON con la información de la empresa que se desea actualizar

    try:
        # Endpoint para actualizar la información de la empresa asociada al token
        api_response = api_instance.update_self_company(update_company_request)
        print("The response of EmpresasApi->update_self_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmpresasApi->update_self_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_company_request** | [**UpdateCompanyRequest**](UpdateCompanyRequest.md)| Objeto JSON con la información de la empresa que se desea actualizar | 

### Return type

[**CreateCompany200Response**](CreateCompany200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta que contiene la información de una empresa |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

