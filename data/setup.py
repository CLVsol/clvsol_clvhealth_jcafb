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

    # res_partner_args = []
    # table_name = 'res_partner'
    # print('-->', client, res_partner_args, db_path, table_name)
    # print('--> Executing res_partner_export_sqlite()...')
    # print()
    # res_partner_export_sqlite(client, res_partner_args, db_path, table_name)

    # res_users_args = []
    # table_name = 'res_users'
    # print('-->', client, res_users_args, db_path, table_name, conn_string)
    # print('--> Executing res_users_export_sqlite()...')
    # print()
    # res_users_export_sqlite(client, res_users_args, db_path, table_name, conn_string)

    # hr_department_args = []
    # table_name = 'hr_department'
    # print('-->', client, hr_department_args, db_path, table_name)
    # print('--> Executing hr_department_export_sqlite()...')
    # print()
    # hr_department_export_sqlite(client, hr_department_args, db_path, table_name)

    # hr_job_args = []
    # table_name = 'hr_job'
    # print('-->', client, hr_job_args, db_path, table_name)
    # print('--> Executing hr_job_export_sqlite()...')
    # print()
    # hr_job_export_sqlite(client, hr_job_args, db_path, table_name)

    # hr_employee_args = []
    # table_name = 'hr_employee'
    # print('-->', client, hr_employee_args, db_path, table_name)
    # print('--> Executing hr_employee_export_sqlite()...')
    # print()
    # hr_employee_export_sqlite(client, hr_employee_args, db_path, table_name)

    # tag_args = []
    # table_name = 'clv_global_tag'
    # print('-->', client, tag_args, db_path, table_name)
    # print('--> Executing myo_tag_export_sqlite()...')
    # print()
    # myo_tag_export_sqlite(client, tag_args, db_path, table_name)

    # address_category_args = []
    # table_name = 'clv_address_category'
    # print('-->', client, address_category_args, db_path, table_name)
    # print('--> Executing myo_address_category_export_sqlite()...')
    # print()
    # myo_address_category_export_sqlite(client, address_category_args, db_path, table_name)

    # address_args = []
    # table_name = 'clv_address'
    # print('-->', client, address_args, db_path, table_name)
    # print('--> Executing myo_address_export_sqlite()...')
    # print()
    # myo_address_export_sqlite(client, address_args, db_path, table_name)

    # person_category_args = []
    # table_name = 'clv_person_category'
    # print('-->', client, person_category_args, db_path, table_name)
    # print('--> Executing myo_person_category_export_sqlite()...')
    # print()
    # myo_person_category_export_sqlite(client, person_category_args, db_path, table_name)

    # person_args = []
    # table_name = 'clv_person'
    # print('-->', client, person_args, db_path, table_name)
    # print('--> Executing myo_person_export_sqlite()...')
    # print()
    # myo_person_export_sqlite(client, person_args, db_path, table_name)

    # person_address_role_args = []
    # table_name = 'clv_person_address_role'
    # print('-->', client, person_address_role_args, db_path, table_name)
    # print('--> Executing myo_person_address_role_export_sqlite()...')
    # print()
    # myo_person_address_role_export_sqlite(client, person_address_role_args, db_path, table_name)

    # person_address_args = []
    # table_name = 'clv_person_address'
    # print('-->', client, person_address_args, db_path, table_name)
    # print('--> Executing myo_person_address_export_sqlite()...')
    # print()
    # myo_person_address_export_sqlite(client, person_address_args, db_path, table_name)

    ir_sequence_args = []
    table_name = 'ir_sequence'
    print('-->', client, ir_sequence_args, db_path, table_name, conn_string)
    print('--> Executing ir_sequence_export_sqlite()...')
    print()
    ir_sequence_export_sqlite(client, ir_sequence_args, db_path, table_name, conn_string)


def jcafb_2017_import_sqlite(client, db_path, conn_string):

    res_partner_args = []
    table_name = 'res_partner'
    print('-->', client, res_partner_args, db_path, table_name)
    print('--> Executing res_partner_import_sqlite()...')
    print()
    res_partner_import_sqlite(client, res_partner_args, db_path, table_name)

    res_users_args = []
    table_name = 'res_users'
    print('-->', client, res_users_args, db_path, table_name)
    print('--> Executing res_users_import_sqlite()...')
    print()
    res_users_import_sqlite(client, res_users_args, db_path, table_name)

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
    print(
        '-->',
        client, hr_employee_args, db_path, table_name, hr_department_table_name, hr_job_table_name,
        res_partner_table_name, res_users_table_name
    )
    print('--> Executing hr_employee_import_sqlite()...')
    print()
    hr_employee_import_sqlite(
        client, hr_employee_args, db_path, table_name, hr_department_table_name, hr_job_table_name,
        res_partner_table_name, res_users_table_name
    )

    global_tag_args = []
    table_name = 'clv_global_tag'
    print('-->', client, global_tag_args, db_path, table_name)
    print('--> Executing clv_global_tag_import_sqlite()...')
    print()
    clv_global_tag_import_sqlite(client, global_tag_args, db_path, table_name)

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
    print('-->', client, address_args, db_path, table_name, global_tag_table_name, category_table_name)
    print('--> Executing clv_address_import_sqlite()...')
    print()
    clv_address_import_sqlite(client, address_args, db_path, table_name, global_tag_table_name, category_table_name)

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
    print(
        '-->',
        client, person_args, db_path, table_name, global_tag_table_name, category_table_name, address_table_name
    )
    print('--> Executing clv_person_import_sqlite()...')
    print()
    clv_person_import_sqlite(
        client, person_args, db_path, table_name, global_tag_table_name, category_table_name, address_table_name
    )

    person_address_history_args = []
    table_name = 'clv_person_address'
    global_tag_table_name = 'clv_global_tag'
    role_table_name = 'clv_person_address_role'
    person_table_name = 'clv_person'
    address_table_name = 'clv_address'
    print(
        '-->', client, person_address_history_args, db_path, table_name, global_tag_table_name,
        role_table_name, person_table_name, address_table_name
    )
    print('--> Executing clv_person_address_history_import_sqlite()...')
    print()
    clv_person_address_history_import_sqlite(
        client, person_address_history_args, db_path, table_name, global_tag_table_name,
        role_table_name, person_table_name, address_table_name
    )


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

    # ***** clvhealth-jcafb-2017-pro
    #
    db_path = 'data/clvhealth_jcafb_2017.sqlite'
    print('-->', client, db_path, conn_string)
    print('--> Executing jcafb_2017_export_sqlite()...')
    jcafb_2017_export_sqlite(client, db_path, conn_string)

    # # ***** tkl-odoo10-vm
    # #
    # db_path = 'data/clvhealth_jcafb_2017.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_2017_import_sqlite()...')
    # jcafb_2017_import_sqlite(client, db_path, conn_string)

    print()
    print('--> setup.py', '- Execution time:', secondsToStr(time() - start))
    print()
