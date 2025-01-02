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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_client.models.create_support_document_request_supplier_address import CreateSupportDocumentRequestSupplierAddress
from typing import Optional, Set
from typing_extensions import Self

class CreateSupportDocumentRequestSupplier(BaseModel):
    """
    Objeto que contiene la información del proveedor del documento electrónico
    """ # noqa: E501
    name: StrictStr = Field(description="Nombre del proveedor")
    origin: Optional[Annotated[str, Field(strict=True, max_length=2)]] = Field(default=None, description="Indicador de procedencia del vendedor (Residente fiscal en Colombia [`10`] o No residente fiscal [`11`]). Se debe colocar el Código que corresponda de la tabla de tipos de procedencia del vendedor de la DIAN")
    organization_type: Union[Annotated[float, Field(strict=True)], Annotated[int, Field(strict=True)]] = Field(description="Tipo de organización jurídica. Se debe colocar el Código que corresponda de la tabla de tipos de organización jurídica de la DIAN", alias="organizationType")
    identification_type: Annotated[str, Field(strict=True, max_length=2)] = Field(description="Tipo de documento de identificación del proveedor. Se debe colocar el Código que corresponda de la tabla de tipos de identificación de la DIAN", alias="identificationType")
    identification_number: StrictStr = Field(description="Número de indentificación del proveedor", alias="identificationNumber")
    dv: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="DV del NIT del proveedor. Es obligatorio si identificationType = 31")
    regime_code: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Régimen al que pertenece el proveedor. Se debe colocar el Código que corresponda de la tabla de tipos de régimen/responsabilidades fiscales de la DIAN. Para reportar varias obligaciones / responsabilidades, se deben reportar separando cada uno de los valores de la lista con ';'. Ejemplo O‐13;O‐15;", alias="regimeCode")
    tax_code: Optional[StrictStr] = Field(default=None, description="Identificador del tributo. Se debe colocar el Código que corresponda de la tabla de tipos de tributos de la DIAN. Valores posibles: `ZZ`: 'No Aplica'(<i>Valor default</i>), `01`: IVA. <br><i>Campo oficial DIAN &lt;TaxScheme&gt;</i>", alias="taxCode")
    address: CreateSupportDocumentRequestSupplierAddress
    __properties: ClassVar[List[str]] = ["name", "origin", "organizationType", "identificationType", "identificationNumber", "dv", "regimeCode", "taxCode", "address"]

    @field_validator('origin')
    def origin_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['10', '11']):
            raise ValueError("must be one of enum values ('10', '11')")
        return value

    @field_validator('organization_type')
    def organization_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set([1, 2]):
            raise ValueError("must be one of enum values (1, 2)")
        return value

    @field_validator('identification_type')
    def identification_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['21', '22', '31', '41', '42', '47', '50']):
            raise ValueError("must be one of enum values ('21', '22', '31', '41', '42', '47', '50')")
        return value

    @field_validator('dv')
    def dv_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]{1})$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]{1})$/")
        return value

    @field_validator('regime_code')
    def regime_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(O-(15|23|47|48|49)|R-99-PN)(;(O-(15|23|47|48|49)|R-99-PN))*$", value):
            raise ValueError(r"must validate the regular expression /^(O-(15|23|47|48|49)|R-99-PN)(;(O-(15|23|47|48|49)|R-99-PN))*$/")
        return value

    @field_validator('tax_code')
    def tax_code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['01', 'ZZ']):
            raise ValueError("must be one of enum values ('01', 'ZZ')")
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
        """Create an instance of CreateSupportDocumentRequestSupplier from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateSupportDocumentRequestSupplier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "origin": obj.get("origin"),
            "organizationType": obj.get("organizationType"),
            "identificationType": obj.get("identificationType"),
            "identificationNumber": obj.get("identificationNumber"),
            "dv": obj.get("dv"),
            "regimeCode": obj.get("regimeCode"),
            "taxCode": obj.get("taxCode"),
            "address": CreateSupportDocumentRequestSupplierAddress.from_dict(obj["address"]) if obj.get("address") is not None else None
        })
        return _obj


