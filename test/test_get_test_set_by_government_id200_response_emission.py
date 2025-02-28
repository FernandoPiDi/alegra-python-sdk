# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_test_set_by_government_id200_response_emission import GetTestSetByGovernmentId200ResponseEmission

class TestGetTestSetByGovernmentId200ResponseEmission(unittest.TestCase):
    """GetTestSetByGovernmentId200ResponseEmission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTestSetByGovernmentId200ResponseEmission:
        """Test GetTestSetByGovernmentId200ResponseEmission
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTestSetByGovernmentId200ResponseEmission`
        """
        model = GetTestSetByGovernmentId200ResponseEmission()
        if include_optional:
            return GetTestSetByGovernmentId200ResponseEmission(
                id = '',
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'REGISTERED',
                legal_status = 'ACCEPTED',
                company_identification = '',
                employee_identification = '',
                cune = '',
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
                zip_file_name = ''
            )
        else:
            return GetTestSetByGovernmentId200ResponseEmission(
        )
        """

    def testGetTestSetByGovernmentId200ResponseEmission(self):
        """Test GetTestSetByGovernmentId200ResponseEmission"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
