# Copyright (c) 2023, Vivek and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        "Date:Date:100",
        "Bundle Number:Data:100",
        "Denomination:Currency:100",
        "No of Tickets:Int:100",
    ]

    conditions = ""
    values = {}

    if filters.get("date"):
        conditions += " AND dte.date = %(date)s"
        values["date"] = filters["date"]

    if filters.get("bundle_number"):
        conditions += " AND dti.bundle_number = %(bundle_number)s"
        values["bundle_number"] = filters["bundle_number"]

    if filters.get("denomination"):
        conditions += " AND dti.denomination = %(denomination)s"
        values["denomination"] = filters["denomination"]

    data = frappe.db.sql(
        f"""
        SELECT
            dte.date AS date,
            dti.bundle_number AS bundle_number,
            dti.denomination AS denomination,
            SUM(dti.no_of_tickets) AS no_of_tickets
        FROM
            `tabDaily Ticket Entry` AS dte
        INNER JOIN
            `tabDaily Ticket Item` AS dti
        ON
            dte.name = dti.parent
        WHERE
            dte.docstatus = 1
            {conditions}
        GROUP BY
            dte.date, dti.bundle_number, dti.denomination
        ORDER BY
            dte.date
        """,
        values,
        as_dict=True,
    )

    return columns, data
