# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_payroll_file200_response import GetPayrollFile200Response

class TestGetPayrollFile200Response(unittest.TestCase):
    """GetPayrollFile200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPayrollFile200Response:
        """Test GetPayrollFile200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPayrollFile200Response`
        """
        model = GetPayrollFile200Response()
        if include_optional:
            return GetPayrollFile200Response(
                file = openapi_client.models.get_payroll_file_200_response_file.getPayrollFile_200_response_file(
                    content = 'YQ==', )
            )
        else:
            return GetPayrollFile200Response(
        )
        """

    def testGetPayrollFile200Response(self):
        """Test GetPayrollFile200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
