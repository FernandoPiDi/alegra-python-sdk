# coding: utf-8

"""
    API Alegra Proveedor Electrónico Colombia

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_adjustment_note_equivalent_document_request import CreateAdjustmentNoteEquivalentDocumentRequest

class TestCreateAdjustmentNoteEquivalentDocumentRequest(unittest.TestCase):
    """CreateAdjustmentNoteEquivalentDocumentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAdjustmentNoteEquivalentDocumentRequest:
        """Test CreateAdjustmentNoteEquivalentDocumentRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAdjustmentNoteEquivalentDocumentRequest`
        """
        model = CreateAdjustmentNoteEquivalentDocumentRequest()
        if include_optional:
            return CreateAdjustmentNoteEquivalentDocumentRequest(
                prefix = '0',
                number = 1.337,
                note = '0',
                document_reference = openapi_client.models.create_adjustment_note_equivalent_document_request_document_reference.createAdjustmentNoteEquivalentDocument_request_documentReference(
                    id = '', 
                    full_number = '', 
                    cude = '', 
                    issue_date = '', ),
                discrepancy = openapi_client.models.create_adjustment_note_equivalent_document_request_discrepancy.createAdjustmentNoteEquivalentDocument_request_discrepancy(
                    section_id = '', 
                    response_code = 1, 
                    description = '', ),
                company = openapi_client.models.create_equivalent_document_pos_request_company.createEquivalentDocumentPos_request_company(
                    id = '', 
                    organization_type = 1.337, 
                    identification_number = '', 
                    dv = '0', 
                    name = '0', 
                    trade_name = '', 
                    regime_code = '', 
                    tax_code = openapi_client.models.create_equivalent_document_pos_request_company_tax_code.createEquivalentDocumentPos_request_company_taxCode(
                        id = '', 
                        name = '', ), 
                    economic_activities = [
                        '0480'
                        ], 
                    email = '', 
                    phone = '', 
                    address = openapi_client.models.get_companies_200_response_companies_inner_address.getCompanies_200_response_companies_inner_address(
                        city = '', 
                        department = '', 
                        country = '', ), 
                    contact = openapi_client.models.create_equivalent_document_pos_request_company_contact.createEquivalentDocumentPos_request_company_contact(
                        name = '', 
                        telefax = '', 
                        note = '', 
                        commercial_registration_number = '', ), ),
                customer = openapi_client.models.create_adjustment_note_equivalent_document_request_customer.createAdjustmentNoteEquivalentDocument_request_customer(
                    name = '0', 
                    organization_type = 1.337, 
                    identification_type = '', 
                    identification_number = '', 
                    dv = '0', 
                    regime_code = '', 
                    tax_code = openapi_client.models.create_equivalent_document_pos_request_customer_tax_code.createEquivalentDocumentPos_request_customer_taxCode(
                        id = '', 
                        name = '', ), 
                    trade_name = '', 
                    address = openapi_client.models.get_companies_200_response_companies_inner_address.getCompanies_200_response_companies_inner_address(
                        city = '', 
                        department = '', 
                        country = '', ), ),
                items = [
                    openapi_client.models.create_adjustment_note_equivalent_document_request_items_inner.createAdjustmentNoteEquivalentDocument_request_items_inner(
                        code = openapi_client.models.create_adjustment_note_equivalent_document_request_items_inner_code.createAdjustmentNoteEquivalentDocument_request_items_inner_code(
                            identification_id = '01234', 
                            id = '', ), 
                        description = '', 
                        price = 1.337, 
                        price_reference = 1.337, 
                        discount = 1.337, 
                        discount_amount = 1.337, 
                        charge = 1.337, 
                        charge_amount = 1.337, 
                        quantity = 1.337, 
                        unit_code = '', 
                        note = '012345678910111213141516171819', 
                        subtotal = 1.337, 
                        tax_amount = 1.337, 
                        total = 1.337, 
                        taxes = [
                            openapi_client.models.create_equivalent_document_pos_request_items_inner_taxes_inner.createEquivalentDocumentPos_request_items_inner_taxes_inner(
                                tax_code = '', 
                                tax_amount = 1.337, 
                                tax_percentage = '', 
                                taxable_amount = 1.337, 
                                tax_base_unit_measure = 1.337, 
                                tax_per_unit_amount = 1.337, )
                            ], 
                        pack_size = 0, 
                        brand_name = '0', 
                        model_name = '0', 
                        additional_item_properties = [
                            openapi_client.models.create_equivalent_document_pos_request_items_inner_additional_item_properties_inner.createEquivalentDocumentPos_request_items_inner_additionalItemProperties_inner(
                                name = '', 
                                value = '', )
                            ], )
                    ],
                total_amounts = openapi_client.models.create_equivalent_document_pos_request_total_amounts.createEquivalentDocumentPos_request_totalAmounts(
                    gross_total = 1.337, 
                    taxable_total = 1.337, 
                    tax_total = 1.337, 
                    discount_total = 1.337, 
                    charge_total = 1.337, 
                    advance_total = 1.337, 
                    payable_total = 1.337, 
                    currency_code = '', ),
                payments = [
                    openapi_client.models.create_equivalent_document_pos_request_payments_inner.createEquivalentDocumentPos_request_payments_inner(
                        payment_form = '', 
                        payment_method = '', 
                        payment_due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        payment_id = '0', )
                    ],
                discounts_and_charges = [
                    openapi_client.models.create_equivalent_document_pos_request_discounts_and_charges_inner.createEquivalentDocumentPos_request_discountsAndCharges_inner(
                        is_charge = True, 
                        reason = '', 
                        percentage_amount = 0, 
                        amount = 0, 
                        base_amount = 0, )
                    ],
                delivery = openapi_client.models.create_adjustment_note_equivalent_document_request_delivery.createAdjustmentNoteEquivalentDocument_request_delivery(
                    date = '', 
                    time = '', 
                    address = openapi_client.models.create_adjustment_note_equivalent_document_request_delivery_address.createAdjustmentNoteEquivalentDocument_request_delivery_address(
                        city = '', 
                        postal = '', 
                        department = '', ), 
                    delivery_company = openapi_client.models.create_adjustment_note_equivalent_document_request_delivery_delivery_company.createAdjustmentNoteEquivalentDocument_request_delivery_deliveryCompany(
                        name = '', 
                        tax_scheme = openapi_client.models.create_adjustment_note_equivalent_document_request_delivery_delivery_company_tax_scheme.createAdjustmentNoteEquivalentDocument_request_delivery_deliveryCompany_taxScheme(
                            name = '', 
                            code = '', 
                            identification = '', 
                            identification_type = '', 
                            dv = '', ), ), )
            )
        else:
            return CreateAdjustmentNoteEquivalentDocumentRequest(
                number = 1.337,
                document_reference = openapi_client.models.create_adjustment_note_equivalent_document_request_document_reference.createAdjustmentNoteEquivalentDocument_request_documentReference(
                    id = '', 
                    full_number = '', 
                    cude = '', 
                    issue_date = '', ),
                discrepancy = openapi_client.models.create_adjustment_note_equivalent_document_request_discrepancy.createAdjustmentNoteEquivalentDocument_request_discrepancy(
                    section_id = '', 
                    response_code = 1, 
                    description = '', ),
                company = openapi_client.models.create_equivalent_document_pos_request_company.createEquivalentDocumentPos_request_company(
                    id = '', 
                    organization_type = 1.337, 
                    identification_number = '', 
                    dv = '0', 
                    name = '0', 
                    trade_name = '', 
                    regime_code = '', 
                    tax_code = openapi_client.models.create_equivalent_document_pos_request_company_tax_code.createEquivalentDocumentPos_request_company_taxCode(
                        id = '', 
                        name = '', ), 
                    economic_activities = [
                        '0480'
                        ], 
                    email = '', 
                    phone = '', 
                    address = openapi_client.models.get_companies_200_response_companies_inner_address.getCompanies_200_response_companies_inner_address(
                        city = '', 
                        department = '', 
                        country = '', ), 
                    contact = openapi_client.models.create_equivalent_document_pos_request_company_contact.createEquivalentDocumentPos_request_company_contact(
                        name = '', 
                        telefax = '', 
                        note = '', 
                        commercial_registration_number = '', ), ),
                items = [
                    openapi_client.models.create_adjustment_note_equivalent_document_request_items_inner.createAdjustmentNoteEquivalentDocument_request_items_inner(
                        code = openapi_client.models.create_adjustment_note_equivalent_document_request_items_inner_code.createAdjustmentNoteEquivalentDocument_request_items_inner_code(
                            identification_id = '01234', 
                            id = '', ), 
                        description = '', 
                        price = 1.337, 
                        price_reference = 1.337, 
                        discount = 1.337, 
                        discount_amount = 1.337, 
                        charge = 1.337, 
                        charge_amount = 1.337, 
                        quantity = 1.337, 
                        unit_code = '', 
                        note = '012345678910111213141516171819', 
                        subtotal = 1.337, 
                        tax_amount = 1.337, 
                        total = 1.337, 
                        taxes = [
                            openapi_client.models.create_equivalent_document_pos_request_items_inner_taxes_inner.createEquivalentDocumentPos_request_items_inner_taxes_inner(
                                tax_code = '', 
                                tax_amount = 1.337, 
                                tax_percentage = '', 
                                taxable_amount = 1.337, 
                                tax_base_unit_measure = 1.337, 
                                tax_per_unit_amount = 1.337, )
                            ], 
                        pack_size = 0, 
                        brand_name = '0', 
                        model_name = '0', 
                        additional_item_properties = [
                            openapi_client.models.create_equivalent_document_pos_request_items_inner_additional_item_properties_inner.createEquivalentDocumentPos_request_items_inner_additionalItemProperties_inner(
                                name = '', 
                                value = '', )
                            ], )
                    ],
                total_amounts = openapi_client.models.create_equivalent_document_pos_request_total_amounts.createEquivalentDocumentPos_request_totalAmounts(
                    gross_total = 1.337, 
                    taxable_total = 1.337, 
                    tax_total = 1.337, 
                    discount_total = 1.337, 
                    charge_total = 1.337, 
                    advance_total = 1.337, 
                    payable_total = 1.337, 
                    currency_code = '', ),
                payments = [
                    openapi_client.models.create_equivalent_document_pos_request_payments_inner.createEquivalentDocumentPos_request_payments_inner(
                        payment_form = '', 
                        payment_method = '', 
                        payment_due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        payment_id = '0', )
                    ],
        )
        """

    def testCreateAdjustmentNoteEquivalentDocumentRequest(self):
        """Test CreateAdjustmentNoteEquivalentDocumentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
