# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_event200_response_event_type import CreateEvent200ResponseEventType

class TestCreateEvent200ResponseEventType(unittest.TestCase):
    """CreateEvent200ResponseEventType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateEvent200ResponseEventType:
        """Test CreateEvent200ResponseEventType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateEvent200ResponseEventType`
        """
        model = CreateEvent200ResponseEventType()
        if include_optional:
            return CreateEvent200ResponseEventType(
                code = '',
                value = ''
            )
        else:
            return CreateEvent200ResponseEventType(
        )
        """

    def testCreateEvent200ResponseEventType(self):
        """Test CreateEvent200ResponseEventType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
