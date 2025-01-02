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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CreateInvoiceRequestHealthSectorGeneralPrepaidPaymentsInner(BaseModel):
    """
    Objeto que contiene la información de los pagos anticipados. <br><i>Grupo de información oficial DIAN &lt;PrepaidPayment&gt;</i>
    """ # noqa: E501
    code: StrictStr = Field(description="Codigo del pago anticipado, según la tabla `conceptoRecaudo`. (01): Copago, (02): Cuota moderadora, (03): Pagos compartidos en planes voluntarios de salud, (04): Anticipo, (05): No aplica")
    amount: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Valor del pago")
    received_date: date = Field(description="Fecha en la cual el pago fue recibido. Formato AAAA-MM-DD", alias="receivedDate")
    __properties: ClassVar[List[str]] = ["code", "amount", "receivedDate"]

    @field_validator('code')
    def code_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['01', '02', '03', '04', '05']):
            raise ValueError("must be one of enum values ('01', '02', '03', '04', '05')")
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
        """Create an instance of CreateInvoiceRequestHealthSectorGeneralPrepaidPaymentsInner from a JSON string"""
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
        """Create an instance of CreateInvoiceRequestHealthSectorGeneralPrepaidPaymentsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "amount": obj.get("amount"),
            "receivedDate": obj.get("receivedDate")
        })
        return _obj


