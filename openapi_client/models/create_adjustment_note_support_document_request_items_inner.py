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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_client.models.create_support_document_request_items_inner_standard_code import CreateSupportDocumentRequestItemsInnerStandardCode
from openapi_client.models.create_support_document_request_items_inner_taxes_inner import CreateSupportDocumentRequestItemsInnerTaxesInner
from typing import Optional, Set
from typing_extensions import Self

class CreateAdjustmentNoteSupportDocumentRequestItemsInner(BaseModel):
    """
    Objeto que contiene la información del listado de articulos y/o servicios. <br><i>Grupo de información oficial DIAN &lt;InvoiceLine&gt;</i>
    """ # noqa: E501
    standard_code: CreateSupportDocumentRequestItemsInnerStandardCode = Field(alias="standardCode")
    sellers_item_identification: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=50)]] = Field(default=None, description="Grupo de datos de identificación del artículo o servicio de acuerdo con el vendedor. <br><i>Grupo de información oficial DIAN &lt;SellersItemIdentification&gt;</i>", alias="sellersItemIdentification")
    description: Annotated[str, Field(min_length=1, strict=True, max_length=300)] = Field(description="Nombre y descripción del articulo y/o servicio que se está vendiendo en esta linea del documento. <br><i>Campo oficial DIAN &lt;Description&gt;</i>")
    pack_size: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Número de productos por empaque. <br><i>Campo oficial DIAN &lt;PackSizeNumeric&gt;</i>", alias="packSize")
    brand_name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default=None, description="Marca del artículo. <br><i>Campo oficial DIAN &lt;BrandName&gt;</i>", alias="brandName")
    model_name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default=None, description="Modelo del artículo. <br><i>Campo oficial DIAN &lt;ModelName&gt;</i>", alias="modelName")
    price: Union[StrictFloat, StrictInt] = Field(description="Precio del articulo y/o servicio. <br><i>Campo oficial DIAN &lt;PriceAmount&gt;</i>")
    discount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Porcentaje de descuento del articulo y/o servicio. Se debe informar a nivel de ítem, si y solamente si el descuento afecta la base gravable del ítem. <br><i>Campo oficial DIAN &lt;/cac:AllowanceCharge/cbc:MultiplierFactorNumeric&gt;</i>")
    discount_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Valor de descuento del articulo y/o servicio. Se debe informar a nivel de ítem, si y solamente si el descuento afecta la base gravable del ítem. <br><i>Campo oficial DIAN &lt;/cac:AllowanceCharge/cbc:Amount&gt;</i>", alias="discountAmount")
    charge: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Porcentaje de cargo adicional aplicado articulo y/o servicio")
    charge_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Valor del cargo adicional del articulo y/o servicio", alias="chargeAmount")
    quantity: Union[StrictFloat, StrictInt] = Field(description="Cantidad del articulo y/o servicio. <br><i>Campo oficial DIAN &lt;InvoicedQuantity&gt;</i>")
    unit_code: StrictStr = Field(description="Código de Unidad de medida del articulo y/o servicio. Se debe colocar el Código que corresponda de la tabla de unidades de la DIAN. <br><i>Campo oficial DIAN &lt;@unitCode&gt;</i>", alias="unitCode")
    note: Optional[StrictStr] = Field(default=None, description="Información Adicional o texto libre para añadir información del articulo y/o servicio. <br><i>Campo oficial DIAN &lt;Note&gt;</i>")
    subtotal: Union[StrictFloat, StrictInt] = Field(description="Subtotal del articulo y/o servicio. El subtotal de la línea es igual a la Cantidad x Precio Unidad menos Descuentos más Recargos que apliquen al articulo y/o servicio. <br><i>Campo oficial DIAN &lt;LineExtensionAmount&gt;</i>")
    tax_amount: Union[StrictFloat, StrictInt] = Field(description="Valor total de los impuestos aplicados al articulo y/o servicio.", alias="taxAmount")
    taxes: Optional[List[CreateSupportDocumentRequestItemsInnerTaxesInner]] = Field(default=None, description="Array que contiene el listado de tributos/impuestos que aplican al articulo y/o servicio")
    __properties: ClassVar[List[str]] = ["standardCode", "sellersItemIdentification", "description", "packSize", "brandName", "modelName", "price", "discount", "discountAmount", "charge", "chargeAmount", "quantity", "unitCode", "note", "subtotal", "taxAmount", "taxes"]

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
        """Create an instance of CreateAdjustmentNoteSupportDocumentRequestItemsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of standard_code
        if self.standard_code:
            _dict['standardCode'] = self.standard_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in taxes (list)
        _items = []
        if self.taxes:
            for _item_taxes in self.taxes:
                if _item_taxes:
                    _items.append(_item_taxes.to_dict())
            _dict['taxes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateAdjustmentNoteSupportDocumentRequestItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "standardCode": CreateSupportDocumentRequestItemsInnerStandardCode.from_dict(obj["standardCode"]) if obj.get("standardCode") is not None else None,
            "sellersItemIdentification": obj.get("sellersItemIdentification"),
            "description": obj.get("description"),
            "packSize": obj.get("packSize"),
            "brandName": obj.get("brandName"),
            "modelName": obj.get("modelName"),
            "price": obj.get("price"),
            "discount": obj.get("discount"),
            "discountAmount": obj.get("discountAmount"),
            "charge": obj.get("charge"),
            "chargeAmount": obj.get("chargeAmount"),
            "quantity": obj.get("quantity"),
            "unitCode": obj.get("unitCode"),
            "note": obj.get("note"),
            "subtotal": obj.get("subtotal"),
            "taxAmount": obj.get("taxAmount"),
            "taxes": [CreateSupportDocumentRequestItemsInnerTaxesInner.from_dict(_item) for _item in obj["taxes"]] if obj.get("taxes") is not None else None
        })
        return _obj


