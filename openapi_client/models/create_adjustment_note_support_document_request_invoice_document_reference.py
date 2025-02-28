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

class CreateAdjustmentNoteSupportDocumentRequestInvoiceDocumentReference(BaseModel):
    """
    CreateAdjustmentNoteSupportDocumentRequestInvoiceDocumentReference
    """ # noqa: E501
    id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Id registrado por la API E-providers, en caso de que el documento de referencia haya sido emitido a través de E-providers solo se necesita este dato para identificar el documento. En caso de que no se especifique los campos `fullNumber` y `cuds` son obligatorios.")
    full_number: Optional[StrictStr] = Field(default=None, description="Número del Documento Soporte al que se hace referencia. (Prefijo + Número). Se indica en caso de que sea un documento equivalente emitido con otro proveedor y/o el id no se especifique. <br><i>Campo oficial DIAN &lt;ID&gt;</i>", alias="fullNumber")
    cuds: Optional[StrictStr] = Field(default=None, description="Cude del Documento Soporte relacionado. Se indica en caso de que sea un documento equivalente emitido con otro proveedor y/o el id no se especifique. <br><i>Campo oficial DIAN &lt;UUID&gt;</i>")
    var_date: Optional[StrictStr] = Field(default=None, description="Fecha del documento referenciado. <br><i>Campo oficial DIAN &lt;IssueDate&gt;</i>", alias="date")
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
        """Create an instance of CreateAdjustmentNoteSupportDocumentRequestInvoiceDocumentReference from a JSON string"""
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
        """Create an instance of CreateAdjustmentNoteSupportDocumentRequestInvoiceDocumentReference from a dict"""
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


