# openapi_client.CorreosRecepcinApi

All URIs are relative to *https://sandbox-api.alegra.com/e-provider/col/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reception_emails**](CorreosRecepcinApi.md#get_reception_emails) | **GET** /reception-emails/{nit} | Endpoint para la consulta del correo electrónico registrado por el facturador para la recepción de facturas electrónicas


# **get_reception_emails**
> GetReceptionEmails200Response get_reception_emails(nit)

Endpoint para la consulta del correo electrónico registrado por el facturador para la recepción de facturas electrónicas

Retorna la información relacionada al correo electrónico registrado por el facturador para la recepción de facturas electrónicas

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_reception_emails200_response import GetReceptionEmails200Response
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
    api_instance = openapi_client.CorreosRecepcinApi(api_client)
    nit = 'nit_example' # str | Nit de la empresa

    try:
        # Endpoint para la consulta del correo electrónico registrado por el facturador para la recepción de facturas electrónicas
        api_response = api_instance.get_reception_emails(nit)
        print("The response of CorreosRecepcinApi->get_reception_emails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorreosRecepcinApi->get_reception_emails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nit** | **str**| Nit de la empresa | 

### Return type

[**GetReceptionEmails200Response**](GetReceptionEmails200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta que contiene la información del correo electrónico registrado para la recepción de facturas electrónicas |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

