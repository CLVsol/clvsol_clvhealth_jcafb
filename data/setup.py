#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from __future__ import print_function

import argparse
import getpass
import erppeek

from odoo_api import *


def jcafb_2017_export_sqlite(client, db_path, conn_string):

    res_country_args = []
    table_name = 'res_country'
    print('-->', client, res_country_args, db_path, table_name)
    print('--> Executing res_country_export_sqlite()...')
    print()
    res_country_export_sqlite(client, res_country_args, db_path, table_name)

    res_country_state_args = []
    table_name = 'res_country_state'
    print('-->', client, res_country_state_args, db_path, table_name)
    print('--> Executing res_country_state_export_sqlite()...')
    print()
    res_country_state_export_sqlite(client, res_country_state_args, db_path, table_name)

    l10n_br_base_city_args = []
    table_name = 'l10n_br_base_city'
    print('-->', client, l10n_br_base_city_args, db_path, table_name)
    print('--> Executing l10n_br_base_city_export_sqlite()...')
    print()
    l10n_br_base_city_export_sqlite(client, l10n_br_base_city_args, db_path, table_name)

    res_partner_args = []
    table_name = 'res_partner'
    print('-->', client, res_partner_args, db_path, table_name)
    print('--> Executing res_partner_export_sqlite()...')
    print()
    res_partner_export_sqlite(client, res_partner_args, db_path, table_name)

    res_users_args = []
    table_name = 'res_users'
    print('-->', client, res_users_args, db_path, table_name, conn_string)
    print('--> Executing res_users_export_sqlite()...')
    print()
    res_users_export_sqlite(client, res_users_args, db_path, table_name, conn_string)

    hr_department_args = []
    table_name = 'hr_department'
    print('-->', client, hr_department_args, db_path, table_name)
    print('--> Executing hr_department_export_sqlite()...')
    print()
    hr_department_export_sqlite(client, hr_department_args, db_path, table_name)

    hr_job_args = []
    table_name = 'hr_job'
    print('-->', client, hr_job_args, db_path, table_name)
    print('--> Executing hr_job_export_sqlite()...')
    print()
    hr_job_export_sqlite(client, hr_job_args, db_path, table_name)

    hr_employee_args = []
    table_name = 'hr_employee'
    print('-->', client, hr_employee_args, db_path, table_name)
    print('--> Executing hr_employee_export_sqlite()...')
    print()
    hr_employee_export_sqlite(client, hr_employee_args, db_path, table_name)

    tag_args = []
    table_name = 'clv_global_tag'
    print('-->', client, tag_args, db_path, table_name)
    print('--> Executing myo_tag_export_sqlite()...')
    print()
    myo_tag_export_sqlite(client, tag_args, db_path, table_name)

    address_category_args = []
    table_name = 'clv_address_category'
    print('-->', client, address_category_args, db_path, table_name)
    print('--> Executing myo_address_category_export_sqlite()...')
    print()
    myo_address_category_export_sqlite(client, address_category_args, db_path, table_name)

    address_args = []
    table_name = 'clv_address'
    print('-->', client, address_args, db_path, table_name)
    print('--> Executing myo_address_export_sqlite()...')
    print()
    myo_address_export_sqlite(client, address_args, db_path, table_name)

    address_log_args = []
    table_name = 'clv_address_log'
    print('-->', client, address_log_args, db_path, table_name)
    print('--> Executing myo_address_log_export_sqlite()...')
    print()
    myo_address_log_export_sqlite(client, address_log_args, db_path, table_name)

    person_category_args = []
    table_name = 'clv_person_category'
    print('-->', client, person_category_args, db_path, table_name)
    print('--> Executing myo_person_category_export_sqlite()...')
    print()
    myo_person_category_export_sqlite(client, person_category_args, db_path, table_name)

    person_args = []
    table_name = 'clv_person'
    print('-->', client, person_args, db_path, table_name)
    print('--> Executing myo_person_export_sqlite()...')
    print()
    myo_person_export_sqlite(client, person_args, db_path, table_name)

    person_log_args = []
    table_name = 'clv_person_log'
    print('-->', client, person_log_args, db_path, table_name)
    print('--> Executing myo_person_log_export_sqlite()...')
    print()
    myo_person_log_export_sqlite(client, person_log_args, db_path, table_name)

    person_address_role_args = []
    table_name = 'clv_person_address_role'
    print('-->', client, person_address_role_args, db_path, table_name)
    print('--> Executing myo_person_address_role_export_sqlite()...')
    print()
    myo_person_address_role_export_sqlite(client, person_address_role_args, db_path, table_name)

    person_address_args = []
    table_name = 'clv_person_address'
    print('-->', client, person_address_args, db_path, table_name)
    print('--> Executing myo_person_address_export_sqlite()...')
    print()
    myo_person_address_export_sqlite(client, person_address_args, db_path, table_name)

    person_address_log_args = []
    table_name = 'clv_person_address_history_log'
    print('-->', client, person_address_log_args, db_path, table_name)
    print('--> Executing myo_person_address_log_export_sqlite()...')
    print()
    myo_person_address_log_export_sqlite(client, person_address_log_args, db_path, table_name)

    survey_survey_args = []
    table_name = 'survey_survey'
    print('-->', client, survey_survey_args, db_path, table_name)
    print('--> Executing survey_survey_export_sqlite()...')
    print()
    survey_survey_export_sqlite(client, survey_survey_args, db_path, table_name)

    document_category_args = []
    table_name = 'clv_document_category'
    print('-->', client, document_category_args, db_path, table_name)
    print('--> Executing myo_document_category_export_sqlite()...')
    print()
    myo_document_category_export_sqlite(client, document_category_args, db_path, table_name)

    document_args = []
    table_name = 'clv_document'
    print('-->', client, document_args, db_path, table_name)
    print('--> Executing myo_document_export_sqlite()...')
    print()
    myo_document_export_sqlite(client, document_args, db_path, table_name)

    document_log_args = []
    table_name = 'clv_document_log'
    print('-->', client, document_log_args, db_path, table_name)
    print('--> Executing myo_document_log_export_sqlite()...')
    print()
    myo_document_log_export_sqlite(client, document_log_args, db_path, table_name)

    document_person_args = []
    table_name = 'clv_document_person'
    print('-->', client, document_person_args, db_path, table_name)
    print('--> Executing myo_document_person_export_sqlite()...')
    print()
    myo_document_person_export_sqlite(client, document_person_args, db_path, table_name)

    lab_test_unit_args = []
    table_name = 'clv_lab_test_unit'
    print('-->', client, lab_test_unit_args, db_path, table_name)
    print('--> Executing myo_lab_test_unit_export_sqlite()...')
    print()
    myo_lab_test_unit_export_sqlite(client, lab_test_unit_args, db_path, table_name)

    lab_test_criterion_args = []
    table_name = 'clv_lab_test_criterion'
    print('-->', client, lab_test_criterion_args, db_path, table_name)
    print('--> Executing myo_lab_test_criterion_export_sqlite()...')
    print()
    myo_lab_test_criterion_export_sqlite(client, lab_test_criterion_args, db_path, table_name)

    lab_test_type_args = []
    table_name = 'clv_lab_test_type'
    print('-->', client, lab_test_type_args, db_path, table_name)
    print('--> Executing myo_lab_test_type_export_sqlite()...')
    print()
    myo_lab_test_type_export_sqlite(client, lab_test_type_args, db_path, table_name)

    lab_test_request_args = []
    table_name = 'clv_lab_test_request'
    print('-->', client, lab_test_request_args, db_path, table_name)
    print('--> Executing myo_lab_test_request_export_sqlite()...')
    print()
    myo_lab_test_request_export_sqlite(client, lab_test_request_args, db_path, table_name)

    lab_test_result_args = []
    table_name = 'clv_lab_test_result'
    print('-->', client, lab_test_result_args, db_path, table_name)
    print('--> Executing myo_lab_test_result_export_sqlite()...')
    print()
    myo_lab_test_result_export_sqlite(client, lab_test_result_args, db_path, table_name)

    ir_sequence_args = []
    table_name = 'ir_sequence'
    print('-->', client, ir_sequence_args, db_path, table_name, conn_string)
    print('--> Executing ir_sequence_export_sqlite()...')
    print()
    ir_sequence_export_sqlite(client, ir_sequence_args, db_path, table_name, conn_string)


