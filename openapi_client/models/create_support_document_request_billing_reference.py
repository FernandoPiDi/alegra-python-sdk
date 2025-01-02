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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CreateSupportDocumentRequestBillingReference(BaseModel):
    """
    Exclusivo para referenciar la Nota de Ajuste que dio origen al presente Documento Soporte Electrónico (DSE). Incluye los datos clave de la Nota de Ajuste, como el número, la fecha de emisión y el motivo del ajuste. <br><i>Campo oficial DIAN &lt;BillingReference&gt;</i>
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Id registrado por la API E-providers, en caso de que el documento de referencia haya sido emitido a través de E-providers solo se necesita este dato para identificar el documento, de lo contratrio deben enviarse los campos `fullNumber`, `cuds` y `date`.")
    full_number: Optional[StrictStr] = Field(default=None, description="Prefijo + Número de la nota de ajuste referenciada. <br><i>Campo oficial DIAN &lt;ID&gt;</i>", alias="fullNumber")
    cuds: Optional[StrictStr] = Field(default=None, description="CUDS de la nota de ajuste relacionada. <br><i>Campo oficial DIAN &lt;UUID&gt;</i>")
    var_date: Optional[date] = Field(default=None, description="Fecha de generación de la nota de ajuste relacionada. <br><i>Campo oficial DIAN &lt;ID&gt;</i>", alias="date")
    __properties: ClassVar[List[str]] = ["id", "fullNumber", "cuds", "date"]

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
        """Create an instance of CreateSupportDocumentRequestBillingReference from a JSON string"""
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
        """Create an instance of CreateSupportDocumentRequestBillingReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "fullNumber": obj.get("fullNumber"),
            "cuds": obj.get("cuds"),
            "date": obj.get("date")
        })
        return _obj


