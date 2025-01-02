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
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.get_debit_notes200_response_invoices_inner import GetDebitNotes200ResponseInvoicesInner
from openapi_client.models.get_payrolls200_response_metadata import GetPayrolls200ResponseMetadata
from typing import Optional, Set
from typing_extensions import Self

class GetDebitNotes200Response(BaseModel):
    """
    GetDebitNotes200Response
    """ # noqa: E501
    metadata: Optional[GetPayrolls200ResponseMetadata] = None
    invoices: Optional[List[GetDebitNotes200ResponseInvoicesInner]] = Field(default=None, description="Array con Notas Débito / Documentos")
    __properties: ClassVar[List[str]] = ["metadata", "invoices"]

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
        """Create an instance of GetDebitNotes200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in invoices (list)
        _items = []
        if self.invoices:
            for _item_invoices in self.invoices:
                if _item_invoices:
                    _items.append(_item_invoices.to_dict())
            _dict['invoices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetDebitNotes200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metadata": GetPayrolls200ResponseMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "invoices": [GetDebitNotes200ResponseInvoicesInner.from_dict(_item) for _item in obj["invoices"]] if obj.get("invoices") is not None else None
        })
        return _obj