def jcafb_2017_import_sqlite(client, db_path, conn_string):

    global_tag_args = []
    table_name = 'clv_global_tag'
    print('-->', client, global_tag_args, db_path, table_name)
    print('--> Executing clv_global_tag_import_sqlite()...')
    print()
    clv_global_tag_import_sqlite(client, global_tag_args, db_path, table_name)

    res_partner_args = []
    table_name = 'res_partner'
    print('-->', client, res_partner_args, db_path, table_name)
    print('--> Executing res_partner_import_sqlite()...')
    print()
    res_partner_import_sqlite(client, res_partner_args, db_path, table_name)

    res_users_args = []
    table_name = 'res_users'
    res_partner_table_name = 'res_partner'
    print('-->', client, res_users_args, db_path, table_name, res_partner_table_name)
    print('--> Executing res_users_import_sqlite()...')
    print()
    res_users_import_sqlite(client, res_users_args, db_path, table_name, res_partner_table_name)

    hr_department_args = []
    table_name = 'hr_department'
    print('-->', client, hr_department_args, db_path, table_name)
    print('--> Executing hr_department_import_sqlite()...')
    print()
    hr_department_import_sqlite(client, hr_department_args, db_path, table_name)

    hr_job_args = []
    table_name = 'hr_job'
    print('-->', client, hr_job_args, db_path, table_name)
    print('--> Executing hr_job_import_sqlite()...')
    print()
    hr_job_import_sqlite(client, hr_job_args, db_path, table_name)

    hr_employee_args = []
    table_name = 'hr_employee'
    hr_department_table_name = 'hr_department'
    hr_job_table_name = 'hr_job'
    res_partner_table_name = 'res_partner'
    res_users_table_name = 'res_users'
    history_marker_name = 'JCAFB-2017'
    print(
        '-->',
        client, hr_employee_args, db_path, table_name, hr_department_table_name, hr_job_table_name,
        res_partner_table_name, res_users_table_name, history_marker_name
    )
    print('--> Executing hr_employee_import_sqlite()...')
    print()
    hr_employee_import_sqlite(
        client, hr_employee_args, db_path, table_name, hr_department_table_name, hr_job_table_name,
        res_partner_table_name, res_users_table_name, history_marker_name
    )

    ir_sequence_args = []
    table_name = 'ir_sequence'
    input_code = 'hr.employee.code'
    output_code = 'hr.employee.code'
    print('-->', client, ir_sequence_args, db_path, table_name, conn_string, input_code, output_code)
    print('--> Executing ir_sequence_import_sqlite_named()...')
    print()
    ir_sequence_import_sqlite_named(
        client, ir_sequence_args, db_path, table_name, conn_string, input_code, output_code
    )

    address_category_args = []
    table_name = 'clv_address_category'
    print('-->', client, address_category_args, db_path, table_name)
    print('--> Executing clv_address_category_import_sqlite()...')
    print()
    clv_address_category_import_sqlite(client, address_category_args, db_path, table_name)

    address_args = []
    table_name = 'clv_address'
    global_tag_table_name = 'clv_global_tag'
    category_table_name = 'clv_address_category'
    res_country_table_name = 'res_country'
    res_country_state_table_name = 'res_country_state'
    l10n_br_base_city_table_name = 'l10n_br_base_city'
    res_users_table_name = 'res_users'
    history_marker_name = 'JCAFB-2017'
    print(
        '-->', client, address_args, db_path, table_name, global_tag_table_name, category_table_name,
        res_country_table_name, res_country_state_table_name, l10n_br_base_city_table_name,
        res_users_table_name, history_marker_name
    )
    print('--> Executing clv_address_import_sqlite()...')
    print()
    clv_address_import_sqlite(
        client, address_args, db_path, table_name, global_tag_table_name, category_table_name,
        res_country_table_name, res_country_state_table_name, l10n_br_base_city_table_name,
        res_users_table_name, history_marker_name
    )

    ir_sequence_args = []
    table_name = 'ir_sequence'
    input_code = 'myo.address.code'
    output_code = 'clv.address.code'
    print('-->', client, ir_sequence_args, db_path, table_name, conn_string, input_code, output_code)
    print('--> Executing ir_sequence_import_sqlite_named()...')
    print()
    ir_sequence_import_sqlite_named(
        client, ir_sequence_args, db_path, table_name, conn_string, input_code, output_code
    )

    address_log_args = []
    table_name = 'clv_address_log'
    address_table_name = 'clv_address'
    res_users_table_name = 'res_users'
    print('-->', client, address_log_args, db_path, table_name, address_table_name, res_users_table_name)
    print('--> Executing clv_address_log_import_sqlite()...')
    print()
    clv_address_log_import_sqlite(client, address_log_args, db_path, table_name,
                                  address_table_name, res_users_table_name)

    person_category_args = []
    table_name = 'clv_person_category'
    print('-->', client, person_category_args, db_path, table_name)
    print('--> Executing clv_person_category_import_sqlite()...')
    print()
    clv_person_category_import_sqlite(client, person_category_args, db_path, table_name)

    person_address_role_args = []
    table_name = 'clv_person_address_role'
    print('-->', client, person_address_role_args, db_path, table_name)
    print('--> Executing clv_person_address_role_import_sqlite()...')
    print()
    clv_person_address_role_import_sqlite(client, person_address_role_args, db_path, table_name)

    person_args = []
    table_name = 'clv_person'
    global_tag_table_name = 'clv_global_tag'
    category_table_name = 'clv_person_category'
    address_table_name = 'clv_address'
    res_users_table_name = 'res_users'
    history_marker_name = 'JCAFB-2017'
    print(
        '-->',
        client, person_args, db_path, table_name, global_tag_table_name, category_table_name, address_table_name,
        res_users_table_name, history_marker_name
    )
    print('--> Executing clv_person_import_sqlite()...')
    print()
    clv_person_import_sqlite(
        client, person_args, db_path, table_name, global_tag_table_name, category_table_name, address_table_name,
        res_users_table_name, history_marker_name
    )

    ir_sequence_args = []
    table_name = 'ir_sequence'
    input_code = 'myo.person.code'
    output_code = 'clv.person.code'
    print('-->', client, ir_sequence_args, db_path, table_name, conn_string, input_code, output_code)
    print('--> Executing ir_sequence_import_sqlite_named()...')
    print()
    ir_sequence_import_sqlite_named(
        client, ir_sequence_args, db_path, table_name, conn_string, input_code, output_code
    )

    person_log_args = []
    table_name = 'clv_person_log'
    person_table_name = 'clv_person'
    res_users_table_name = 'res_users'
    print('-->', client, person_log_args, db_path, table_name, person_table_name, res_users_table_name)
    print('--> Executing clv_person_log_import_sqlite()...')
    print()
    clv_person_log_import_sqlite(client, person_log_args, db_path, table_name,
                                 person_table_name, res_users_table_name)

    person_address_history_args = []
    table_name = 'clv_person_address'
    global_tag_table_name = 'clv_global_tag'
    role_table_name = 'clv_person_address_role'
    person_table_name = 'clv_person'
    address_table_name = 'clv_address'
    history_marker_name = 'JCAFB-2017'
    print(
        '-->', client, person_address_history_args, db_path, table_name, global_tag_table_name,
        role_table_name, person_table_name, address_table_name, history_marker_name
    )
    print('--> Executing clv_person_address_history_import_sqlite()...')
    print()
    clv_person_address_history_import_sqlite(
        client, person_address_history_args, db_path, table_name, global_tag_table_name,
        role_table_name, person_table_name, address_table_name, history_marker_name
    )

    person_address_history_log_args = []
    table_name = 'clv_person_address_history_log'
    person_address_history_table_name = 'clv_person_address'
    res_users_table_name = 'res_users'
    print('-->', client, person_address_history_log_args, db_path, table_name,
          person_address_history_table_name, res_users_table_name)
    print('--> Executing clv_person_address_history_log_import_sqlite()...')
    print()
    clv_person_address_history_log_import_sqlite(client, person_address_history_log_args, db_path, table_name,
                                                 person_address_history_table_name, res_users_table_name)

    document_category_args = []
    table_name = 'clv_document_category'
    print('-->', client, document_category_args, db_path, table_name)
    print('--> Executing clv_document_category_import_sqlite()...')
    print()
    clv_document_category_import_sqlite(client, document_category_args, db_path, table_name)

    document_args = []
    table_name = 'clv_document'
    global_tag_table_name = 'clv_global_tag'
    category_table_name = 'clv_document_category'
    survey_survey_table_name = 'survey_survey'
    person_table_name = 'clv_person'
    address_table_name = 'clv_address'
    res_users_table_name = 'res_users'
    history_marker_name = 'JCAFB-2017'
    print(
        '-->',
        client, document_args, db_path, table_name, global_tag_table_name, category_table_name,
        survey_survey_table_name, person_table_name, address_table_name, res_users_table_name,
        history_marker_name
    )
    print('--> Executing clv_document_import_sqlite()...')
    print()
    clv_document_import_sqlite(
        client, document_args, db_path, table_name, global_tag_table_name, category_table_name,
        survey_survey_table_name, person_table_name, address_table_name, res_users_table_name,
        history_marker_name
    )

    ir_sequence_args = []
    table_name = 'ir_sequence'
    input_code = 'myo.document.code'
    output_code = 'clv.document.code'
    print('-->', client, ir_sequence_args, db_path, table_name, conn_string, input_code, output_code)
    print('--> Executing ir_sequence_import_sqlite_named()...')
    print()
    ir_sequence_import_sqlite_named(
        client, ir_sequence_args, db_path, table_name, conn_string, input_code, output_code
    )

    document_log_args = []
    table_name = 'clv_document_log'
    document_table_name = 'clv_document'
    res_users_table_name = 'res_users'
    print('-->', client, document_log_args, db_path, table_name, document_table_name, res_users_table_name)
    print('--> Executing clv_document_log_import_sqlite()...')
    print()
    clv_document_log_import_sqlite(client, document_log_args, db_path, table_name,
                                   document_table_name, res_users_table_name)

    lab_test_request_args = []
    table_name = 'clv_lab_test_request'
    lab_test_type_table_name = 'clv_lab_test_type'
    person_table_name = 'clv_person'
    res_users_table_name = 'res_users'
    history_marker_name = 'JCAFB-2017'
    print(
        '-->',
        client, lab_test_request_args, db_path, table_name, lab_test_type_table_name,
        person_table_name, res_users_table_name, history_marker_name
    )
    print('--> Executing clv_lab_test_request_import_sqlite()...')
    print()
    clv_lab_test_request_import_sqlite(
        client, lab_test_request_args, db_path, table_name, lab_test_type_table_name,
        person_table_name, res_users_table_name, history_marker_name
    )

    ir_sequence_args = []
    table_name = 'ir_sequence'
    input_code = 'myo.lab_test.request.code'
    output_code = 'clv.lab_test.request.code'
    print('-->', client, ir_sequence_args, db_path, table_name, conn_string, input_code, output_code)
    print('--> Executing ir_sequence_import_sqlite_named()...')
    print()
    ir_sequence_import_sqlite_named(
        client, ir_sequence_args, db_path, table_name, conn_string, input_code, output_code
    )

    lab_test_result_args = []
    table_name = 'clv_lab_test_result'
    lab_test_type_table_name = 'clv_lab_test_type'
    person_table_name = 'clv_person'
    res_users_table_name = 'res_users'
    history_marker_name = 'JCAFB-2017'
    lab_test_criterion_table_name = 'clv_lab_test_criterion'
    lab_test_unit_table_name = 'clv_lab_test_unit'
    print(
        '-->',
        client, lab_test_result_args, db_path, table_name, lab_test_type_table_name,
        person_table_name, res_users_table_name, history_marker_name,
        lab_test_criterion_table_name, lab_test_unit_table_name
    )
    print('--> Executing clv_lab_test_result_import_sqlite()...')
    print()
    clv_lab_test_result_import_sqlite(
        client, lab_test_result_args, db_path, table_name, lab_test_type_table_name,
        person_table_name, res_users_table_name, history_marker_name,
        lab_test_criterion_table_name, lab_test_unit_table_name
    )


