# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_support_document_request_supplier_address import CreateSupportDocumentRequestSupplierAddress

class TestCreateSupportDocumentRequestSupplierAddress(unittest.TestCase):
    """CreateSupportDocumentRequestSupplierAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSupportDocumentRequestSupplierAddress:
        """Test CreateSupportDocumentRequestSupplierAddress
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSupportDocumentRequestSupplierAddress`
        """
        model = CreateSupportDocumentRequestSupplierAddress()
        if include_optional:
            return CreateSupportDocumentRequestSupplierAddress(
                address = '',
                city = '',
                department = '',
                postal_code = 'gCu2LC012345',
                country = ''
            )
        else:
            return CreateSupportDocumentRequestSupplierAddress(
                address = '',
                city = '',
        )
        """

    def testCreateSupportDocumentRequestSupplierAddress(self):
        """Test CreateSupportDocumentRequestSupplierAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
