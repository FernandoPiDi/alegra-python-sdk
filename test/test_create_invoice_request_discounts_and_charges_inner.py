# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_invoice_request_discounts_and_charges_inner import CreateInvoiceRequestDiscountsAndChargesInner

class TestCreateInvoiceRequestDiscountsAndChargesInner(unittest.TestCase):
    """CreateInvoiceRequestDiscountsAndChargesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateInvoiceRequestDiscountsAndChargesInner:
        """Test CreateInvoiceRequestDiscountsAndChargesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateInvoiceRequestDiscountsAndChargesInner`
        """
        model = CreateInvoiceRequestDiscountsAndChargesInner()
        if include_optional:
            return CreateInvoiceRequestDiscountsAndChargesInner(
                is_charge = True,
                reason = '',
                reason_code = '00',
                percentage_amount = 0,
                amount = 0,
                base_amount = 0
            )
        else:
            return CreateInvoiceRequestDiscountsAndChargesInner(
                is_charge = True,
                reason = '',
                percentage_amount = 0,
                amount = 0,
                base_amount = 0,
        )
        """

    def testCreateInvoiceRequestDiscountsAndChargesInner(self):
        """Test CreateInvoiceRequestDiscountsAndChargesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
