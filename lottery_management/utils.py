import frappe

@frappe.whitelist()
def get_bundle_details(barcode):    
    bundle_list = frappe.get_all("Ticket Bundle", {"bundle_number": barcode[:10], "start_sequence": ["<=", barcode[10:13]], "end_sequence": [">=", barcode[10:13]]}, ["bundle_number"])
    
    if bundle_list:
        return {'bundle_number': bundle_list[0]["bundle_number"]}
    
    return None