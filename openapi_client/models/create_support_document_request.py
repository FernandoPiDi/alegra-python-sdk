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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_client.models.create_support_document_request_billing_reference import CreateSupportDocumentRequestBillingReference
from openapi_client.models.create_support_document_request_company import CreateSupportDocumentRequestCompany
from openapi_client.models.create_support_document_request_discounts_and_charges_inner import CreateSupportDocumentRequestDiscountsAndChargesInner
from openapi_client.models.create_support_document_request_document_currency import CreateSupportDocumentRequestDocumentCurrency
from openapi_client.models.create_support_document_request_items_inner import CreateSupportDocumentRequestItemsInner
from openapi_client.models.create_support_document_request_order_reference import CreateSupportDocumentRequestOrderReference
from openapi_client.models.create_support_document_request_payments_inner import CreateSupportDocumentRequestPaymentsInner
from openapi_client.models.create_support_document_request_resolution import CreateSupportDocumentRequestResolution
from openapi_client.models.create_support_document_request_supplier import CreateSupportDocumentRequestSupplier
from openapi_client.models.create_support_document_request_total_amounts import CreateSupportDocumentRequestTotalAmounts
from typing import Optional, Set
from typing_extensions import Self

class CreateSupportDocumentRequest(BaseModel):
    """
    CreateSupportDocumentRequest
    """ # noqa: E501
    document_currency: Optional[CreateSupportDocumentRequestDocumentCurrency] = Field(default=None, alias="documentCurrency")
    number: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Número del documento soporte electrónico")
    resolution: CreateSupportDocumentRequestResolution
    company: CreateSupportDocumentRequestCompany
    supplier: CreateSupportDocumentRequestSupplier
    items: List[CreateSupportDocumentRequestItemsInner] = Field(description="Array que contiene el listado de articulos y/o servicios")
    payments: List[CreateSupportDocumentRequestPaymentsInner] = Field(description="Array con el listado de pagos. Grupo de campos para información relacionadas con el pago de la factura. <br><i>Grupo de información oficial DIAN &lt;PaymentMeans&gt;</i>")
    discounts_and_charges: Optional[List[CreateSupportDocumentRequestDiscountsAndChargesInner]] = Field(default=None, description="Descuentos Descuentos o cargos a nivel del DSE, estos descuentos o cargos no afectan las bases gravables. Si se desea agregar un descuento o cargo que afecte la base gravable se debe informan a nivel de items en el elemento `discountAmount`. <br><i>Grupo de información oficial DIAN &lt;AllowanceCharge&gt;</i>", alias="discountsAndCharges")
    total_amounts: CreateSupportDocumentRequestTotalAmounts = Field(alias="totalAmounts")
    notes: Optional[Annotated[str, Field(min_length=15, strict=True, max_length=5000)]] = Field(default=None, description="Información adicional: Texto libre, relativo al documento")
    order_reference: Optional[CreateSupportDocumentRequestOrderReference] = Field(default=None, alias="orderReference")
    billing_reference: Optional[CreateSupportDocumentRequestBillingReference] = Field(default=None, alias="billingReference")
    __properties: ClassVar[List[str]] = ["documentCurrency", "number", "resolution", "company", "supplier", "items", "payments", "discountsAndCharges", "totalAmounts", "notes", "orderReference", "billingReference"]

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
        """Create an instance of CreateSupportDocumentRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of document_currency
        if self.document_currency:
            _dict['documentCurrency'] = self.document_currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resolution
        if self.resolution:
            _dict['resolution'] = self.resolution.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company
        if self.company:
            _dict['company'] = self.company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of supplier
        if self.supplier:
            _dict['supplier'] = self.supplier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payments (list)
        _items = []
        if self.payments:
            for _item_payments in self.payments:
                if _item_payments:
                    _items.append(_item_payments.to_dict())
            _dict['payments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in discounts_and_charges (list)
        _items = []
        if self.discounts_and_charges:
            for _item_discounts_and_charges in self.discounts_and_charges:
                if _item_discounts_and_charges:
                    _items.append(_item_discounts_and_charges.to_dict())
            _dict['discountsAndCharges'] = _items
        # override the default output from pydantic by calling `to_dict()` of total_amounts
        if self.total_amounts:
            _dict['totalAmounts'] = self.total_amounts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order_reference
        if self.order_reference:
            _dict['orderReference'] = self.order_reference.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_reference
        if self.billing_reference:
            _dict['billingReference'] = self.billing_reference.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateSupportDocumentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "documentCurrency": CreateSupportDocumentRequestDocumentCurrency.from_dict(obj["documentCurrency"]) if obj.get("documentCurrency") is not None else None,
            "number": obj.get("number"),
            "resolution": CreateSupportDocumentRequestResolution.from_dict(obj["resolution"]) if obj.get("resolution") is not None else None,
            "company": CreateSupportDocumentRequestCompany.from_dict(obj["company"]) if obj.get("company") is not None else None,
            "supplier": CreateSupportDocumentRequestSupplier.from_dict(obj["supplier"]) if obj.get("supplier") is not None else None,
            "items": [CreateSupportDocumentRequestItemsInner.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "payments": [CreateSupportDocumentRequestPaymentsInner.from_dict(_item) for _item in obj["payments"]] if obj.get("payments") is not None else None,
            "discountsAndCharges": [CreateSupportDocumentRequestDiscountsAndChargesInner.from_dict(_item) for _item in obj["discountsAndCharges"]] if obj.get("discountsAndCharges") is not None else None,
            "totalAmounts": CreateSupportDocumentRequestTotalAmounts.from_dict(obj["totalAmounts"]) if obj.get("totalAmounts") is not None else None,
            "notes": obj.get("notes"),
            "orderReference": CreateSupportDocumentRequestOrderReference.from_dict(obj["orderReference"]) if obj.get("orderReference") is not None else None,
            "billingReference": CreateSupportDocumentRequestBillingReference.from_dict(obj["billingReference"]) if obj.get("billingReference") is not None else None
        })
        return _obj


