# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.nminas_electrnicas_api import NminasElectrnicasApi


class TestNminasElectrnicasApi(unittest.TestCase):
    """NminasElectrnicasApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NminasElectrnicasApi()

    def tearDown(self) -> None:
        pass

    def test_adjust_payroll(self) -> None:
        """Test case for adjust_payroll

        Endpoint para reemplazar/ajustar una nómina electrónica
        """
        pass

    def test_cancel_payroll(self) -> None:
        """Test case for cancel_payroll

        Endpoint para anular una nómina electrónica
        """
        pass

    def test_create_payroll(self) -> None:
        """Test case for create_payroll

        Endpoint para emitir una nómina a la DIAN
        """
        pass

    def test_get_payroll(self) -> None:
        """Test case for get_payroll

        Endpoint para consultar una nómina electrónica
        """
        pass

    def test_get_payroll_adjustments(self) -> None:
        """Test case for get_payroll_adjustments

        Endpoint para consultar ajustes de nóminas electrónicas
        """
        pass

    def test_get_payroll_cancellations(self) -> None:
        """Test case for get_payroll_cancellations

        Endpoint para consultar cancelaciones de nóminas electrónicas
        """
        pass

    def test_get_payroll_file(self) -> None:
        """Test case for get_payroll_file

        Endpoint para obtener un archivo asociado a la nómina electrónica
        """
        pass

    def test_get_payrolls(self) -> None:
        """Test case for get_payrolls

        Endpoint para consultar nóminas electrónicas
        """
        pass


if __name__ == '__main__':
    unittest.main()
