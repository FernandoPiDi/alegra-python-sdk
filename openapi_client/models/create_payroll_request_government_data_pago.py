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

class CreatePayrollRequestGovernmentDataPago(BaseModel):
    """
    Objeto con la información del pago del documento
    """ # noqa: E501
    forma: Annotated[str, Field(strict=True, max_length=1)] = Field(description="Formas de Pago del Documento. Se debe colocar el Codigo que corresponda de la tabla de formas de pago de la DIAN", alias="Forma")
    metodo: Annotated[str, Field(strict=True, max_length=2)] = Field(description="Metodos de Pago del Documento. Se debe colocar el Codigo que corresponda de la tabla de métodos de pago de la DIAN", alias="Metodo")
    banco: Optional[StrictStr] = Field(default=None, description="Si el método de pago se realiza de forma bancaria. Se debe colocar el nombre de la entidad bancaria donde el trabajador tiene su cuenta para pago de nómina.", alias="Banco")
    tipo_cuenta: Optional[StrictStr] = Field(default=None, description="Tipo de Cuenta Bancaria del Empleado donde se realiza la consignación", alias="TipoCuenta")
    numero_cuenta: Optional[StrictStr] = Field(default=None, description="Numero de Cuenta Bancaria del Empleado donde se realiza la consignación", alias="NumeroCuenta")
    __properties: ClassVar[List[str]] = ["Forma", "Metodo", "Banco", "TipoCuenta", "NumeroCuenta"]

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
        """Create an instance of CreatePayrollRequestGovernmentDataPago from a JSON string"""
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
        """Create an instance of CreatePayrollRequestGovernmentDataPago from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Forma": obj.get("Forma"),
            "Metodo": obj.get("Metodo"),
            "Banco": obj.get("Banco"),
            "TipoCuenta": obj.get("TipoCuenta"),
            "NumeroCuenta": obj.get("NumeroCuenta")
        })
        return _obj


