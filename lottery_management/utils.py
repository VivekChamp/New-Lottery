import frappe

@frappe.whitelist()
def get_bundle_details(barcode):
    print("get_bundle_details function called")  # Check if the function is being called
    bundle = frappe.get_doc('Ticket Bundle', {'barcode': barcode})
    print("Bundle:", bundle)  # Check if the bundle is fetched correctly
    if bundle:
        return {'bundle_number': bundle.bundle_number}
    return None

