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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class GetResolutions200ResponseResolutionsInner(BaseModel):
    """
    Objeto que contiene la información de la Resolución de Numeración de Facturas asociada al emisor de la factura electrónica en formato JSON según el estándar de la DIAN. <br><i>Grupo de información oficial DIAN &lt;InvoiceControl&gt;</i>
    """ # noqa: E501
    resolution_number: Annotated[str, Field(strict=True, max_length=14)] = Field(description="Número de Resolución o de Autorización: Número del código de la resolución otorgada para la numeración. <br><i>Campo oficial DIAN &lt;InvoiceAuthorization&gt;</i>", alias="resolutionNumber")
    prefix: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=4)]] = Field(default=None, description="Prefijo de la Resolución o Autorización. <br><i>Campo oficial DIAN &lt;Prefix&gt;</i>")
    min_number: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Valor inicial del rango de numeración. <br><i>Campo oficial DIAN &lt;From&gt;</i>", alias="minNumber")
    max_number: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Valor final del rango de numeración. <br><i>Campo oficial DIAN &lt;To&gt;</i>", alias="maxNumber")
    start_date: date = Field(description="Fecha de inicio de la autorización de la numeración. <br><i>Campo oficial DIAN &lt;StartDate&gt;</i>", alias="startDate")
    end_date: date = Field(description="Fecha final de la autorización de la numeración. <br><i>Campo oficial DIAN &lt;EndDate&gt;</i>", alias="endDate")
    technical_key: StrictStr = Field(description="Clave técnica del rango de facturación. <br><i>ClTec: Obligatorio para la generación del CUFE (Código Único de Factura Electrónica)</i>", alias="technicalKey")
    __properties: ClassVar[List[str]] = ["resolutionNumber", "prefix", "minNumber", "maxNumber", "startDate", "endDate", "technicalKey"]

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
        """Create an instance of GetResolutions200ResponseResolutionsInner from a JSON string"""
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
        """Create an instance of GetResolutions200ResponseResolutionsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resolutionNumber": obj.get("resolutionNumber"),
            "prefix": obj.get("prefix"),
            "minNumber": obj.get("minNumber"),
            "maxNumber": obj.get("maxNumber"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "technicalKey": obj.get("technicalKey")
        })
        return _obj


