# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CreatePayrollRequestGovernmentDataDevengadosHENDFsHENDFInner(BaseModel):
    """
    Objeto con información sobre devengados por concepto de horas extras nocturnas dominicales y festivas
    """ # noqa: E501
    hora_inicio: Optional[datetime] = Field(default=None, description="Hora de inicio de Horas Extras Nocturnas Dominical y Festivos", alias="HoraInicio")
    hora_fin: Optional[datetime] = Field(default=None, description="Hora de fin de Horas Extras Nocturnas Dominical y Festivos", alias="HoraFin")
    cantidad: Union[StrictFloat, StrictInt] = Field(description="Cantidad de Horas Extras Nocturnas Dominical y Festivos", alias="Cantidad")
    porcentaje: StrictStr = Field(description="Porcentaje al cual corresponde el calculo de 1 hora Extras Nocturnas Dominical y Festivo. Se debe colocar el Porcentaje que corresponda de la tabla de la DIAN para tipos de horas extra", alias="Porcentaje")
    pago: Union[StrictFloat, StrictInt] = Field(description="Es el valor pagado por el tiempo que se trabaja adicional a la jornada legal o pactada contractualmente.", alias="Pago")
    __properties: ClassVar[List[str]] = ["HoraInicio", "HoraFin", "Cantidad", "Porcentaje", "Pago"]

    @field_validator('porcentaje')
    def porcentaje_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['6']):
            raise ValueError("must be one of enum values ('6')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreatePayrollRequestGovernmentDataDevengadosHENDFsHENDFInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreatePayrollRequestGovernmentDataDevengadosHENDFsHENDFInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "HoraInicio": obj.get("HoraInicio"),
            "HoraFin": obj.get("HoraFin"),
            "Cantidad": obj.get("Cantidad"),
            "Porcentaje": obj.get("Porcentaje"),
            "Pago": obj.get("Pago")
        })
        return _obj


