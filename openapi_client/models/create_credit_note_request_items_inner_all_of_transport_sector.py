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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CreateCreditNoteRequestItemsInnerAllOfTransportSector(BaseModel):
    """
    Objeto que contiene los campos adicionales que hacen referencia al sector transporte de carga. Aplica solo para facturas de transporte, y se debe informar a nivel de ítem.
    """ # noqa: E501
    is_registered_in_rndc: Optional[StrictBool] = Field(default=None, description="True si el Bien o Servicio “B/S” reportado corresponde o no a una línea registrada en el RNDC.<br><i>Campo oficial DIAN &lt;@schemeID&gt;</i>", alias="isRegisteredInRNDC")
    number_rndc: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Número Radicado de Aceptación de la Remesa. Hace referencia al consecutivo único nacional que controla y entrega el RNDC.", alias="numberRNDC")
    number_remesa: Optional[Annotated[str, Field(strict=True, max_length=15)]] = Field(default=None, description="Número de Remesa. Hace referencia al número del consecutivo de la Remesa según codificación interna de cada empresa de transporte.", alias="numberRemesa")
    freight_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Valor del flete a cobrar por el servicio de transporte de la remesa.", alias="freightAmount")
    quantity_transported: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Cantidad transportada.", alias="quantityTransported")
    unit_code: Optional[Annotated[str, Field(strict=True, max_length=3)]] = Field(default=None, description="Unidad de medida. Se utilizará alguna de las dos codificaciones permitidas por el estándar. KGM: Kilogramos y GLL: Galones.", alias="unitCode")
    __properties: ClassVar[List[str]] = ["isRegisteredInRNDC", "numberRNDC", "numberRemesa", "freightAmount", "quantityTransported", "unitCode"]

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
        """Create an instance of CreateCreditNoteRequestItemsInnerAllOfTransportSector from a JSON string"""
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
        """Create an instance of CreateCreditNoteRequestItemsInnerAllOfTransportSector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isRegisteredInRNDC": obj.get("isRegisteredInRNDC"),
            "numberRNDC": obj.get("numberRNDC"),
            "numberRemesa": obj.get("numberRemesa"),
            "freightAmount": obj.get("freightAmount"),
            "quantityTransported": obj.get("quantityTransported"),
            "unitCode": obj.get("unitCode")
        })
        return _obj


