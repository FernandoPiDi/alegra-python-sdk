# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_invoice_request_company import CreateInvoiceRequestCompany

class TestCreateInvoiceRequestCompany(unittest.TestCase):
    """CreateInvoiceRequestCompany unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateInvoiceRequestCompany:
        """Test CreateInvoiceRequestCompany
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateInvoiceRequestCompany`
        """
        model = CreateInvoiceRequestCompany()
        if include_optional:
            return CreateInvoiceRequestCompany(
                id = '',
                organization_type = 1,
                identification_number = '012',
                dv = '0',
                name = '01234',
                trade_name = '0',
                regime_code = 'R-99-PN;O-13;O-48;O-23;R-99-PN;O-13;O-47;R-99-PN;R-99-PN;R-99-PN;R-99-PN;O-47;R-99-PN;O-13;O-13;O-13;O-49;O-48;O-47;O-15;O-48;R-99-PN;O-23;R-99-PN;O-47;R-99-PN;O-47;O-15;O-47',
                tax_code = openapi_client.models.create_invoice_request_company_tax_code.createInvoice_request_company_taxCode(
                    id = '01', ),
                economic_activities = [
                    '0480'
                    ],
                email = '',
                phone = '',
                address = None,
                tax_address = None,
                shareholders = [
                    openapi_client.models.create_invoice_request_company_shareholders_inner.createInvoice_request_company_shareholders_inner(
                        identification_number = '012', 
                        dv = '0', 
                        name = '01234', 
                        regime_code = 'R-99-PN;O-13;O-13;O-15;R-99-PN;O-13;O-47;R-99-PN;R-99-PN;R-99-PN;R-99-PN;O-13;R-99-PN;O-15;O-13;O-47;O-15;O-15;O-13;O-13;O-23;R-99-PN;O-13;R-99-PN;O-47;R-99-PN;O-13;O-23;O-13', 
                        percent = 0, 
                        tax_code = '01', )
                    ],
                contact = openapi_client.models.create_equivalent_document_pos_request_company_contact.createEquivalentDocumentPos_request_company_contact(
                    name = '', 
                    telefax = '', 
                    note = '', 
                    commercial_registration_number = '', )
            )
        else:
            return CreateInvoiceRequestCompany(
                id = '',
        )
        """

    def testCreateInvoiceRequestCompany(self):
        """Test CreateInvoiceRequestCompany"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
