# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_support_document_request_resolution import CreateSupportDocumentRequestResolution

class TestCreateSupportDocumentRequestResolution(unittest.TestCase):
    """CreateSupportDocumentRequestResolution unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSupportDocumentRequestResolution:
        """Test CreateSupportDocumentRequestResolution
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSupportDocumentRequestResolution`
        """
        model = CreateSupportDocumentRequestResolution()
        if include_optional:
            return CreateSupportDocumentRequestResolution(
                resolution_number = '',
                prefix = '0',
                min_number = 1.337,
                max_number = 1.337,
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else:
            return CreateSupportDocumentRequestResolution(
                resolution_number = '',
                min_number = 1.337,
                max_number = 1.337,
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testCreateSupportDocumentRequestResolution(self):
        """Test CreateSupportDocumentRequestResolution"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