def jcafb_2018_export_2017_update_sqlite(client, db_path, conn_string):

    res_country_args = []
    table_name = 'res_country'
    print('-->', client, res_country_args, db_path, table_name)
    print('--> Executing res_country_export_sqlite_10()...')
    print()
    res_country_export_sqlite_10(client, res_country_args, db_path, table_name)

    res_country_state_args = []
    table_name = 'res_country_state'
    print('-->', client, res_country_state_args, db_path, table_name)
    print('--> Executing res_country_state_export_sqlite_10()...')
    print()
    res_country_state_export_sqlite_10(client, res_country_state_args, db_path, table_name)

    l10n_br_base_city_args = []
    table_name = 'l10n_br_base_city'
    print('-->', client, l10n_br_base_city_args, db_path, table_name)
    print('--> Executing l10n_br_base_city_export_sqlite_10()...')
    print()
    l10n_br_base_city_export_sqlite_10(client, l10n_br_base_city_args, db_path, table_name)

    res_partner_args = []
    table_name = 'res_partner'
    print('-->', client, res_partner_args, db_path, table_name)
    print('--> Executing res_partner_export_sqlite_10()...')
    print()
    res_partner_export_sqlite_10(client, res_partner_args, db_path, table_name)

    res_users_args = []
    table_name = 'res_users'
    print('-->', client, res_users_args, db_path, table_name, conn_string)
    print('--> Executing res_users_export_sqlite_10()...')
    print()
    res_users_export_sqlite_10(client, res_users_args, db_path, table_name, conn_string)

    hr_department_args = []
    table_name = 'hr_department'
    print('-->', client, hr_department_args, db_path, table_name)
    print('--> Executing hr_department_export_sqlite_10()...')
    print()
    hr_department_export_sqlite_10(client, hr_department_args, db_path, table_name)

    hr_job_args = []
    table_name = 'hr_job'
    print('-->', client, hr_job_args, db_path, table_name)
    print('--> Executing hr_job_export_sqlite_10()...')
    print()
    hr_job_export_sqlite_10(client, hr_job_args, db_path, table_name)

    hr_employee_args = []
    table_name = 'hr_employee'
    print('-->', client, hr_employee_args, db_path, table_name)
    print('--> Executing hr_employee_export_sqlite_10()...')
    print()
    hr_employee_export_sqlite_10(client, hr_employee_args, db_path, table_name)

    hr_employee_history_args = []
    table_name = 'hr_employee_history'
    print('-->', client, hr_employee_history_args, db_path, table_name)
    print('--> Executing hr_employee_history_export_sqlite_10()...')
    print()
    hr_employee_history_export_sqlite_10(client, hr_employee_history_args, db_path, table_name)

    hr_job_history_args = []
    table_name = 'hr_job_history'
    print('-->', client, hr_job_history_args, db_path, table_name)
    print('--> Executing hr_job_history_export_sqlite_10()...')
    print()
    hr_job_history_export_sqlite_10(client, hr_job_history_args, db_path, table_name)

    hr_department_history_args = []
    table_name = 'hr_department_history'
    print('-->', client, hr_department_history_args, db_path, table_name)
    print('--> Executing hr_department_history_export_sqlite_10()...')
    print()
    hr_department_history_export_sqlite_10(client, hr_department_history_args, db_path, table_name)

    tag_args = []
    table_name = 'clv_global_tag'
    print('-->', client, tag_args, db_path, table_name)
    print('--> Executing clv_global_tag_export_sqlite_10()...')
    print()
    clv_global_tag_export_sqlite_10(client, tag_args, db_path, table_name)

    history_marker_args = []
    table_name = 'clv_history_marker'
    print('-->', client, history_marker_args, db_path, table_name)
    print('--> Executing clv_history_marker_export_sqlite_10()...')
    print()
    clv_history_marker_export_sqlite_10(client, history_marker_args, db_path, table_name)

    person_args = []
    table_name = 'clv_person'
    print('-->', client, person_args, db_path, table_name)
    print('--> Executing clv_person_export_sqlite_10()...')
    print()
    clv_person_export_sqlite_10(client, person_args, db_path, table_name)

    event_category_args = []
    table_name = 'clv_event_category'
    print('-->', client, event_category_args, db_path, table_name)
    print('--> Executing clv_event_category_export_sqlite_10()...')
    print()
    clv_event_category_export_sqlite_10(client, event_category_args, db_path, table_name)

    event_args = []
    table_name = 'clv_event'
    print('-->', client, event_args, db_path, table_name)
    print('--> Executing clv_event_export_sqlite_10()...')
    print()
    clv_event_export_sqlite_10(client, event_args, db_path, table_name)

    ir_sequence_args = []
    table_name = 'ir_sequence'
    print('-->', client, ir_sequence_args, db_path, table_name, conn_string)
    print('--> Executing ir_sequence_export_sqlite_10()...')
    print()
    ir_sequence_export_sqlite_10(client, ir_sequence_args, db_path, table_name, conn_string)


