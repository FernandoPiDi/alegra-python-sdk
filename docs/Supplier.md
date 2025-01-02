# Supplier

Objeto que contiene la información del proveedor del documento electrónico

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre del proveedor | 
**origin** | **str** | Indicador de procedencia del vendedor (Residente fiscal en Colombia o No residente fiscal). Se debe colocar el Código que corresponda de la tabla de tipos de procedencia del vendedor de la DIAN | [optional] 
**organization_type** | **float** | Tipo de organización jurídica. Se debe colocar el Código que corresponda de la tabla de tipos de organización jurídica de la DIAN | 
**identification_type** | **str** | Tipo de documento de identificación del proveedor. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN | 
**identification_number** | **str** | Número de identificación del proveedor | 
**dv** | **str** | DV del NIT del proveedor. Es obligatorio si identificationType &#x3D; 31 | [optional] 
**regime_code** | **str** | Régimen al que pertenece el proveedor. Se debe colocar el Código que corresponda de la tabla de tipos de régimen/responsabilidades fiscales de la DIAN. Para reportar varias obligaciones / responsabilidades, se deben reportar separando cada uno de los valores de la lista con &#39;;&#39;. Ejemplo O‐13;O‐15; | [optional] 
**email** | **str** | Correo electrónico. Se agregará como información de contacto en caso de tener habilitado la propiedad notificationByEmail en Compañía | [optional] 
**phone** | **str** | Número de teléfono, celular u otro. Se agregará el número de contacto en el correo de notificación en caso de tener habilitado la propiedad notificationByEmail en Compañía | [optional] 
**address** | [**GetCompanies200ResponseCompaniesInnerAddress**](GetCompanies200ResponseCompaniesInnerAddress.md) |  | 

## Example

```python
from openapi_client.models.supplier import Supplier

# TODO update the JSON string below
json = "{}"
# create an instance of Supplier from a JSON string
supplier_instance = Supplier.from_json(json)
# print the JSON string representation of the object
print(Supplier.to_json())

# convert the object into a dict
supplier_dict = supplier_instance.to_dict()
# create an instance of Supplier from a dict
supplier_from_dict = Supplier.from_dict(supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


