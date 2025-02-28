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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxSchemeAddress(BaseModel):
    """
    Información de la dirección fiscal del transportador
    """ # noqa: E501
    city: Optional[Annotated[str, Field(strict=True, max_length=5)]] = Field(default=None, description="Se debe colocar el Código que corresponda de la tabla de municipios disponibles de la DIAN")
    postal: Optional[StrictStr] = Field(default=None, description="Código postal del lugar de entrega")
    department: Optional[Annotated[str, Field(strict=True, max_length=2)]] = Field(default=None, description="Se debe colocar el Código que corresponda de la tabla de departamentos disponibles de la DIAN")
    address: Optional[StrictStr] = Field(default=None, description="Dirección del lugar fisico, sin ciudad ni departamento")
    __properties: ClassVar[List[str]] = ["city", "postal", "department", "address"]

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
        """Create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxSchemeAddress from a JSON string"""
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
        """Create an instance of CreateAdjustmentNoteEquivalentDocumentRequestDeliveryDeliveryCompanyTaxSchemeAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "city": obj.get("city"),
            "postal": obj.get("postal"),
            "department": obj.get("department"),
            "address": obj.get("address")
        })
        return _obj


