# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_test_set200_response import CreateTestSet200Response

class TestCreateTestSet200Response(unittest.TestCase):
    """CreateTestSet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTestSet200Response:
        """Test CreateTestSet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTestSet200Response`
        """
        model = CreateTestSet200Response()
        if include_optional:
            return CreateTestSet200Response(
                test_sets = [
                    openapi_client.models.create_test_set_200_response_test_sets_inner.createTestSet_200_response_testSets_inner(
                        id = '', 
                        type = 'payrolls', 
                        government_id = '', 
                        status = 'ACCEPTED', )
                    ]
            )
        else:
            return CreateTestSet200Response(
        )
        """

    def testCreateTestSet200Response(self):
        """Test CreateTestSet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