def jcafb_2018_import_2017_update_sqlite(client, db_path, conn_string):

    res_users_args = []
    table_name = 'res_users'
    res_partner_table_name = 'res_partner'
    print('-->', client, res_users_args, db_path, table_name, res_partner_table_name)
    print('--> Executing res_users_import_sqlite_10()...')
    print()
    res_users_import_sqlite_10(client, res_users_args, db_path, table_name, res_partner_table_name)

    history_marker_args = []
    table_name = 'clv_history_marker'
    print(
        '-->',
        client, history_marker_args, db_path, table_name
    )
    print('--> Executing clv_history_marker_import_sqlite_10()...')
    print()
    clv_history_marker_import_sqlite_10(
        client, history_marker_args, db_path, table_name
    )

    hr_employee_args = []
    table_name = 'hr_employee'
    hr_department_table_name = 'hr_department'
    hr_job_table_name = 'hr_job'
    res_partner_table_name = 'res_partner'
    res_users_table_name = 'res_users'
    history_marker_table_name = 'clv_history_marker'
    print(
        '-->',
        client, hr_employee_args, db_path, table_name, hr_department_table_name, hr_job_table_name,
        res_partner_table_name, res_users_table_name, history_marker_table_name
    )
    print('--> Executing hr_employee_import_sqlite_10()...')
    print()
    hr_employee_import_sqlite_10(
        client, hr_employee_args, db_path, table_name, hr_department_table_name, hr_job_table_name,
        res_partner_table_name, res_users_table_name, history_marker_table_name
    )

    employee_history_args = []
    table_name = 'hr_employee_history'
    hr_employee_table_name = 'hr_employee'
    hr_department_table_name = 'hr_department'
    hr_job_table_name = 'hr_job'
    history_marker_table_name = 'clv_history_marker'
    print('-->', client, employee_history_args, db_path, table_name,
          hr_employee_table_name, hr_department_table_name, hr_job_table_name,
          history_marker_table_name)
    print('--> Executing hr_employee_history_import_sqlite_10()...')
    print()
    hr_employee_history_import_sqlite_10(client, employee_history_args, db_path, table_name,
                                         hr_employee_table_name, hr_department_table_name, hr_job_table_name,
                                         history_marker_table_name)

    job_history_args = []
    table_name = 'hr_job_history'
    hr_employee_table_name = 'hr_employee'
    hr_job_table_name = 'hr_job'
    history_marker_table_name = 'clv_history_marker'
    print('-->', client, job_history_args, db_path, table_name,
          hr_employee_table_name, hr_job_table_name,
          history_marker_table_name)
    print('--> Executing hr_job_history_import_sqlite_10()...')
    print()
    hr_job_history_import_sqlite_10(client, job_history_args, db_path, table_name,
                                    hr_employee_table_name, hr_job_table_name,
                                    history_marker_table_name)

    department_history_args = []
    table_name = 'hr_department_history'
    hr_employee_table_name = 'hr_employee'
    hr_department_table_name = 'hr_department'
    history_marker_table_name = 'clv_history_marker'
    print('-->', client, department_history_args, db_path, table_name,
          hr_employee_table_name, hr_department_table_name,
          history_marker_table_name)
    print('--> Executing hr_department_history_import_sqlite_10()...')
    print()
    hr_department_history_import_sqlite_10(client, department_history_args, db_path, table_name,
                                           hr_employee_table_name, hr_department_table_name,
                                           history_marker_table_name)

    event_args = []
    table_name = 'clv_event'
    global_tag_table_name = 'clv_global_tag'
    category_table_name = 'clv_person_category'
    hr_employee_table_name = 'hr_employee'
    person_table_name = 'clv_person'
    history_marker_table_name = 'clv_history_marker'
    print('-->', client, event_args, db_path, table_name,
          global_tag_table_name, category_table_name, hr_employee_table_name, person_table_name,
          history_marker_table_name)
    print('--> Executing clv_event_import_sqlite_10()...')
    print()
    clv_event_import_sqlite_10(client, event_args, db_path, table_name,
                               global_tag_table_name, category_table_name, hr_employee_table_name, person_table_name,
                               history_marker_table_name)

    ir_sequence_args = []
    table_name = 'ir_sequence'
    input_code = 'clv.event.code'
    output_code = 'clv.event.code'
    print('-->', client, ir_sequence_args, db_path, table_name, conn_string, input_code, output_code)
    print('--> Executing ir_sequence_import_sqlite_named_10()...')
    print()
    ir_sequence_import_sqlite_named_10(
        client, ir_sequence_args, db_path, table_name, conn_string, input_code, output_code
    )


