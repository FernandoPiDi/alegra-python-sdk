# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_payroll_request_government_data_deducciones_libranzas_libranza_inner import CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner

class TestCreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner(unittest.TestCase):
    """CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner:
        """Test CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner`
        """
        model = CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner()
        if include_optional:
            return CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner(
                descripcion = '',
                deduccion = 1.337
            )
        else:
            return CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner(
                descripcion = '',
                deduccion = 1.337,
        )
        """

    def testCreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner(self):
        """Test CreatePayrollRequestGovernmentDataDeduccionesLibranzasLibranzaInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
