# CreatePayrollRequestGovernmentDataTrabajador

Objeto con la información del trabajador

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo_trabajador** | **str** | Código del tipo de trabajador del Ministerio de salud. Aportes a Seguridad Social de Activos. Se debe colocar el Codigo que corresponda de la tabla de tipos de trabajador de la DIAN | 
**sub_tipo_trabajador** | **str** | Código del Sub tipo de trabajador del Ministerio de salud. Aportes a Seguridad Social de Activos. Se debe colocar el Codigo que corresponda de la tabla de subtipos de trabajador de la DIAN | 
**alto_riesgo_pension** | **bool** | Si el trabajador desarrollo durante el presente periodo alguna de las actividades descritas en el Decreto 2090 de 2003, o la norma que lo modifique, adicione o sustituya. | 
**tipo_documento** | **str** | Tipo de documento de identificación que actualmente tiene el trabajador, aprendiz, o pasante. Se debe colocar el Codigo que corresponda de la tabla de tipos de identificación de la DIAN | 
**numero_documento** | **float** | Numero de identificación que actualmente el trabajador o aprendiz | 
**primer_apellido** | **str** | Primer Apellido del trabajador o aprendiz | 
**segundo_apellido** | **str** | Segundo Apellido del trabajador o aprendiz | [optional] 
**primer_nombre** | **str** | Primer Nombre del trabajador o aprendiz | 
**otros_nombres** | **str** | Otros Nombres del trabajador o aprendiz | [optional] 
**lugar_trabajo_pais** | **str** | Código del país actual donde se encontraba ubicado el trabajador o aprendiz en el mes reportado. Se debe colocar el Codigo del país | [optional] 
**lugar_trabajo_municipio_ciudad** | **str** | Código del municipio o ciudad actual donde se encontraba ubicado el trabajador o aprendiz en el mes reportado. Se debe colocar el Codigo que corresponda de la tabla de municipios de la DIAN | 
**lugar_trabajo_direccion** | **str** | Debe corresponder a la dirección del lugar físico donde vive el empleado. | 
**salario_integral** | **bool** | Si el trabajador tiene un salario integral, el cual es el tipo de remuneración que incluye todos los conceptos que puedan constituir salario en un solo monto o pago (prestaciones sociales y recargos nocturno, dominical y festivo, y el trabajo extra) y que sea superior a 10 SMLMV mas un 30% correspondiente a factor prestacional. | 
**tipo_contrato** | **str** | Tipo de Contrato que posee el empleado con el Empleador. Se debe colocar el Codigo que corresponda de la tabla de tipos de contratos de la DIAN | 
**sueldo** | **float** | Corresponde al valor que el empleador paga de forma periódica al trabajador como contraprestación por el trabajo realizado, este puede ser fijo o variable de acuerdo a la unidad de tiempo en que las partes hayan acordado el pago, teniendo como base el día o la hora trabajada. | 
**codigo_trabajador** | **str** | Codigo del Trabajador | [optional] 

## Example

```python
from openapi_client.models.create_payroll_request_government_data_trabajador import CreatePayrollRequestGovernmentDataTrabajador

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayrollRequestGovernmentDataTrabajador from a JSON string
create_payroll_request_government_data_trabajador_instance = CreatePayrollRequestGovernmentDataTrabajador.from_json(json)
# print the JSON string representation of the object
print(CreatePayrollRequestGovernmentDataTrabajador.to_json())

# convert the object into a dict
create_payroll_request_government_data_trabajador_dict = create_payroll_request_government_data_trabajador_instance.to_dict()
# create an instance of CreatePayrollRequestGovernmentDataTrabajador from a dict
create_payroll_request_government_data_trabajador_from_dict = CreatePayrollRequestGovernmentDataTrabajador.from_dict(create_payroll_request_government_data_trabajador_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


