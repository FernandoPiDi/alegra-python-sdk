# CreateInvoiceRequestHealthSectorGeneral

Objeto que contiene los campos de datos adicionales correspondientes al Sector Salud

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_provider_code** | **str** | Código del prestador de servicios de salud | 
**payment_method** | **str** | Modalidad de pago. Debe registrarse la modalidad de pago pactada objeto de facturación. Se debe colocar el Código que corresponda de la tabla de los tipos de modalidades de pago (Sector Salud) disponibles de la DIAN | 
**benefits_plan_type** | **str** | Cobertura o plan de beneficios. Se debe colocar el Código que corresponda de la tabla de los tipos de cobertura o plan de beneficios (Sector Salud) disponibles de la DIAN | 
**contract_number** | **str** | Número de contrato. Cuando sea informado un número de contrato no se podrá informar un número de póliza (&#x60;policyNumber&#x60;). | [optional] 
**policy_number** | **str** | Número de póliza SOAT o del número de póliza de planes voluntarios de salud.  Cuando sea informado un número de Póliza, no se podrá informar un número de contrato (&#x60;contractNumber&#x60;) | [optional] 
**prepaid_payments** | [**List[CreateInvoiceRequestHealthSectorGeneralPrepaidPaymentsInner]**](CreateInvoiceRequestHealthSectorGeneralPrepaidPaymentsInner.md) |  | 
**service_start_date** | **date** | Fecha de inicio del periodo de facturación. Formato AAAA-MM-DD | 
**service_end_date** | **date** | Fecha final del periodo de facturación. Formato AAAA-MM-DD | 
**operation_type** | **str** | Código del tipo de operación salud | 

## Example

```python
from openapi_client.models.create_invoice_request_health_sector_general import CreateInvoiceRequestHealthSectorGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoiceRequestHealthSectorGeneral from a JSON string
create_invoice_request_health_sector_general_instance = CreateInvoiceRequestHealthSectorGeneral.from_json(json)
# print the JSON string representation of the object
print(CreateInvoiceRequestHealthSectorGeneral.to_json())

# convert the object into a dict
create_invoice_request_health_sector_general_dict = create_invoice_request_health_sector_general_instance.to_dict()
# create an instance of CreateInvoiceRequestHealthSectorGeneral from a dict
create_invoice_request_health_sector_general_from_dict = CreateInvoiceRequestHealthSectorGeneral.from_dict(create_invoice_request_health_sector_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