def jcafb_2018_user_groups_set(client, db_path, conn_string):

    group_name_list_geral = [

        # base:
        #
        'Employee',

        # clv_base:
        #
        'User (Base)',
        'Super User (Base)',
        'Annotation User (Base)',
        'Register User (Base)',
        'Log User (Base)',
        'Manager (Base)',
        # 'Super Manager (Base)',

        # clv_global_tag:
        #
        'User (Global Tag)',
        'Manager (Global Tag)',
        # 'Super Manager (Global Tag)',

        # clv_history_marker:
        #
        'User (History Marker)',
        'Manager (History Marker)',
        # 'Super Manager (History Marker)',

        # clv_address:
        #
        'User (Address)',
        'Manager (Address)',
        # 'Super Manager (Address)',

        # clv_person:
        #
        'User (Person)',
        'Manager (Person)',
        # 'Super Manager (Person)',

        # clv_community:
        #
        'User (Community)',
        'Manager (Community)',
        # 'Super Manager (Community)',

        # clv_event:
        #
        'User (Event)',
        'Manager (Event)',
        # 'Super Manager (Event)',
    ]

    # Demo User
    #
    user_login = 'demo'
    group_name_list = group_name_list_geral
    print('-->', client, user_login, group_name_list)
    print('--> Executing user_groups_set()...')
    print()
    user_groups_set(client, user_login, group_name_list)


