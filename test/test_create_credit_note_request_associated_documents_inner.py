# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_credit_note_request_associated_documents_inner import CreateCreditNoteRequestAssociatedDocumentsInner

class TestCreateCreditNoteRequestAssociatedDocumentsInner(unittest.TestCase):
    """CreateCreditNoteRequestAssociatedDocumentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateCreditNoteRequestAssociatedDocumentsInner:
        """Test CreateCreditNoteRequestAssociatedDocumentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCreditNoteRequestAssociatedDocumentsInner`
        """
        model = CreateCreditNoteRequestAssociatedDocumentsInner()
        if include_optional:
            return CreateCreditNoteRequestAssociatedDocumentsInner(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                document_type = '',
                number = 1.337,
                prefix = '0',
                uuid = ''
            )
        else:
            return CreateCreditNoteRequestAssociatedDocumentsInner(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                document_type = '',
                number = 1.337,
                prefix = '0',
                uuid = '',
        )
        """

    def testCreateCreditNoteRequestAssociatedDocumentsInner(self):
        """Test CreateCreditNoteRequestAssociatedDocumentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
