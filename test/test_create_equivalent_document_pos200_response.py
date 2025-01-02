# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_equivalent_document_pos200_response import CreateEquivalentDocumentPos200Response

class TestCreateEquivalentDocumentPos200Response(unittest.TestCase):
    """CreateEquivalentDocumentPos200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateEquivalentDocumentPos200Response:
        """Test CreateEquivalentDocumentPos200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateEquivalentDocumentPos200Response`
        """
        model = CreateEquivalentDocumentPos200Response()
        if include_optional:
            return CreateEquivalentDocumentPos200Response(
                equivalent_document = openapi_client.models.create_equivalent_document_pos_200_response_equivalent_document.createEquivalentDocumentPos_200_response_equivalent_document(
                    id = '', 
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    status = 'REGISTERED', 
                    legal_status = 'ACCEPTED', 
                    company_identification = '', 
                    cude = '', 
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
                    qr_code_content = '', 
                    errors = [
                        openapi_client.models.create_equivalent_document_pos_200_response_equivalent_document_errors_inner.createEquivalentDocumentPos_200_response_equivalent_document_errors_inner(
                            code = '', 
                            message = '', )
                        ], )
            )
        else:
            return CreateEquivalentDocumentPos200Response(
        )
        """

    def testCreateEquivalentDocumentPos200Response(self):
        """Test CreateEquivalentDocumentPos200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