def get_arguments():

    global server
    global username
    global password
    global dbname
    global db_server
    global db_user
    global db_password

    parser = argparse.ArgumentParser()
    parser.add_argument('--server', action="store", dest="server")
    parser.add_argument('--user', action="store", dest="username")
    parser.add_argument('--pw', action="store", dest="password")
    parser.add_argument('--db', action="store", dest="dbname")
    parser.add_argument('--dbserver', action="store", dest="db_server")
    parser.add_argument('--dbu', action="store", dest="db_user")
    parser.add_argument('--dbw', action="store", dest="db_password")

    args = parser.parse_args()
    print('%s%s' % ('--> ', args))

    if args.server is not None:
        server = args.server
    elif server == '*':
        server = raw_input('server: ')

    if args.dbname is not None:
        dbname = args.dbname
    elif dbname == '*':
        dbname = raw_input('dbname: ')

    if args.username is not None:
        username = args.username
    elif username == '*':
        username = raw_input('username: ')

    if args.password is not None:
        password = args.password
    elif password == '*':
        password = getpass.getpass('password: ')

    if args.db_server is not None:
        db_server = args.db_server
    elif db_server == '*':
        db_server = getpass.getpass('db_server: ')

    if args.db_user is not None:
        db_user = args.db_user
    elif db_user == '*':
        db_user = getpass.getpass('db_user: ')

    if args.db_password is not None:
        db_password = args.db_password
    elif db_password == '*':
        db_password = getpass.getpass('db_password: ')


