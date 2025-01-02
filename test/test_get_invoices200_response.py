# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_invoices200_response import GetInvoices200Response

class TestGetInvoices200Response(unittest.TestCase):
    """GetInvoices200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetInvoices200Response:
        """Test GetInvoices200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetInvoices200Response`
        """
        model = GetInvoices200Response()
        if include_optional:
            return GetInvoices200Response(
                metadata = openapi_client.models.get_payrolls_200_response_metadata.getPayrolls_200_response_metadata(
                    from = '', 
                    to = '', 
                    results_count = 56, ),
                invoices = [
                    openapi_client.models.get_invoices_200_response_invoices_inner.getInvoices_200_response_invoices_inner(
                        id = '', 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = 'REGISTERED', 
                        legal_status = 'ACCEPTED', 
                        company_identification = '', 
                        customer_identification = '', 
                        cufe = '', 
                        prefix = '0', 
                        number = 1.337, 
                        full_number = '', 
                        government_response = openapi_client.models.get_test_set_by_government_id_200_response_emission_government_response.getTestSetByGovernmentId_200_response_emission_governmentResponse(
                            code = '', 
                            message = '', 
                            error_messages = [
                                ''
                                ], ), 
                        xml_file_name = '', 
                        zip_file_name = '', 
                        zip = '', 
                        qr_code_content = '', 
                        errors = [
                            openapi_client.models.create_equivalent_document_pos_200_response_equivalent_document_errors_inner.createEquivalentDocumentPos_200_response_equivalent_document_errors_inner(
                                code = '', 
                                message = '', )
                            ], )
                    ]
            )
        else:
            return GetInvoices200Response(
        )
        """

    def testGetInvoices200Response(self):
        """Test GetInvoices200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
