# openapi_client.DocumentosEquivalentesElectrnicosApi

All URIs are relative to *https://sandbox-api.alegra.com/e-provider/col/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjustment_note_equivalent_document_file**](DocumentosEquivalentesElectrnicosApi.md#adjustment_note_equivalent_document_file) | **GET** /adjustment-note-equivalent-documents/{id}/files/{fileType} | Endpoint para obtener un archivo asociado a la nota de ajuste al documento equivalente electrónico
[**create_adjustment_note_equivalent_document**](DocumentosEquivalentesElectrnicosApi.md#create_adjustment_note_equivalent_document) | **POST** /adjustment-note-equivalent-documents | Endpoint para emitir una nota de ajuste al documento equivalente electrónico a la DIAN
[**create_equivalent_document_pos**](DocumentosEquivalentesElectrnicosApi.md#create_equivalent_document_pos) | **POST** /equivalent-documents/pos | Emisión Documento Equivalente POS a la DIAN
[**get_adjustment_note_equivalent_document**](DocumentosEquivalentesElectrnicosApi.md#get_adjustment_note_equivalent_document) | **GET** /adjustment-note-equivalent-documents/{id} | Endpoint para consultar una nota de ajuste al documento equivalente electrónico
[**get_equivalent_document_pos**](DocumentosEquivalentesElectrnicosApi.md#get_equivalent_document_pos) | **GET** /equivalent-documents/{id} | Endpoint para consultar un documento equivalente electrónico
[**get_equivalent_document_pos_file**](DocumentosEquivalentesElectrnicosApi.md#get_equivalent_document_pos_file) | **GET** /equivalent-documents/{id}/files/{fileType} | Endpoint para obtener un archivo asociado al documento equivalente electrónico


# **adjustment_note_equivalent_document_file**
> GetPayrollFile200Response adjustment_note_equivalent_document_file(id, file_type)

Endpoint para obtener un archivo asociado a la nota de ajuste al documento equivalente electrónico

Retorna el archivo asociado a la nota de ajuste al documento equivalente electrónico codificado en base 64.

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
    api_instance = openapi_client.DocumentosEquivalentesElectrnicosApi(api_client)
    id = 'id_example' # str | Id de la nota de ajuste al documento equivalente electrónico
    file_type = 'file_type_example' # str | Tipo de archivo que se desea obtener

    try:
        # Endpoint para obtener un archivo asociado a la nota de ajuste al documento equivalente electrónico
        api_response = api_instance.adjustment_note_equivalent_document_file(id, file_type)
        print("The response of DocumentosEquivalentesElectrnicosApi->adjustment_note_equivalent_document_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentosEquivalentesElectrnicosApi->adjustment_note_equivalent_document_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la nota de ajuste al documento equivalente electrónico | 
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

# **create_adjustment_note_equivalent_document**
> CreateAdjustmentNoteEquivalentDocument200Response create_adjustment_note_equivalent_document(create_adjustment_note_equivalent_document_request)

Endpoint para emitir una nota de ajuste al documento equivalente electrónico a la DIAN

Este endpoint permite emitir una nota de ajuste al documento equivalente electrónico a la DIAN. Recuerda visitar previamente las guías de [Inicio](https://e-provider-docs.alegra.com/docs/gu%C3%ADa-creaci%C3%B3n-de-una-compa%C3%B1%C3%ADa-asociada) y la guía de [Habilitación en la DIAN - Documento Equivalente POS Electrónico](https://e-provider-docs.alegra.com/docs/gu%C3%ADa-del-proceso-de-habilitaci%C3%B3n-en-la-dian-documento-equivalente-pos-electr%C3%B3nico)

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_adjustment_note_equivalent_document200_response import CreateAdjustmentNoteEquivalentDocument200Response
from openapi_client.models.create_adjustment_note_equivalent_document_request import CreateAdjustmentNoteEquivalentDocumentRequest
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
    api_instance = openapi_client.DocumentosEquivalentesElectrnicosApi(api_client)
    create_adjustment_note_equivalent_document_request = {"prefix":"NADE","number":"001","documentReference":{"fullNumber":"EPOS18","cude":"d48a9a3c134e1e2abcaefd056f8c0ba00ca03644f93e65a730264d53cfb406e05870fa1ab35564c62c574225aecbe944","issueDate":"2022-11-28"},"discrepancies":[{"sectionId":"DSBB02","responseCode":4,"description":"Ajuste de precio"}],"note":"nota de ejmplo","company":{"id":"01FCYA9GSSNT2674KGJV2V0NS9","organizationType":1,"identificationType":"31","identificationNumber":"900559088","dv":"2","name":"Soluciones Alegra S.A.S","regimeCode":"R-99-PN","email":"email@email.com","address":{"address":"Cra. 13 #12-12 Edificio A & A","city":"11001","department":"11","country":"CO"}},"customer":{"organizationType":1,"identificationType":"13","identificationNumber":"900559088","dv":"2","name":"Company SAS","email":"company@alegra.com","address":{"address":"Calle. 123 Edificio A & A","city":"11001","department":"11"}},"items":[{"code":"","name":"Botella de M3","description":"This is the ítem de metro cubico M3","price":10000,"discount":0,"discountAmount":0,"quantity":1,"unitCode":"94","subtotal":10000,"taxAmount":1900,"total":11900,"taxes":[{"taxCode":"01","taxAmount":1900,"taxPercentage":"19.00","taxableAmount":10000}]}],"totalAmounts":{"grossTotal":10000,"taxableTotal":10000,"taxTotal":1900,"discountTotal":0,"chargeTotal":0,"advanceTotal":0,"payableTotal":11900,"currencyCode":"COP"},"payments":[{"paymentForm":"1","paymentMethod":"10","paymentDueDate":"2021-08-30"}],"delivery":{"date":"2022-10-19","time":"09:24:37-05:00","address":{"city":"05001","postal":"050001","department":"05","address":"Calle Falsa # 56-89"},"deliveryCompany":{"name":"Repartidora S.A.S","address":{"city":"11001","postal":"2002","department":"11","address":"Calle 125 # 66-111"},"taxScheme":{"name":"Repartidora Asociados","code":"01","identification":"9008002121","identificationType":"31","dv":"2","address":{"city":"11001","postal":"2002","department":"11","address":"Calle 100 # 54-09"}}}}} # CreateAdjustmentNoteEquivalentDocumentRequest | Objeto con la información de una nota de ajuste al documento equivalente electrónico

    try:
        # Endpoint para emitir una nota de ajuste al documento equivalente electrónico a la DIAN
        api_response = api_instance.create_adjustment_note_equivalent_document(create_adjustment_note_equivalent_document_request)
        print("The response of DocumentosEquivalentesElectrnicosApi->create_adjustment_note_equivalent_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentosEquivalentesElectrnicosApi->create_adjustment_note_equivalent_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_adjustment_note_equivalent_document_request** | [**CreateAdjustmentNoteEquivalentDocumentRequest**](CreateAdjustmentNoteEquivalentDocumentRequest.md)| Objeto con la información de una nota de ajuste al documento equivalente electrónico | 

### Return type

[**CreateAdjustmentNoteEquivalentDocument200Response**](CreateAdjustmentNoteEquivalentDocument200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía una una nota de ajuste al documento equivalente electrónico a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_equivalent_document_pos**
> CreateEquivalentDocumentPos200Response create_equivalent_document_pos(create_equivalent_document_pos_request)

Emisión Documento Equivalente POS a la DIAN

Este endpoint permite emitir un Documento Equivalente Electrónico Tiquete de Máquina Registradora con sistema P.O.S a la DIAN. Recuerda visitar previamente las guías de [Inicio](https://e-provider-docs.alegra.com/docs/gu%C3%ADa-creaci%C3%B3n-de-una-compa%C3%B1%C3%ADa-asociada) y la guía de [Habilitación en la DIAN - Documento Equivalente POS Electrónico](https://e-provider-docs.alegra.com/docs/gu%C3%ADa-del-proceso-de-habilitaci%C3%B3n-en-la-dian-documento-equivalente-pos-electr%C3%B3nico)

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_equivalent_document_pos200_response import CreateEquivalentDocumentPos200Response
from openapi_client.models.create_equivalent_document_pos_request import CreateEquivalentDocumentPosRequest
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
    api_instance = openapi_client.DocumentosEquivalentesElectrnicosApi(api_client)
    create_equivalent_document_pos_request = {"number":990015,"resolution":{"resolutionNumber":"18760000001","prefix":"POS","minNumber":990000,"maxNumber":995000,"startDate":"2019-01-19","endDate":"2030-01-19"},"company":{"id":"01FCYA9GSSNT2674KGJV2V0NS9","organizationType":1,"identificationNumber":"900559088","dv":"2","name":"Soluciones Alegra S.A.S","regimeCode":"R-99-PN","taxCode":{"id":"01"},"email":"email@email.com","address":{"address":"Cra. 13 #12-12 Edificio A & A","city":"11001","department":"11","country":"CO"}},"items":[{"code":{"identificationId":"BM3","id":"999"},"description":"This is the ítem de metro cubico M3","price":10000,"discount":0,"discountAmount":0,"quantity":1,"unitCode":"94","subtotal":10000,"taxAmount":1900,"total":11900,"taxes":[{"taxCode":"01","taxAmount":1900,"taxPercentage":"19.00","taxableAmount":10000}]}],"payments":[{"paymentForm":"1","paymentMethod":"10","paymentDueDate":"2021-08-30"}],"totalAmounts":{"grossTotal":10000,"taxableTotal":10000,"taxTotal":1900,"discountTotal":0,"chargeTotal":0,"advanceTotal":0,"payableTotal":11900,"currencyCode":"COP"},"buyerBenefits":{"identification":"123455667","name":"John Doe","points":"300"},"cashRegister":{"plate":"210291","location":"Centro","type":"standard","cashier":"Pedro P","saleCode":"A129","subtotal":"8000"},"note":"El cliente recibe un descuento de frecuencia"} # CreateEquivalentDocumentPosRequest | Objeto con la información del Documento Equivalente POS

    try:
        # Emisión Documento Equivalente POS a la DIAN
        api_response = api_instance.create_equivalent_document_pos(create_equivalent_document_pos_request)
        print("The response of DocumentosEquivalentesElectrnicosApi->create_equivalent_document_pos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentosEquivalentesElectrnicosApi->create_equivalent_document_pos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_equivalent_document_pos_request** | [**CreateEquivalentDocumentPosRequest**](CreateEquivalentDocumentPosRequest.md)| Objeto con la información del Documento Equivalente POS | 

### Return type

[**CreateEquivalentDocumentPos200Response**](CreateEquivalentDocumentPos200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía un documento equivalente electrónico a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_adjustment_note_equivalent_document**
> CreateAdjustmentNoteEquivalentDocument200Response get_adjustment_note_equivalent_document(id)

Endpoint para consultar una nota de ajuste al documento equivalente electrónico

Retorna toda la información asociada a la nota de ajuste a un documento equivalente electrónico enviado como parámetro.

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_adjustment_note_equivalent_document200_response import CreateAdjustmentNoteEquivalentDocument200Response
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
    api_instance = openapi_client.DocumentosEquivalentesElectrnicosApi(api_client)
    id = 'id_example' # str | Id de la nota de ajuste a un documento equivalente electrónico

    try:
        # Endpoint para consultar una nota de ajuste al documento equivalente electrónico
        api_response = api_instance.get_adjustment_note_equivalent_document(id)
        print("The response of DocumentosEquivalentesElectrnicosApi->get_adjustment_note_equivalent_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentosEquivalentesElectrnicosApi->get_adjustment_note_equivalent_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la nota de ajuste a un documento equivalente electrónico | 

### Return type

[**CreateAdjustmentNoteEquivalentDocument200Response**](CreateAdjustmentNoteEquivalentDocument200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía una una nota de ajuste al documento equivalente electrónico a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_equivalent_document_pos**
> CreateEquivalentDocumentPos200Response get_equivalent_document_pos(id)

Endpoint para consultar un documento equivalente electrónico

Retorna toda la información asociada al documento equivalente correspondiente al parámetro

### Example

* Bearer Authentication (auth):

```python
import openapi_client
from openapi_client.models.create_equivalent_document_pos200_response import CreateEquivalentDocumentPos200Response
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
    api_instance = openapi_client.DocumentosEquivalentesElectrnicosApi(api_client)
    id = 'id_example' # str | Id de la documento equivalente electrónico

    try:
        # Endpoint para consultar un documento equivalente electrónico
        api_response = api_instance.get_equivalent_document_pos(id)
        print("The response of DocumentosEquivalentesElectrnicosApi->get_equivalent_document_pos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentosEquivalentesElectrnicosApi->get_equivalent_document_pos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id de la documento equivalente electrónico | 

### Return type

[**CreateEquivalentDocumentPos200Response**](CreateEquivalentDocumentPos200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Objeto que representa la respuesta cuando se envía un documento equivalente electrónico a la DIAN |  -  |
**400** | Objeto que representa una respuesta de error por validaciones |  -  |
**404** | Objeto que representa una respuesta de error por qué no se ha encontrado el recurso al que se intenta acceder |  -  |
**500** | Objeto que representa una respuesta de error por qué ha ocurrido un error interno en el sistema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_equivalent_document_pos_file**
> GetPayrollFile200Response get_equivalent_document_pos_file(id, file_type)

Endpoint para obtener un archivo asociado al documento equivalente electrónico

Retorna el archivo asociado al documento equivalente codificado en base 64.

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
    api_instance = openapi_client.DocumentosEquivalentesElectrnicosApi(api_client)
    id = 'id_example' # str | Id del documento equivalente electrónica
    file_type = 'file_type_example' # str | Tipo de archivo que se desea obtener

    try:
        # Endpoint para obtener un archivo asociado al documento equivalente electrónico
        api_response = api_instance.get_equivalent_document_pos_file(id, file_type)
        print("The response of DocumentosEquivalentesElectrnicosApi->get_equivalent_document_pos_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentosEquivalentesElectrnicosApi->get_equivalent_document_pos_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id del documento equivalente electrónica | 
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

