import frappe

@frappe.whitelist()
def export_Customer():
    return frappe.db.sql('''
        SELECT cus.name AS 'Customer ID', cus.customer_name AS 'Customer Name',  
               cus.mobile_no AS 'Mobile Number', addr.address_type AS 'Address Type', 
               addr.address_line1 AS 'Address Line 1', addr.address_line2 AS 'Address Line 2', 
               addr.city AS 'City', addr.country AS 'Country', addr.pincode AS 'Pin Code'
        FROM `tabCustomer` cus
        LEFT JOIN `tabAddress` addr ON addr.name = cus.customer_primary_address
    ''', as_dict=True)