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
from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CreateAdjustmentNoteSupportDocumentRequestPaymentsInner(BaseModel):
    """
    Información de un pago. <br><i>Grupo de información oficial DIAN &lt;PaymentMeans&gt;</i>
    """ # noqa: E501
    payment_form: Annotated[str, Field(strict=True, max_length=1)] = Field(description="Forma de pago. Se debe colocar el Código que corresponda de la tabla de formas de pago disponibles de la DIAN. Valores posible: `1`: Contado, `2`: Crédito <br><i>Campo oficial DIAN &lt;ID&gt;</i>", alias="paymentForm")
    payment_method: Annotated[str, Field(strict=True, max_length=3)] = Field(description="Medio de pago. Se debe colocar el Código que corresponda de la tabla de métodos de pago disponibles de la DIAN. <br><i>Campo oficial DIAN &lt;PaymentMeansCode&gt;</i>", alias="paymentMethod")
    payment_due_date: Optional[date] = Field(default=None, description="Fecha de vencimiento de la factura. Si Forma de Pago es igual a 2, este valor debe ser enviado. <br><i>Campo oficial DIAN &lt;PaymentDueDate&gt;</i>", alias="paymentDueDate")
    payment_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = Field(default=None, description="Texto libre para informar datos adicionales sobre el medio de pago. <br><i>Campo oficial DIAN &lt;PaymentID&gt;</i>", alias="paymentID")
    __properties: ClassVar[List[str]] = ["paymentForm", "paymentMethod", "paymentDueDate", "paymentID"]

    @field_validator('payment_form')
    def payment_form_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['1', '2']):
            raise ValueError("must be one of enum values ('1', '2')")
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
        """Create an instance of CreateAdjustmentNoteSupportDocumentRequestPaymentsInner from a JSON string"""
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
        """Create an instance of CreateAdjustmentNoteSupportDocumentRequestPaymentsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "paymentForm": obj.get("paymentForm"),
            "paymentMethod": obj.get("paymentMethod"),
            "paymentDueDate": obj.get("paymentDueDate"),
            "paymentID": obj.get("paymentID")
        })
        return _obj


