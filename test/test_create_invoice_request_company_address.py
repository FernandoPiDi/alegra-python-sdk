# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_invoice_request_company_address import CreateInvoiceRequestCompanyAddress

class TestCreateInvoiceRequestCompanyAddress(unittest.TestCase):
    """CreateInvoiceRequestCompanyAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateInvoiceRequestCompanyAddress:
        """Test CreateInvoiceRequestCompanyAddress
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateInvoiceRequestCompanyAddress`
        """
        model = CreateInvoiceRequestCompanyAddress()
        if include_optional:
            return CreateInvoiceRequestCompanyAddress(
                address = '',
                city = '',
                department = '',
                postal_code = 'gCu2LC012345'
            )
        else:
            return CreateInvoiceRequestCompanyAddress(
                address = '',
                city = '',
                department = '',
        )
        """

    def testCreateInvoiceRequestCompanyAddress(self):
        """Test CreateInvoiceRequestCompanyAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
