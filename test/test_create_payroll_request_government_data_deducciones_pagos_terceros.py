# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_payroll_request_government_data_deducciones_pagos_terceros import CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros

class TestCreatePayrollRequestGovernmentDataDeduccionesPagosTerceros(unittest.TestCase):
    """CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros:
        """Test CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros`
        """
        model = CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros()
        if include_optional:
            return CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros(
                pago_tercero = [
                    1.337
                    ]
            )
        else:
            return CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros(
        )
        """

    def testCreatePayrollRequestGovernmentDataDeduccionesPagosTerceros(self):
        """Test CreatePayrollRequestGovernmentDataDeduccionesPagosTerceros"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
