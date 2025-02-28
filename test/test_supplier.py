# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.supplier import Supplier

class TestSupplier(unittest.TestCase):
    """Supplier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Supplier:
        """Test Supplier
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Supplier`
        """
        model = Supplier()
        if include_optional:
            return Supplier(
                name = '',
                origin = '',
                organization_type = 1.337,
                identification_type = '',
                identification_number = '',
                dv = '0',
                regime_code = '',
                email = '',
                phone = '',
                address = openapi_client.models.get_companies_200_response_companies_inner_address.getCompanies_200_response_companies_inner_address(
                    address = '', 
                    city = '', 
                    department = '', 
                    country = '', )
            )
        else:
            return Supplier(
                name = '',
                organization_type = 1.337,
                identification_type = '',
                identification_number = '',
                address = openapi_client.models.get_companies_200_response_companies_inner_address.getCompanies_200_response_companies_inner_address(
                    address = '', 
                    city = '', 
                    department = '', 
                    country = '', ),
        )
        """

    def testSupplier(self):
        """Test Supplier"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
