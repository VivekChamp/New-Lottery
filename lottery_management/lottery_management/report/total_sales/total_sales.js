// Copyright (c) 2023, Vivek and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Total Sales"] = {
	"filters": [
		{
            "fieldname": "date",
            "label": __("Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.get_today(),
            "reqd": 1
        },
        {
            "fieldname": "bundle_number",
            "label": __("Bundle Number"),
            "fieldtype": "Link",
			"options":"Ticket Bundle"
        },
        {
            "fieldname": "denomination",
            "label": __("Denomination"),
            "fieldtype": "Currency"
        }
	]
};
