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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CreatePayrollRequestGovernmentDataDevengadosOtrosConceptosOtroConceptoInner(BaseModel):
    """
    Objeto con información sobre devengados por otro concepto
    """ # noqa: E501
    descripcion_concepto: StrictStr = Field(description="Nombre del Concepto que corresponde a los demás pagos fijos o variables realizados al trabajador que remuneren en dinero o en especie como contraprestación directa del servicio, sea cualquiera la forma o denominación que se adopte.", alias="DescripcionConcepto")
    concepto_s: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Valor de los demás pagos fijos o variables realizados al trabajador que remuneren en dinero o en especie como contraprestación directa del servicio, sea cualquiera la forma o denominación que se adopte (Salarial).", alias="ConceptoS")
    concepto_ns: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Valor de los demás pagos que ocasionalmente y por mera liberalidad recibe el trabajador del empleador, en dinero o en especie no para su beneficio, ni para enriquecer su patrimonio, sino para desempeñar a cabalidad sus funciones (No Salarial).", alias="ConceptoNS")
    __properties: ClassVar[List[str]] = ["DescripcionConcepto", "ConceptoS", "ConceptoNS"]

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
        """Create an instance of CreatePayrollRequestGovernmentDataDevengadosOtrosConceptosOtroConceptoInner from a JSON string"""
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
        """Create an instance of CreatePayrollRequestGovernmentDataDevengadosOtrosConceptosOtroConceptoInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "DescripcionConcepto": obj.get("DescripcionConcepto"),
            "ConceptoS": obj.get("ConceptoS"),
            "ConceptoNS": obj.get("ConceptoNS")
        })
        return _obj


