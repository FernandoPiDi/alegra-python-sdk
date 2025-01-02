# openapi_client.EnvioCorreoElectrnicoApi

All URIs are relative to *https://sandbox-api.alegra.com/e-provider/col/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_email_post**](EnvioCorreoElectrnicoApi.md#send_email_post) | **POST** /send-email | Endpoint para enviar una notificación de un documento electrónico por correo


# **send_email_post**
> SendEmailPost200Response send_email_post(send_email_post_request)

Endpoint para enviar una notificación de un documento electrónico por correo

Este endpoint permite enviar un correo electrónico notificando la emisión de un documento electrónico aceptado por la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.send_email_post200_response import SendEmailPost200Response
from openapi_client.models.send_email_post_request import SendEmailPostRequest
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
    api_instance = openapi_client.EnvioCorreoElectrnicoApi(api_client)
    send_email_post_request = {"documentType":"01","documentId":"01GB3VA2YSYFASDL72143JKMHVA","email":{"to":"testing@email.com","replyTo":"testing@email.com"}} # SendEmailPostRequest | Información que permite identificar el documento y la información relacionada al envio del correo

    try:
        # Endpoint para enviar una notificación de un documento electrónico por correo
        api_response = api_instance.send_email_post(send_email_post_request)
        print("The response of EnvioCorreoElectrnicoApi->send_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvioCorreoElectrnicoApi->send_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_email_post_request** | [**SendEmailPostRequest**](SendEmailPostRequest.md)| Información que permite identificar el documento y la información relacionada al envio del correo | 

### Return type

[**SendEmailPost200Response**](SendEmailPost200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se ha emitido un email |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

