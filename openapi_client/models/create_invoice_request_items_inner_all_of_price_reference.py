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
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CreateInvoiceRequestItemsInnerAllOfPriceReference(BaseModel):
    """
    Si se proporciona un precio de referencia, el atributo \"price\" debe ser cero (0.00), ya que se considera una muestra o regalo comercial. <br><i>Campo oficial DIAN &lt;AlternativeConditionPrice&gt;</i>
    """ # noqa: E501
    price_amount: Union[Annotated[float, Field(strict=True, ge=0.01)], Annotated[int, Field(strict=True, ge=1)]] = Field(description="Valor del artículo o servicio. Este precio se deberá utilizar para calcular el impuesto correspondiente. <br><i>Campo oficial DIAN &lt;PriceAmount&gt;</i>", alias="priceAmount")
    price_type_code: StrictStr = Field(description="Deberá contener uno de los siguientes valores posibles de acuerdo al precio informado en el elemento \"priceAmount\":<br>\"1\": Valor comercial; \"2\": Valor en Inventarios; \"3\": Otro valor<br><i>Campo oficial DIAN &lt;PriceTypeCode&gt;</i>", alias="priceTypeCode")
    __properties: ClassVar[List[str]] = ["priceAmount", "priceTypeCode"]

    @field_validator('price_type_code')
    def price_type_code_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['1', '2', '3']):
            raise ValueError("must be one of enum values ('1', '2', '3')")
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
        """Create an instance of CreateInvoiceRequestItemsInnerAllOfPriceReference from a JSON string"""
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
        """Create an instance of CreateInvoiceRequestItemsInnerAllOfPriceReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "priceAmount": obj.get("priceAmount"),
            "priceTypeCode": obj.get("priceTypeCode")
        })
        return _obj


