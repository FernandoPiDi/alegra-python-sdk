# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_invoice_request_health_sector_general import CreateInvoiceRequestHealthSectorGeneral

class TestCreateInvoiceRequestHealthSectorGeneral(unittest.TestCase):
    """CreateInvoiceRequestHealthSectorGeneral unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateInvoiceRequestHealthSectorGeneral:
        """Test CreateInvoiceRequestHealthSectorGeneral
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateInvoiceRequestHealthSectorGeneral`
        """
        model = CreateInvoiceRequestHealthSectorGeneral()
        if include_optional:
            return CreateInvoiceRequestHealthSectorGeneral(
                service_provider_code = '',
                payment_method = '',
                benefits_plan_type = '',
                contract_number = '',
                policy_number = '',
                prepaid_payments = [
                    openapi_client.models.create_invoice_request_health_sector_general_prepaid_payments_inner.createInvoice_request_healthSectorGeneral_prepaidPayments_inner(
                        code = '01', 
                        amount = 0, 
                        received_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), )
                    ],
                service_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                service_end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                operation_type = 'SS-CUFE'
            )
        else:
            return CreateInvoiceRequestHealthSectorGeneral(
                service_provider_code = '',
                payment_method = '',
                benefits_plan_type = '',
                prepaid_payments = [
                    openapi_client.models.create_invoice_request_health_sector_general_prepaid_payments_inner.createInvoice_request_healthSectorGeneral_prepaidPayments_inner(
                        code = '01', 
                        amount = 0, 
                        received_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), )
                    ],
                service_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                service_end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                operation_type = 'SS-CUFE',
        )
        """

    def testCreateInvoiceRequestHealthSectorGeneral(self):
        """Test CreateInvoiceRequestHealthSectorGeneral"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
