# openapi_client.DianApi

All URIs are relative to *https://sandbox-api.alegra.com/e-provider/col/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contrat_types**](DianApi.md#get_contrat_types) | **GET** /dian/contract-types | Endpoint para obtener la tabla de la DIAN con los tipos de contratos disponibles
[**get_correction_concept_codes_nc**](DianApi.md#get_correction_concept_codes_nc) | **GET** /dian/correction-concept-codes-nc | Endpoint para obtener la tabla de la DIAN con los tipos de concepto de corrección para notas crédito disponibles
[**get_correction_concept_codes_nd**](DianApi.md#get_correction_concept_codes_nd) | **GET** /dian/correction-concept-codes-nd | Endpoint para obtener la tabla de la DIAN con los tipos de concepto de corrección para notas débito disponibles
[**get_countries**](DianApi.md#get_countries) | **GET** /dian/countries | Endpoint para obtener la tabla de la DIAN con los países disponibles
[**get_currencies**](DianApi.md#get_currencies) | **GET** /dian/currencies | Endpoint para obtener la tabla de la DIAN con las monedas disponibles
[**get_departments**](DianApi.md#get_departments) | **GET** /dian/departments | Endpoint para obtener la tabla de la DIAN con los departamentos disponibles
[**get_employee_sub_types**](DianApi.md#get_employee_sub_types) | **GET** /dian/employee-sub-types | Endpoint para obtener la tabla de la DIAN con los subtipos de empleados disponibles
[**get_employee_types**](DianApi.md#get_employee_types) | **GET** /dian/employee-types | Endpoint para obtener la tabla de la DIAN con los tipos de empleados disponibles
[**get_extra_hour_types**](DianApi.md#get_extra_hour_types) | **GET** /dian/extra-hour-types | Endpoint para obtener la tabla de la DIAN con los tipos de hora extra disponibles
[**get_fiscal_responsability_types**](DianApi.md#get_fiscal_responsability_types) | **GET** /dian/fiscal-Responsability-types | Endpoint para obtener la tabla de la DIAN con los tipos de régimen/responsabilidades fiscales disponibles
[**get_health_benefits_plan_types**](DianApi.md#get_health_benefits_plan_types) | **GET** /dian/health-benefits-plan-types | Endpoint para obtener la tabla de la DIAN con los tipos de cobertura o plan de beneficios (Sector Salud) disponibles
[**get_health_identification_types**](DianApi.md#get_health_identification_types) | **GET** /dian/health-identification-types | Endpoint para obtener la tabla de la DIAN con los tipos de documento de identificación del usuario (Sector Salud) disponibles
[**get_health_payment_methods**](DianApi.md#get_health_payment_methods) | **GET** /dian/health-payment-methods | Endpoint para obtener la tabla de la DIAN con los tipos de modalidades de pago (Sector Salud) disponibles
[**get_health_user_types**](DianApi.md#get_health_user_types) | **GET** /dian/health-user-types | Endpoint para obtener la tabla de la DIAN con los tipos de usuario (Sector Salud) disponibles
[**get_identification_types**](DianApi.md#get_identification_types) | **GET** /dian/identification-types | Endpoint para obtener la tabla de la DIAN con los tipos de identificación disponibles
[**get_inhability_types**](DianApi.md#get_inhability_types) | **GET** /dian/inability-types | Endpoint para obtener la tabla de la DIAN con los tipos de incapacidad disponibles
[**get_languages**](DianApi.md#get_languages) | **GET** /dian/languages | Endpoint para obtener la tabla de la DIAN con los lenguajes disponibles
[**get_municipalities**](DianApi.md#get_municipalities) | **GET** /dian/municipalities | Endpoint para obtener la tabla de la DIAN con los municipios disponibles
[**get_organization_types**](DianApi.md#get_organization_types) | **GET** /dian/organization-types | Endpoint para obtener la tabla de la DIAN con los tipos de organización jurídica disponibles
[**get_payment_forms**](DianApi.md#get_payment_forms) | **GET** /dian/payment-forms | Endpoint para obtener la tabla de la DIAN con las formas de pago disponibles
[**get_payment_methods**](DianApi.md#get_payment_methods) | **GET** /dian/payment-methods | Endpoint para obtener la tabla de la DIAN con los métodos de pago disponibles
[**get_payroll_periods**](DianApi.md#get_payroll_periods) | **GET** /dian/payroll-periods | Endpoint para obtener la tabla de la DIAN con los periodos de nómina disponibles
[**get_tax_types**](DianApi.md#get_tax_types) | **GET** /dian/tax-types | Endpoint para obtener la tabla de la DIAN con los tipos de tributos/impuestos disponibles
[**get_unit_codes**](DianApi.md#get_unit_codes) | **GET** /dian/unit-codes | Endpoint para obtener la tabla de la DIAN con los tipos de unidades de cantidad disponibles


# **get_contrat_types**
> GetIdentificationTypes200Response get_contrat_types()

Endpoint para obtener la tabla de la DIAN con los tipos de contratos disponibles

Este endpoint permite obtener los tipos de contratos disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de contratos disponibles
        api_response = api_instance.get_contrat_types()
        print("The response of DianApi->get_contrat_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_contrat_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_correction_concept_codes_nc**
> GetIdentificationTypes200Response get_correction_concept_codes_nc()

Endpoint para obtener la tabla de la DIAN con los tipos de concepto de corrección para notas crédito disponibles

Este endpoint permite obtener los tipos de concepto de corrección para notas crédito disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de concepto de corrección para notas crédito disponibles
        api_response = api_instance.get_correction_concept_codes_nc()
        print("The response of DianApi->get_correction_concept_codes_nc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_correction_concept_codes_nc: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_correction_concept_codes_nd**
> GetIdentificationTypes200Response get_correction_concept_codes_nd()

Endpoint para obtener la tabla de la DIAN con los tipos de concepto de corrección para notas débito disponibles

Este endpoint permite obtener los tipos de concepto de corrección para notas débito disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de concepto de corrección para notas débito disponibles
        api_response = api_instance.get_correction_concept_codes_nd()
        print("The response of DianApi->get_correction_concept_codes_nd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_correction_concept_codes_nd: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries**
> GetIdentificationTypes200Response get_countries()

Endpoint para obtener la tabla de la DIAN con los países disponibles

Este endpoint permite obtener los países disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los países disponibles
        api_response = api_instance.get_countries()
        print("The response of DianApi->get_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_countries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies**
> GetIdentificationTypes200Response get_currencies()

Endpoint para obtener la tabla de la DIAN con las monedas disponibles

Este endpoint permite obtener las monedas disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con las monedas disponibles
        api_response = api_instance.get_currencies()
        print("The response of DianApi->get_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_currencies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_departments**
> GetIdentificationTypes200Response get_departments()

Endpoint para obtener la tabla de la DIAN con los departamentos disponibles

Este endpoint permite obtener los departamentos disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los departamentos disponibles
        api_response = api_instance.get_departments()
        print("The response of DianApi->get_departments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_departments: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_sub_types**
> GetIdentificationTypes200Response get_employee_sub_types()

Endpoint para obtener la tabla de la DIAN con los subtipos de empleados disponibles

Este endpoint permite obtener los subtipos de empleados disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los subtipos de empleados disponibles
        api_response = api_instance.get_employee_sub_types()
        print("The response of DianApi->get_employee_sub_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_employee_sub_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_types**
> GetIdentificationTypes200Response get_employee_types()

Endpoint para obtener la tabla de la DIAN con los tipos de empleados disponibles

Este endpoint permite obtener los tipos de empleados disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de empleados disponibles
        api_response = api_instance.get_employee_types()
        print("The response of DianApi->get_employee_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_employee_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extra_hour_types**
> GetIdentificationTypes200Response get_extra_hour_types()

Endpoint para obtener la tabla de la DIAN con los tipos de hora extra disponibles

Este endpoint permite obtener los tipos de hora extra disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de hora extra disponibles
        api_response = api_instance.get_extra_hour_types()
        print("The response of DianApi->get_extra_hour_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_extra_hour_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscal_responsability_types**
> GetIdentificationTypes200Response get_fiscal_responsability_types()

Endpoint para obtener la tabla de la DIAN con los tipos de régimen/responsabilidades fiscales disponibles

Este endpoint permite obtener los tipos de régimen/responsabilidades fiscales disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de régimen/responsabilidades fiscales disponibles
        api_response = api_instance.get_fiscal_responsability_types()
        print("The response of DianApi->get_fiscal_responsability_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_fiscal_responsability_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health_benefits_plan_types**
> GetIdentificationTypes200Response get_health_benefits_plan_types()

Endpoint para obtener la tabla de la DIAN con los tipos de cobertura o plan de beneficios (Sector Salud) disponibles

Este endpoint permite obtener los tipos de modalidades de cobertura o plan de beneficios (Sector Salud) disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de cobertura o plan de beneficios (Sector Salud) disponibles
        api_response = api_instance.get_health_benefits_plan_types()
        print("The response of DianApi->get_health_benefits_plan_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_health_benefits_plan_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health_identification_types**
> GetIdentificationTypes200Response get_health_identification_types()

Endpoint para obtener la tabla de la DIAN con los tipos de documento de identificación del usuario (Sector Salud) disponibles

Este endpoint permite obtener los tipos de documento de identificación del usuario (Sector Salud) disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de documento de identificación del usuario (Sector Salud) disponibles
        api_response = api_instance.get_health_identification_types()
        print("The response of DianApi->get_health_identification_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_health_identification_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health_payment_methods**
> GetIdentificationTypes200Response get_health_payment_methods()

Endpoint para obtener la tabla de la DIAN con los tipos de modalidades de pago (Sector Salud) disponibles

Este endpoint permite obtener los tipos de modalidades de pago (Sector Salud) disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de modalidades de pago (Sector Salud) disponibles
        api_response = api_instance.get_health_payment_methods()
        print("The response of DianApi->get_health_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_health_payment_methods: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health_user_types**
> GetIdentificationTypes200Response get_health_user_types()

Endpoint para obtener la tabla de la DIAN con los tipos de usuario (Sector Salud) disponibles

Este endpoint permite obtener los tipos de usuario (Sector Salud) disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de usuario (Sector Salud) disponibles
        api_response = api_instance.get_health_user_types()
        print("The response of DianApi->get_health_user_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_health_user_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identification_types**
> GetIdentificationTypes200Response get_identification_types()

Endpoint para obtener la tabla de la DIAN con los tipos de identificación disponibles

Este endpoint permite obtener los tipos de identificación disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de identificación disponibles
        api_response = api_instance.get_identification_types()
        print("The response of DianApi->get_identification_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_identification_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inhability_types**
> GetIdentificationTypes200Response get_inhability_types()

Endpoint para obtener la tabla de la DIAN con los tipos de incapacidad disponibles

Este endpoint permite obtener los tipos de incapacidad disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de incapacidad disponibles
        api_response = api_instance.get_inhability_types()
        print("The response of DianApi->get_inhability_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_inhability_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_languages**
> GetIdentificationTypes200Response get_languages()

Endpoint para obtener la tabla de la DIAN con los lenguajes disponibles

Este endpoint permite obtener los lenguajes disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los lenguajes disponibles
        api_response = api_instance.get_languages()
        print("The response of DianApi->get_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_languages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_municipalities**
> GetIdentificationTypes200Response get_municipalities()

Endpoint para obtener la tabla de la DIAN con los municipios disponibles

Este endpoint permite obtener los municipios disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los municipios disponibles
        api_response = api_instance.get_municipalities()
        print("The response of DianApi->get_municipalities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_municipalities: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_types**
> GetIdentificationTypes200Response get_organization_types()

Endpoint para obtener la tabla de la DIAN con los tipos de organización jurídica disponibles

Este endpoint permite obtener los tipos de organización jurídica disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de organización jurídica disponibles
        api_response = api_instance.get_organization_types()
        print("The response of DianApi->get_organization_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_organization_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_forms**
> GetIdentificationTypes200Response get_payment_forms()

Endpoint para obtener la tabla de la DIAN con las formas de pago disponibles

Este endpoint permite obtener las formas de pago disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con las formas de pago disponibles
        api_response = api_instance.get_payment_forms()
        print("The response of DianApi->get_payment_forms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_payment_forms: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_methods**
> GetIdentificationTypes200Response get_payment_methods()

Endpoint para obtener la tabla de la DIAN con los métodos de pago disponibles

Este endpoint permite obtener los métodos de pago disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los métodos de pago disponibles
        api_response = api_instance.get_payment_methods()
        print("The response of DianApi->get_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_payment_methods: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payroll_periods**
> GetIdentificationTypes200Response get_payroll_periods()

Endpoint para obtener la tabla de la DIAN con los periodos de nómina disponibles

Este endpoint permite obtener los periodos de nómina disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los periodos de nómina disponibles
        api_response = api_instance.get_payroll_periods()
        print("The response of DianApi->get_payroll_periods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_payroll_periods: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_types**
> GetIdentificationTypes200Response get_tax_types()

Endpoint para obtener la tabla de la DIAN con los tipos de tributos/impuestos disponibles

Este endpoint permite obtener los tipos de tributos/impuestos disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de tributos/impuestos disponibles
        api_response = api_instance.get_tax_types()
        print("The response of DianApi->get_tax_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_tax_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unit_codes**
> GetIdentificationTypes200Response get_unit_codes()

Endpoint para obtener la tabla de la DIAN con los tipos de unidades de cantidad disponibles

Este endpoint permite obtener los tipos de unidades de cantidad disponibles para la DIAN

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response
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
    api_instance = openapi_client.DianApi(api_client)

    try:
        # Endpoint para obtener la tabla de la DIAN con los tipos de unidades de cantidad disponibles
        api_response = api_instance.get_unit_codes()
        print("The response of DianApi->get_unit_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DianApi->get_unit_codes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIdentificationTypes200Response**](GetIdentificationTypes200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respuesta con valores disponibles para la DIAN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

