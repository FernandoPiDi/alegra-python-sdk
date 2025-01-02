# openapi_client.ReportsApi

All URIs are relative to *https://sandbox-api.alegra.com/e-provider/col/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_daily_document_report**](ReportsApi.md#get_daily_document_report) | **GET** /reports/daily | Endpoint para obtener un reporte de emisiones por día


# **get_daily_document_report**
> GetDailyDocumentReport200Response get_daily_document_report(var_date, type)

Endpoint para obtener un reporte de emisiones por día

Devuelve la URL de descarga del reporte diario de emisiones de un tipo de documento para la empresa asociado al token del usuario, en formato `CSV`.

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_daily_document_report200_response import GetDailyDocumentReport200Response
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
    api_instance = openapi_client.ReportsApi(api_client)
    var_date = '2024-10-01' # date | Fecha la cual se quiere obtener el reporte
    type = 'invoice' # str | Tipo de documento a consultar

    try:
        # Endpoint para obtener un reporte de emisiones por día
        api_response = api_instance.get_daily_document_report(var_date, type)
        print("The response of ReportsApi->get_daily_document_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_daily_document_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**| Fecha la cual se quiere obtener el reporte | 
 **type** | **str**| Tipo de documento a consultar | 

### Return type

[**GetDailyDocumentReport200Response**](GetDailyDocumentReport200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta de un reporte diario |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

