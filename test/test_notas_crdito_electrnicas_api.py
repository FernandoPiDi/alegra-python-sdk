# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.notas_crdito_electrnicas_api import NotasCrditoElectrnicasApi


class TestNotasCrditoElectrnicasApi(unittest.TestCase):
    """NotasCrditoElectrnicasApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NotasCrditoElectrnicasApi()

    def tearDown(self) -> None:
        pass

    def test_create_credit_note(self) -> None:
        """Test case for create_credit_note

        Endpoint para emitir una nota crédito electrónica a la DIAN
        """
        pass

    def test_get_credit_note(self) -> None:
        """Test case for get_credit_note

        Endpoint para consultar una nota crédito electrónica
        """
        pass

    def test_get_credit_note_file(self) -> None:
        """Test case for get_credit_note_file

        Endpoint para obtener un archivo asociado a la nota crédito electrónica
        """
        pass

    def test_get_credit_notes(self) -> None:
        """Test case for get_credit_notes

        Endpoint para consultar notas crédito electrónicas
        """
        pass


if __name__ == '__main__':
    unittest.main()
