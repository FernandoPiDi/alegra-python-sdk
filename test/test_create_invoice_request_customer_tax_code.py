# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_invoice_request_customer_tax_code import CreateInvoiceRequestCustomerTaxCode

class TestCreateInvoiceRequestCustomerTaxCode(unittest.TestCase):
    """CreateInvoiceRequestCustomerTaxCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateInvoiceRequestCustomerTaxCode:
        """Test CreateInvoiceRequestCustomerTaxCode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateInvoiceRequestCustomerTaxCode`
        """
        model = CreateInvoiceRequestCustomerTaxCode()
        if include_optional:
            return CreateInvoiceRequestCustomerTaxCode(
                id = '01'
            )
        else:
            return CreateInvoiceRequestCustomerTaxCode(
                id = '01',
        )
        """

    def testCreateInvoiceRequestCustomerTaxCode(self):
        """Test CreateInvoiceRequestCustomerTaxCode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
