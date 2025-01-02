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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CreateInvoiceRequestCompanyTaxAddress(BaseModel):
    """
    Objeto que contiene la información con respeto a la dirección fiscal del emisor. Si no se envía este objeto se replicará la información que se envía en 'address'. <br><i>Grupo de información oficial DIAN &lt;RegistrationAddress&gt;</i>
    """ # noqa: E501
    address: StrictStr = Field(description="Dirección del lugar fisico. <br><i>Campo oficial DIAN &lt;Line&gt;</i>")
    city: Annotated[str, Field(strict=True, max_length=5)] = Field(description="Código de la Ciudad. Se debe colocar el Código que corresponda de la tabla de municipios disponibles de la DIAN. Se debe informar cuando el código del País es 'CO'. <br><i>Campo oficial DIAN &lt;ID&gt;</i>")
    department: Annotated[str, Field(strict=True, max_length=2)] = Field(description="Código del Departamento. Se debe colocar el Código que corresponda de la tabla de departamentos disponibles de la DIAN. Se debe informar cuando el código del País es 'CO'. <br><i>Campo oficial DIAN &lt;CountrySubentityCode&gt;</i>")
    postal_code: Optional[Annotated[str, Field(min_length=6, strict=True, max_length=6)]] = Field(default=None, description="Código Postal del lugar físico del proveedor. <br><i>Campo oficial DIAN &lt;PostalZone&gt;</i>", alias="postalCode")
    __properties: ClassVar[List[str]] = ["address", "city", "department", "postalCode"]

    @field_validator('postal_code')
    def postal_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]{6}$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]{6}$/")
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
        """Create an instance of CreateInvoiceRequestCompanyTaxAddress from a JSON string"""
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
        """Create an instance of CreateInvoiceRequestCompanyTaxAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "city": obj.get("city"),
            "department": obj.get("department"),
            "postalCode": obj.get("postalCode")
        })
        return _obj


