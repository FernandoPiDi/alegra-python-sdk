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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_client.models.create_event200_response_event_receiver import CreateEvent200ResponseEventReceiver
from openapi_client.models.create_event200_response_event_type import CreateEvent200ResponseEventType
from openapi_client.models.get_test_set_by_government_id200_response_emission_government_response import GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse
from typing import Optional, Set
from typing_extensions import Self

class CreateEvent200ResponseEvent(BaseModel):
    """
    CreateEvent200ResponseEvent
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Id del evento emitido")
    type: Optional[CreateEvent200ResponseEventType] = None
    var_date: Optional[datetime] = Field(default=None, description="Fecha de emisión del evento", alias="date")
    legal_status: Optional[StrictStr] = Field(default=None, description="Estado legal del evento ante la DIAN", alias="legalStatus")
    company_identification: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Identificación del emisor del evento", alias="companyIdentification")
    cude: Optional[StrictStr] = Field(default=None, description="del documento electrónico del evento")
    associated_document_id: Optional[StrictStr] = Field(default=None, description="Código único de la factura electrónica asociada al evento", alias="associatedDocumentId")
    receiver: Optional[CreateEvent200ResponseEventReceiver] = None
    prefix: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Prefijo del evento electrónico")
    number: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Número de evento electronico")
    full_number: Optional[StrictStr] = Field(default=None, description="Número de nota débito electrónica (Incluye prefijo y número)", alias="fullNumber")
    government_response: Optional[GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse] = Field(default=None, alias="governmentResponse")
    xml_file_name: Optional[StrictStr] = Field(default=None, description="Nombre del archivo XML que se envió a la DIAN", alias="xmlFileName")
    zip_file_name: Optional[StrictStr] = Field(default=None, description="Nombre del archivo Zip que se envió a la DIAN", alias="zipFileName")
    status: Optional[StrictStr] = Field(default=None, description="Estado del evento electrónico")
    __properties: ClassVar[List[str]] = ["id", "type", "date", "legalStatus", "companyIdentification", "cude", "associatedDocumentId", "receiver", "prefix", "number", "fullNumber", "governmentResponse", "xmlFileName", "zipFileName", "status"]

    @field_validator('legal_status')
    def legal_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACCEPTED', 'ACCEPTED_WITH_OBSERVATIONS', 'REJECTED']):
            raise ValueError("must be one of enum values ('ACCEPTED', 'ACCEPTED_WITH_OBSERVATIONS', 'REJECTED')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['REGISTERED', 'WAITING_RESPONSE', 'FAILED', 'SENT']):
            raise ValueError("must be one of enum values ('REGISTERED', 'WAITING_RESPONSE', 'FAILED', 'SENT')")
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
        """Create an instance of CreateEvent200ResponseEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of receiver
        if self.receiver:
            _dict['receiver'] = self.receiver.to_dict()
        # override the default output from pydantic by calling `to_dict()` of government_response
        if self.government_response:
            _dict['governmentResponse'] = self.government_response.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateEvent200ResponseEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": CreateEvent200ResponseEventType.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "date": obj.get("date"),
            "legalStatus": obj.get("legalStatus"),
            "companyIdentification": obj.get("companyIdentification"),
            "cude": obj.get("cude"),
            "associatedDocumentId": obj.get("associatedDocumentId"),
            "receiver": CreateEvent200ResponseEventReceiver.from_dict(obj["receiver"]) if obj.get("receiver") is not None else None,
            "prefix": obj.get("prefix"),
            "number": obj.get("number"),
            "fullNumber": obj.get("fullNumber"),
            "governmentResponse": GetTestSetByGovernmentId200ResponseEmissionGovernmentResponse.from_dict(obj["governmentResponse"]) if obj.get("governmentResponse") is not None else None,
            "xmlFileName": obj.get("xmlFileName"),
            "zipFileName": obj.get("zipFileName"),
            "status": obj.get("status")
        })
        return _obj