def secondsToStr(t):

    return "%d:%02d:%02d.%03d" % reduce(lambda ll, b: divmod(ll[0], b) + ll[1:], [(t * 1000,), 1000, 60, 60])


def buffer():
    pass


if __name__ == '__main__':

    server = 'http://localhost:8069'
    # server = '*'

    username = 'username'
    # username = '*'
    password = 'password'
    # password = '*'

    dbname = 'odoo'
    # dbname = '*'

    db_server = 'localhost'
    # db_server = '*'

    db_user = 'openerp'
    # db_user = '*'

    db_password = 'openerp'
    # db_password = '*'

    print()
    print('--> setup.py...')
    print('--> server:', server)

    get_arguments()

    from time import time
    start = time()

    client = erppeek.Client(server, dbname, username, password)
    conn_string = "dbname='" + dbname + "' user='" + db_user + "' host='" + db_server + \
                  "' password='" + db_password + "'"

    # # ***** clvhealth-jcafb-2017-pro
    # #
    # db_path = 'data/clvhealth_jcafb_2017.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_2017_export_sqlite()...')
    # jcafb_2017_export_sqlite(client, db_path, conn_string)

    # # ***** tkl-odoo10-jcafb-vm
    # #
    # db_path = 'data/clvhealth_jcafb_2017.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_2017_import_sqlite()...')
    # jcafb_2017_import_sqlite(client, db_path, conn_string)

    # # ***** tkl-odoo10-jcafb-vm
    # #
    # db_path = 'data/clvhealth_jcafb_2017_update.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_2018_import_2017_update_sqlite()...')
    # jcafb_2018_import_2017_update_sqlite(client, db_path, conn_string)

    # # ***** tkl-odoo10-jcafb-vm
    # #
    # db_path = 'data/clvhealth_jcafb_2017_update.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_2018_export_2017_update_sqlite()...')
    # jcafb_2018_export_2017_update_sqlite(client, db_path, conn_string)

    # # ***** tkl-odoo10-jcafb-vm
    # #
    # db_path = 'data/clvhealth_jcafb_2017_update.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_2018_user_groups_set()...')
    # jcafb_2018_user_groups_set(client, db_path, conn_string)

    print()
    print('--> setup.py', '- Execution time:', secondsToStr(time() - start))
    print()
