# openapi_client.NminasElectrnicasApi

All URIs are relative to *https://sandbox-api.alegra.com/e-provider/col/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_payroll**](NminasElectrnicasApi.md#adjust_payroll) | **POST** /payrolls/{id}/replace | Endpoint para reemplazar/ajustar una nómina electrónica
[**cancel_payroll**](NminasElectrnicasApi.md#cancel_payroll) | **POST** /payrolls/{id}/cancel | Endpoint para anular una nómina electrónica
[**create_payroll**](NminasElectrnicasApi.md#create_payroll) | **POST** /payrolls | Endpoint para emitir una nómina a la DIAN
[**get_payroll**](NminasElectrnicasApi.md#get_payroll) | **GET** /payrolls/{id} | Endpoint para consultar una nómina electrónica
[**get_payroll_adjustments**](NminasElectrnicasApi.md#get_payroll_adjustments) | **GET** /payroll-adjustments | Endpoint para consultar ajustes de nóminas electrónicas
[**get_payroll_cancellations**](NminasElectrnicasApi.md#get_payroll_cancellations) | **GET** /payroll-cancellations | Endpoint para consultar cancelaciones de nóminas electrónicas
[**get_payroll_file**](NminasElectrnicasApi.md#get_payroll_file) | **GET** /payrolls/{id}/files/{fileType} | Endpoint para obtener un archivo asociado a la nómina electrónica
[**get_payrolls**](NminasElectrnicasApi.md#get_payrolls) | **GET** /payrolls | Endpoint para consultar nóminas electrónicas


# **adjust_payroll**
> GetTestSetByGovernmentId200Response adjust_payroll(id, adjust_payroll_request)

Endpoint para reemplazar/ajustar una nómina electrónica

Este endpoint permite reemplazar/ajustar la nómina electrónica enviada como parámetro

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.adjust_payroll_request import AdjustPayrollRequest
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
    api_instance = openapi_client.NminasElectrnicasApi(api_client)
    id = 'id_example' # str | Id de la nómina electrónica que se desea reemplazar/ajustar
    adjust_payroll_request = {"payroll":{"prefix":"NE","number":1,"governmentData":{"Periodo":{"FechaIngreso":"2016-04-04","FechaLiquidacionInicio":"2021-02-01","FechaLiquidacionFin":"2021-02-28"},"LugarGeneracionXML":{"Pais":"CO","DepartamentoEstado":"11","MunicipioCiudad":"11001","Idioma":"es"},"InformacionGeneral":{"PeriodoNomina":"5","TipoMoneda":"COP"},"Empleador":{"RazonSocial":"Soluciones Alegra S.A.S","NIT":"1111111","DV":"0","Pais":"CO","DepartamentoEstado":"05","MunicipioCiudad":"05001","Direccion":"Calle test"},"Trabajador":{"TipoTrabajador":"01","SubTipoTrabajador":"00","AltoRiesgoPension":false,"TipoDocumento":"13","NumeroDocumento":"1111111","PrimerApellido":"PrimerApellido","SegundoApellido":"SegundoApellido","PrimerNombre":"PrimerNombre","OtrosNombres":"OtrosNombres","LugarTrabajoPais":"CO","LugarTrabajoDepartamentoEstado":"25","LugarTrabajoMunicipioCiudad":"25899","LugarTrabajoDireccion":"Calle test","SalarioIntegral":false,"TipoContrato":"2","Sueldo":6000000},"Pago":{"Forma":"1","Metodo":"3","Banco":"BANCOLOMBIA S.A","TipoCuenta":"Cuenta de ahorros","NumeroCuenta":"0000000547"},"FechasPagos":{"FechaPago":["2021-02-26"]},"Devengados":{"Basico":{"DiasTrabajados":28,"SueldoTrabajado":6000000},"Bonificaciones":{"Bonificacion":[{"BonificacionNS":2000000}]}},"Deducciones":{"Salud":{"Porcentaje":4,"Deduccion":240000},"FondoPension":{"Porcentaje":4,"Deduccion":240000},"FondoSP":{"Porcentaje":1,"Deduccion":60000},"RetencionFuente":427000},"Redondeo":0,"DevengadosTotal":8000000,"DeduccionesTotal":540000,"ComprobanteTotal":7033000}}} # AdjustPayrollRequest | Objeto con la información de la nómina electrónica que reemplazará a la anterior

    try:
        # Endpoint para reemplazar/ajustar una nómina electrónica
        api_response = api_instance.adjust_payroll(id, adjust_payroll_request)
        print("The response of NminasElectrnicasApi->adjust_payroll:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NminasElectrnicasApi->adjust_payroll: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la nómina electrónica que se desea reemplazar/ajustar | 
 **adjust_payroll_request** | [**AdjustPayrollRequest**](AdjustPayrollRequest.md)| Objeto con la información de la nómina electrónica que reemplazará a la anterior | 

### Return type

[**GetTestSetByGovernmentId200Response**](GetTestSetByGovernmentId200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía una nómina electrónica a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_payroll**
> CancelPayroll200Response cancel_payroll(id, cancel_payroll_request)

Endpoint para anular una nómina electrónica

Este endpoint permite anular la nómina electrónica enviada como parámetro

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.cancel_payroll200_response import CancelPayroll200Response
from openapi_client.models.cancel_payroll_request import CancelPayrollRequest
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
    api_instance = openapi_client.NminasElectrnicasApi(api_client)
    id = 'id_example' # str | Id de la nómina electrónica que se desea anular
    cancel_payroll_request = {"prefix":"NEA","number":1} # CancelPayrollRequest | Objeto con la información de la anulación de nómina electrónica

    try:
        # Endpoint para anular una nómina electrónica
        api_response = api_instance.cancel_payroll(id, cancel_payroll_request)
        print("The response of NminasElectrnicasApi->cancel_payroll:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NminasElectrnicasApi->cancel_payroll: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la nómina electrónica que se desea anular | 
 **cancel_payroll_request** | [**CancelPayrollRequest**](CancelPayrollRequest.md)| Objeto con la información de la anulación de nómina electrónica | 

### Return type

[**CancelPayroll200Response**](CancelPayroll200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se anula una nómina electrónica en la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payroll**
> GetTestSetByGovernmentId200Response create_payroll(create_payroll_request)

Endpoint para emitir una nómina a la DIAN

Este endpoint permite emitir una nómina electrónica a la DIAN.  Recuerda visitar previamente las guías de [Inicio](https://e-provider-docs.alegra.com/docs/gu%C3%ADa-creaci%C3%B3n-de-una-compa%C3%B1%C3%ADa-asociada) y la guía de [Habilitación en la DIAN - Nómina Electronica](https://e-provider-docs.alegra.com/docs/gu%C3%ADa-del-proceso-de-habilitaci%C3%B3n-en-la-dian-n%C3%B3mina-electr%C3%B3nica)

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_payroll_request import CreatePayrollRequest
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
    api_instance = openapi_client.NminasElectrnicasApi(api_client)
    create_payroll_request = {"company":{"id":"01FQS9ZGW84DG8C2ZFDZJZGEV2"},"prefix":"NE","number":1,"governmentData":{"Periodo":{"FechaIngreso":"2016-04-04","FechaLiquidacionInicio":"2021-02-01","FechaLiquidacionFin":"2021-02-28"},"LugarGeneracionXML":{"Pais":"CO","DepartamentoEstado":"11","MunicipioCiudad":"11001","Idioma":"es"},"InformacionGeneral":{"PeriodoNomina":"5","TipoMoneda":"COP"},"Empleador":{"RazonSocial":"Soluciones Alegra S.A.S","NIT":1111111,"DV":0,"Pais":"CO","DepartamentoEstado":"05","MunicipioCiudad":"05001","Direccion":"Calle test"},"Trabajador":{"TipoTrabajador":"01","SubTipoTrabajador":"00","AltoRiesgoPension":false,"TipoDocumento":"13","NumeroDocumento":"1111111","PrimerApellido":"PrimerApellido","SegundoApellido":"SegundoApellido","PrimerNombre":"PrimerNombre","OtrosNombres":"OtrosNombres","LugarTrabajoPais":"CO","LugarTrabajoDepartamentoEstado":"25","LugarTrabajoMunicipioCiudad":"25899","LugarTrabajoDireccion":"Calle test","SalarioIntegral":false,"TipoContrato":"2","Sueldo":6000000},"Pago":{"Forma":"1","Metodo":"3","Banco":"BANCOLOMBIA S.A","TipoCuenta":"Cuenta de ahorros","NumeroCuenta":"0000000547"},"FechasPagos":{"FechaPago":["2021-02-26"]},"Devengados":{"Basico":{"DiasTrabajados":28,"SueldoTrabajado":6000000},"Bonificaciones":{"Bonificacion":[{"BonificacionNS":2000000}]}},"Deducciones":{"Salud":{"Porcentaje":4,"Deduccion":240000},"FondoPension":{"Porcentaje":4,"Deduccion":240000},"FondoSP":{"Porcentaje":1,"Deduccion":60000},"RetencionFuente":427000},"Redondeo":0,"DevengadosTotal":8000000,"DeduccionesTotal":540000,"ComprobanteTotal":7033000}} # CreatePayrollRequest | Objeto con la información de la nómina electrónica

    try:
        # Endpoint para emitir una nómina a la DIAN
        api_response = api_instance.create_payroll(create_payroll_request)
        print("The response of NminasElectrnicasApi->create_payroll:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NminasElectrnicasApi->create_payroll: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payroll_request** | [**CreatePayrollRequest**](CreatePayrollRequest.md)| Objeto con la información de la nómina electrónica | 

### Return type

[**GetTestSetByGovernmentId200Response**](GetTestSetByGovernmentId200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía una nómina electrónica a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payroll**
> GetTestSetByGovernmentId200Response get_payroll(id)

Endpoint para consultar una nómina electrónica

Retorna toda la información asociada a la nómina electrónica enviada como parámetro

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
    api_instance = openapi_client.NminasElectrnicasApi(api_client)
    id = 'id_example' # str | Id de la nómina electrónica

    try:
        # Endpoint para consultar una nómina electrónica
        api_response = api_instance.get_payroll(id)
        print("The response of NminasElectrnicasApi->get_payroll:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NminasElectrnicasApi->get_payroll: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la nómina electrónica | 

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

# **get_payroll_adjustments**
> GetPayrollAdjustments200Response get_payroll_adjustments(limit=limit, var_from=var_from, id_company=id_company, prefix=prefix, number=number, status=status, legal_status=legal_status)

Endpoint para consultar ajustes de nóminas electrónicas

Este endpoint permite consultar todos los ajustes de nómina de una empresa

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_payroll_adjustments200_response import GetPayrollAdjustments200Response
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
    api_instance = openapi_client.NminasElectrnicasApi(api_client)
    limit = 56 # int | Cantidad de resultados a obtener, por defecto es 50. (optional)
    var_from = 'var_from_example' # str | Id del ajuste a partir de la cuál se desea iniciar la consulta. (optional)
    id_company = 'id_company_example' # str | Id de la empresa. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la empresa asociada al token de autenticación (optional)
    prefix = 'prefix_example' # str | Filtrar ajustes por prefijo (optional)
    number = 'number_example' # str | Filtrar ajustes por número, para usar este filtro es obligatorio enviar el de prefijo (optional)
    status = 'status_example' # str | Filtrar ajustes por estado (optional)
    legal_status = 'legal_status_example' # str | Filtrar ajustes por estado legal (optional)

    try:
        # Endpoint para consultar ajustes de nóminas electrónicas
        api_response = api_instance.get_payroll_adjustments(limit=limit, var_from=var_from, id_company=id_company, prefix=prefix, number=number, status=status, legal_status=legal_status)
        print("The response of NminasElectrnicasApi->get_payroll_adjustments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NminasElectrnicasApi->get_payroll_adjustments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Cantidad de resultados a obtener, por defecto es 50. | [optional] 
 **var_from** | **str**| Id del ajuste a partir de la cuál se desea iniciar la consulta. | [optional] 
 **id_company** | **str**| Id de la empresa. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la empresa asociada al token de autenticación | [optional] 
 **prefix** | **str**| Filtrar ajustes por prefijo | [optional] 
 **number** | **str**| Filtrar ajustes por número, para usar este filtro es obligatorio enviar el de prefijo | [optional] 
 **status** | **str**| Filtrar ajustes por estado | [optional] 
 **legal_status** | **str**| Filtrar ajustes por estado legal | [optional] 

### Return type

[**GetPayrollAdjustments200Response**](GetPayrollAdjustments200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se consultan los ajustes de nóminas electrónicas |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payroll_cancellations**
> GetPayrollCancellations200Response get_payroll_cancellations(limit=limit, var_from=var_from, id_company=id_company, prefix=prefix, number=number, status=status, legal_status=legal_status)

Endpoint para consultar cancelaciones de nóminas electrónicas

Este endpoint permite consultar todas las cancelaciones de nómina de una empresa

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_payroll_cancellations200_response import GetPayrollCancellations200Response
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
    api_instance = openapi_client.NminasElectrnicasApi(api_client)
    limit = 56 # int | Cantidad de resultados a obtener, por defecto es 50. (optional)
    var_from = 'var_from_example' # str | Id de la cancelación a partir de la cuál se desea iniciar la consulta. (optional)
    id_company = 'id_company_example' # str | Id de la empresa. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la empresa asociada al token de autenticación (optional)
    prefix = 'prefix_example' # str | Filtrar cancelaciones por prefijo (optional)
    number = 'number_example' # str | Filtrar cancelaciones por número, para usar este filtro es obligatorio enviar el de prefijo (optional)
    status = 'status_example' # str | Filtrar cancelaciones por estado (optional)
    legal_status = 'legal_status_example' # str | Filtrar cancelaciones por estado legal (optional)

    try:
        # Endpoint para consultar cancelaciones de nóminas electrónicas
        api_response = api_instance.get_payroll_cancellations(limit=limit, var_from=var_from, id_company=id_company, prefix=prefix, number=number, status=status, legal_status=legal_status)
        print("The response of NminasElectrnicasApi->get_payroll_cancellations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NminasElectrnicasApi->get_payroll_cancellations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Cantidad de resultados a obtener, por defecto es 50. | [optional] 
 **var_from** | **str**| Id de la cancelación a partir de la cuál se desea iniciar la consulta. | [optional] 
 **id_company** | **str**| Id de la empresa. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la empresa asociada al token de autenticación | [optional] 
 **prefix** | **str**| Filtrar cancelaciones por prefijo | [optional] 
 **number** | **str**| Filtrar cancelaciones por número, para usar este filtro es obligatorio enviar el de prefijo | [optional] 
 **status** | **str**| Filtrar cancelaciones por estado | [optional] 
 **legal_status** | **str**| Filtrar cancelaciones por estado legal | [optional] 

### Return type

[**GetPayrollCancellations200Response**](GetPayrollCancellations200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se consultan las cancelaciones de nóminas electrónicas |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payroll_file**
> GetPayrollFile200Response get_payroll_file(id, file_type)

Endpoint para obtener un archivo asociado a la nómina electrónica

Retorna el archivo asociado a la nómina electrónica codificado en base 64

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
    api_instance = openapi_client.NminasElectrnicasApi(api_client)
    id = 'id_example' # str | Id de la nómina electrónica
    file_type = 'file_type_example' # str | Tipo de archivo que se desea obtener

    try:
        # Endpoint para obtener un archivo asociado a la nómina electrónica
        api_response = api_instance.get_payroll_file(id, file_type)
        print("The response of NminasElectrnicasApi->get_payroll_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NminasElectrnicasApi->get_payroll_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la nómina electrónica | 
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
**200** | Objeto que representa la respuesta que contiene la información de un archivo asociado a la nómina electrónica |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payrolls**
> GetPayrolls200Response get_payrolls(limit=limit, var_from=var_from, id_company=id_company, prefix=prefix, number=number, status=status, legal_status=legal_status)

Endpoint para consultar nóminas electrónicas

Este endpoint permite consultar todas las nóminas electrónicas de una empresa

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.get_payrolls200_response import GetPayrolls200Response
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
    api_instance = openapi_client.NminasElectrnicasApi(api_client)
    limit = 56 # int | Cantidad de resultados a obtener, por defecto es 50. (optional)
    var_from = 'var_from_example' # str | Id de la nómina a partir de la cuál se desea iniciar la consulta. (optional)
    id_company = 'id_company_example' # str | Id de la empresa. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la empresa asociada al token de autenticación (optional)
    prefix = 'prefix_example' # str | Filtrar nóminas por prefijo (optional)
    number = 'number_example' # str | Filtrar nóminas por número, para usar este filtro es obligatorio enviar el de prefijo (optional)
    status = 'status_example' # str | Filtrar nóminas por estado (optional)
    legal_status = 'legal_status_example' # str | Filtrar nóminas por estado legal (optional)

    try:
        # Endpoint para consultar nóminas electrónicas
        api_response = api_instance.get_payrolls(limit=limit, var_from=var_from, id_company=id_company, prefix=prefix, number=number, status=status, legal_status=legal_status)
        print("The response of NminasElectrnicasApi->get_payrolls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NminasElectrnicasApi->get_payrolls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Cantidad de resultados a obtener, por defecto es 50. | [optional] 
 **var_from** | **str**| Id de la nómina a partir de la cuál se desea iniciar la consulta. | [optional] 
 **id_company** | **str**| Id de la empresa. Este parámetro es opcional, sino se envia este objeto, Alegra tomará la empresa asociada al token de autenticación | [optional] 
 **prefix** | **str**| Filtrar nóminas por prefijo | [optional] 
 **number** | **str**| Filtrar nóminas por número, para usar este filtro es obligatorio enviar el de prefijo | [optional] 
 **status** | **str**| Filtrar nóminas por estado | [optional] 
 **legal_status** | **str**| Filtrar nóminas por estado legal | [optional] 

### Return type

[**GetPayrolls200Response**](GetPayrolls200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se consultan las nóminas electrónicas |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

