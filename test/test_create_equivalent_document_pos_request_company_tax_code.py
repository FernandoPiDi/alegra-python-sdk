# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_equivalent_document_pos_request_company_tax_code import CreateEquivalentDocumentPosRequestCompanyTaxCode

class TestCreateEquivalentDocumentPosRequestCompanyTaxCode(unittest.TestCase):
    """CreateEquivalentDocumentPosRequestCompanyTaxCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateEquivalentDocumentPosRequestCompanyTaxCode:
        """Test CreateEquivalentDocumentPosRequestCompanyTaxCode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateEquivalentDocumentPosRequestCompanyTaxCode`
        """
        model = CreateEquivalentDocumentPosRequestCompanyTaxCode()
        if include_optional:
            return CreateEquivalentDocumentPosRequestCompanyTaxCode(
                id = '',
                name = ''
            )
        else:
            return CreateEquivalentDocumentPosRequestCompanyTaxCode(
                id = '',
        )
        """

    def testCreateEquivalentDocumentPosRequestCompanyTaxCode(self):
        """Test CreateEquivalentDocumentPosRequestCompanyTaxCode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
