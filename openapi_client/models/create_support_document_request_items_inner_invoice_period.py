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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CreateSupportDocumentRequestItemsInnerInvoicePeriod(BaseModel):
    """
    CreateSupportDocumentRequestItemsInnerInvoicePeriod
    """ # noqa: E501
    description_code: Union[StrictFloat, StrictInt] = Field(description="Este campo permite indicar la forma de generación y transmisión de la información, utilizando los siguientes códigos: 1 = Por operación o 2 = Acumulado semanal. <br><i>Grupo de información oficial DIAN &lt;DescriptionCode&gt;</i>", alias="descriptionCode")
    start_date: Optional[date] = Field(default=None, description="Aplica para las compras con reporte semanal. Indica la fecha en la que se realizó la transacción, y se incluirá dentro del acumulado correspondiente al reporte semanal. Este campo pasa a ser obligatorio cuando `descriptionCode` es igual a `2`. <br><i>Grupo de información oficial DIAN &lt;StartDate&gt;</i>", alias="startDate")
    __properties: ClassVar[List[str]] = ["descriptionCode", "startDate"]

    @field_validator('description_code')
    def description_code_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set([1, 2]):
            raise ValueError("must be one of enum values (1, 2)")
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
        """Create an instance of CreateSupportDocumentRequestItemsInnerInvoicePeriod from a JSON string"""
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
        """Create an instance of CreateSupportDocumentRequestItemsInnerInvoicePeriod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "descriptionCode": obj.get("descriptionCode"),
            "startDate": obj.get("startDate")
        })
        return _obj


