# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_identification_types200_response import GetIdentificationTypes200Response

class TestGetIdentificationTypes200Response(unittest.TestCase):
    """GetIdentificationTypes200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetIdentificationTypes200Response:
        """Test GetIdentificationTypes200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetIdentificationTypes200Response`
        """
        model = GetIdentificationTypes200Response()
        if include_optional:
            return GetIdentificationTypes200Response(
                table = [
                    openapi_client.models.get_identification_types_200_response_table_inner.getIdentificationTypes_200_response_table_inner(
                        code = '', 
                        value = '', )
                    ]
            )
        else:
            return GetIdentificationTypes200Response(
        )
        """

    def testGetIdentificationTypes200Response(self):
        """Test GetIdentificationTypes200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
