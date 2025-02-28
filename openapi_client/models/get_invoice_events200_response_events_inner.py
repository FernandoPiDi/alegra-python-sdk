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
from openapi_client.models.get_invoice_events200_response_events_inner_document_reference import GetInvoiceEvents200ResponseEventsInnerDocumentReference
from openapi_client.models.get_invoice_events200_response_events_inner_issuer_party import GetInvoiceEvents200ResponseEventsInnerIssuerParty
from openapi_client.models.get_invoice_events200_response_events_inner_receiver_party import GetInvoiceEvents200ResponseEventsInnerReceiverParty
from typing import Optional, Set
from typing_extensions import Self

class GetInvoiceEvents200ResponseEventsInner(BaseModel):
    """
    GetInvoiceEvents200ResponseEventsInner
    """ # noqa: E501
    response_code: Optional[StrictStr] = Field(default=None, description="Código del evento", alias="responseCode")
    type: Optional[StrictStr] = Field(default=None, description="Descripción del tipo de evento")
    effective_time: Optional[StrictStr] = Field(default=None, description="Fecha y hora de emisión del evento", alias="effectiveTime")
    document_reference: Optional[GetInvoiceEvents200ResponseEventsInnerDocumentReference] = Field(default=None, alias="documentReference")
    issuer_party: Optional[GetInvoiceEvents200ResponseEventsInnerIssuerParty] = Field(default=None, alias="issuerParty")
    receiver_party: Optional[GetInvoiceEvents200ResponseEventsInnerReceiverParty] = Field(default=None, alias="receiverParty")
    __properties: ClassVar[List[str]] = ["responseCode", "type", "effectiveTime", "documentReference", "issuerParty", "receiverParty"]

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
        """Create an instance of GetInvoiceEvents200ResponseEventsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of document_reference
        if self.document_reference:
            _dict['documentReference'] = self.document_reference.to_dict()
        # override the default output from pydantic by calling `to_dict()` of issuer_party
        if self.issuer_party:
            _dict['issuerParty'] = self.issuer_party.to_dict()
        # override the default output from pydantic by calling `to_dict()` of receiver_party
        if self.receiver_party:
            _dict['receiverParty'] = self.receiver_party.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetInvoiceEvents200ResponseEventsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "responseCode": obj.get("responseCode"),
            "type": obj.get("type"),
            "effectiveTime": obj.get("effectiveTime"),
            "documentReference": GetInvoiceEvents200ResponseEventsInnerDocumentReference.from_dict(obj["documentReference"]) if obj.get("documentReference") is not None else None,
            "issuerParty": GetInvoiceEvents200ResponseEventsInnerIssuerParty.from_dict(obj["issuerParty"]) if obj.get("issuerParty") is not None else None,
            "receiverParty": GetInvoiceEvents200ResponseEventsInnerReceiverParty.from_dict(obj["receiverParty"]) if obj.get("receiverParty") is not None else None
        })
        return _obj


