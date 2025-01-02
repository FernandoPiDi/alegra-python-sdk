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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CreateEventRequestCompany(BaseModel):
    """
    Detalles de la organización que emite el evento, en caso de omitir este objeto se usará la compañia principal asociada al usuario
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Id de la empresa")
    organization_type: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Tipo de organización jurídica. Se debe colocar el código que corresponda de la tabla de tipos de organización jurídica de la DIAN. Persona Jurídica y asimiladas (1). Persona Natural y asimiladas (2)", alias="organizationType")
    identification_type: Optional[StrictStr] = Field(default=None, description="Tipo de documento de identificación del emisor. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN", alias="identificationType")
    identification_number: Optional[StrictStr] = Field(default=None, description="Número de identificación o NIT del emisor, sin guiones ni dv", alias="identificationNumber")
    dv: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="DV del NIT del emisor. Es obligatorio si identificationType = 31")
    name: Optional[StrictStr] = Field(default=None, description="Nombre o nombre comercial del emisor")
    regime_code: Optional[StrictStr] = Field(default=None, description="Régimen al que pertenece el Emisor. Gran contribuyente (O-13). Autorretenedor (O-15). Agente de retencion IVA (O-23). Régimen simple de tributación (O-47). No aplica - Otros (R-99-PN)", alias="regimeCode")
    tax_code: Optional[StrictStr] = Field(default=None, description="Código tipo de impuesto según los códigos de la tabla de la DIAN. IVA (01). INC (04). IVA e INC (ZA). No aplica (ZZ)", alias="taxCode")
    __properties: ClassVar[List[str]] = ["id", "organizationType", "identificationType", "identificationNumber", "dv", "name", "regimeCode", "taxCode"]

    @field_validator('organization_type')
    def organization_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([1, 2]):
            raise ValueError("must be one of enum values (1, 2)")
        return value

    @field_validator('identification_type')
    def identification_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['11', '12', '13', '21', '22', '31', '41', '42', '47', '50', '91']):
            raise ValueError("must be one of enum values ('11', '12', '13', '21', '22', '31', '41', '42', '47', '50', '91')")
        return value

    @field_validator('dv')
    def dv_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]{1})$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]{1})$/")
        return value

    @field_validator('regime_code')
    def regime_code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['O-13', 'O-15', 'O-23', 'O-47', 'R-99-PN']):
            raise ValueError("must be one of enum values ('O-13', 'O-15', 'O-23', 'O-47', 'R-99-PN')")
        return value

    @field_validator('tax_code')
    def tax_code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['01', '04', 'ZA', 'ZZ']):
            raise ValueError("must be one of enum values ('01', '04', 'ZA', 'ZZ')")
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
        """Create an instance of CreateEventRequestCompany from a JSON string"""
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
        """Create an instance of CreateEventRequestCompany from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "organizationType": obj.get("organizationType"),
            "identificationType": obj.get("identificationType"),
            "identificationNumber": obj.get("identificationNumber"),
            "dv": obj.get("dv"),
            "name": obj.get("name"),
            "regimeCode": obj.get("regimeCode"),
            "taxCode": obj.get("taxCode")
        })
        return _obj


