# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_support_document_request_supplier import CreateSupportDocumentRequestSupplier

class TestCreateSupportDocumentRequestSupplier(unittest.TestCase):
    """CreateSupportDocumentRequestSupplier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSupportDocumentRequestSupplier:
        """Test CreateSupportDocumentRequestSupplier
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSupportDocumentRequestSupplier`
        """
        model = CreateSupportDocumentRequestSupplier()
        if include_optional:
            return CreateSupportDocumentRequestSupplier(
                name = '',
                origin = '10',
                organization_type = 1,
                identification_type = '21',
                identification_number = '',
                dv = '0',
                regime_code = 'R-99-PN;O-15;O-47;O-48;R-99-PN;O-15;O-15;R-99-PN;R-99-PN;R-99-PN;R-99-PN;O-47;R-99-PN;O-15;O-23;O-47;O-15;O-15;O-15;O-47;O-47;R-99-PN;O-48;R-99-PN;O-49;R-99-PN;O-49;O-48;O-49',
                tax_code = '01',
                address = openapi_client.models.create_support_document_request_supplier_address.createSupportDocument_request_supplier_address(
                    address = '', 
                    city = '', 
                    department = '', 
                    postal_code = 'gCu2LC012345', 
                    country = '', )
            )
        else:
            return CreateSupportDocumentRequestSupplier(
                name = '',
                organization_type = 1,
                identification_type = '21',
                identification_number = '',
                address = openapi_client.models.create_support_document_request_supplier_address.createSupportDocument_request_supplier_address(
                    address = '', 
                    city = '', 
                    department = '', 
                    postal_code = 'gCu2LC012345', 
                    country = '', ),
        )
        """

    def testCreateSupportDocumentRequestSupplier(self):
        """Test CreateSupportDocumentRequestSupplier"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
