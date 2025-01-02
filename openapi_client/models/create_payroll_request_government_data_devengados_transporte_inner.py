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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CreatePayrollRequestGovernmentDataDevengadosTransporteInner(BaseModel):
    """
    Objeto con la información devengada por concepto de transporte
    """ # noqa: E501
    auxilio_transporte: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Parte de los viáticos pagado al trabajador correspondientes a medios de transporte y/o los gastos de representación.", alias="AuxilioTransporte")
    viatico_manu_aloj_s: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Parte de los viáticos pagado al trabajador correspondientes a manutención y/o alojamiento.", alias="ViaticoManuAlojS")
    viatico_manu_aloj_ns: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Parte de los viáticos pagado al trabajador correspondientes a manutención y/o alojamiento No Salariales.", alias="ViaticoManuAlojNS")
    __properties: ClassVar[List[str]] = ["AuxilioTransporte", "ViaticoManuAlojS", "ViaticoManuAlojNS"]

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
        """Create an instance of CreatePayrollRequestGovernmentDataDevengadosTransporteInner from a JSON string"""
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
        """Create an instance of CreatePayrollRequestGovernmentDataDevengadosTransporteInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AuxilioTransporte": obj.get("AuxilioTransporte"),
            "ViaticoManuAlojS": obj.get("ViaticoManuAlojS"),
            "ViaticoManuAlojNS": obj.get("ViaticoManuAlojNS")
        })
        return _obj


