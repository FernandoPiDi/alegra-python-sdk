# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.customer import Customer

class TestCustomer(unittest.TestCase):
    """Customer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Customer:
        """Test Customer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Customer`
        """
        model = Customer()
        if include_optional:
            return Customer(
                name = '',
                organization_type = 1.337,
                identification_type = '',
                identification_number = '',
                dv = '0',
                regime_code = '',
                tax_code = openapi_client.models.customer_tax_code.Customer_taxCode(
                    id = '', 
                    name = '', ),
                email = '',
                phone = '',
                address = openapi_client.models.get_companies_200_response_companies_inner_address.getCompanies_200_response_companies_inner_address(
                    address = '', 
                    city = '', 
                    department = '', 
                    country = '', ),
                contact = openapi_client.models.create_equivalent_document_pos_request_customer_contact.createEquivalentDocumentPos_request_customer_contact(
                    name = '', )
            )
        else:
            return Customer(
                name = '',
                identification_type = '',
                identification_number = '',
        )
        """

    def testCustomer(self):
        """Test Customer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
