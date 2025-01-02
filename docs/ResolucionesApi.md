# openapi_client.ResolucionesApi

All URIs are relative to *https://sandbox-api.alegra.com/e-provider/col/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resolutions**](ResolucionesApi.md#get_resolutions) | **GET** /resolutions/{nit} | Endpoint para la consulta de Rangos de Numeración registrados en la DIAN (Resoluciones)


# **get_resolutions**
> GetResolutions200Response get_resolutions(nit)

Endpoint para la consulta de Rangos de Numeración registrados en la DIAN (Resoluciones)

Retorna la información relacionada a los Rangos de Numeración registrada en la DIAN por compañía. Este endpoint solo esta habilitado en ambiente de producción (Production Server).

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_resolutions200_response import GetResolutions200Response
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
    api_instance = openapi_client.ResolucionesApi(api_client)
    nit = 'nit_example' # str | Nit de la empresa

    try:
        # Endpoint para la consulta de Rangos de Numeración registrados en la DIAN (Resoluciones)
        api_response = api_instance.get_resolutions(nit)
        print("The response of ResolucionesApi->get_resolutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolucionesApi->get_resolutions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nit** | **str**| Nit de la empresa | 

### Return type

[**GetResolutions200Response**](GetResolutions200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta que contiene la información de las Resoluciónes o Rangos de Numeración |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

