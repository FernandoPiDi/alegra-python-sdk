# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_payroll_request_government_data_devengados_cesantias import CreatePayrollRequestGovernmentDataDevengadosCesantias

class TestCreatePayrollRequestGovernmentDataDevengadosCesantias(unittest.TestCase):
    """CreatePayrollRequestGovernmentDataDevengadosCesantias unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePayrollRequestGovernmentDataDevengadosCesantias:
        """Test CreatePayrollRequestGovernmentDataDevengadosCesantias
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePayrollRequestGovernmentDataDevengadosCesantias`
        """
        model = CreatePayrollRequestGovernmentDataDevengadosCesantias()
        if include_optional:
            return CreatePayrollRequestGovernmentDataDevengadosCesantias(
                pago = 1.337,
                porcentaje = 1.337,
                pago_intereses = 1.337
            )
        else:
            return CreatePayrollRequestGovernmentDataDevengadosCesantias(
                pago = 1.337,
                porcentaje = 1.337,
                pago_intereses = 1.337,
        )
        """

    def testCreatePayrollRequestGovernmentDataDevengadosCesantias(self):
        """Test CreatePayrollRequestGovernmentDataDevengadosCesantias"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
