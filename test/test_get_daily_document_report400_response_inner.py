# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_daily_document_report400_response_inner import GetDailyDocumentReport400ResponseInner

class TestGetDailyDocumentReport400ResponseInner(unittest.TestCase):
    """GetDailyDocumentReport400ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDailyDocumentReport400ResponseInner:
        """Test GetDailyDocumentReport400ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDailyDocumentReport400ResponseInner`
        """
        model = GetDailyDocumentReport400ResponseInner()
        if include_optional:
            return GetDailyDocumentReport400ResponseInner(
                code = '',
                message = ''
            )
        else:
            return GetDailyDocumentReport400ResponseInner(
                message = '',
        )
        """

    def testGetDailyDocumentReport400ResponseInner(self):
        """Test GetDailyDocumentReport400ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
