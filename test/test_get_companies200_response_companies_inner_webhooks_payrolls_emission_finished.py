# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_companies200_response_companies_inner_webhooks_payrolls_emission_finished import GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished

class TestGetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished(unittest.TestCase):
    """GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished:
        """Test GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished`
        """
        model = GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished()
        if include_optional:
            return GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished(
                url = '',
                headers = None,
                status = 'active'
            )
        else:
            return GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished(
                url = '',
        )
        """

    def testGetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished(self):
        """Test GetCompanies200ResponseCompaniesInnerWebhooksPayrollsEmissionFinished"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
