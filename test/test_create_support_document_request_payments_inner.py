# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_support_document_request_payments_inner import CreateSupportDocumentRequestPaymentsInner

class TestCreateSupportDocumentRequestPaymentsInner(unittest.TestCase):
    """CreateSupportDocumentRequestPaymentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSupportDocumentRequestPaymentsInner:
        """Test CreateSupportDocumentRequestPaymentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSupportDocumentRequestPaymentsInner`
        """
        model = CreateSupportDocumentRequestPaymentsInner()
        if include_optional:
            return CreateSupportDocumentRequestPaymentsInner(
                payment_form = '1',
                payment_method = '',
                payment_due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                payment_id = '0'
            )
        else:
            return CreateSupportDocumentRequestPaymentsInner(
                payment_form = '1',
                payment_method = '',
        )
        """

    def testCreateSupportDocumentRequestPaymentsInner(self):
        """Test CreateSupportDocumentRequestPaymentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
