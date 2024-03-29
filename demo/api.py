from __future__ import unicode_literals
import frappe
from frappe import _
@frappe.whitelist(allow_guest=True)
def get_user():
    try:
        user = frappe.get_all("User",fields=["name", "email", "first_name", "last_name"])
        print(user)
        return frappe._dict({"status": "success", "user": user})
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("User API Error"))
        return frappe._dict({"status": "failed", "message": "An error occurred while fetching user."})

@frappe.whitelist(allow_guest=True)
def create_user(email, first_name, last_name):
        new_user = frappe.get_doc({
            "doctype": "User",
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
        })
        new_user.insert(ignore_permissions=True)

@frappe.whitelist(allow_guest=True)
def update_user(email, first_name, last_name):
    user = frappe.get_doc("User", email)
    user.update({
        "first_name": first_name,
        "last_name": last_name,
    })

    user.save(ignore_permissions=True)

@frappe.whitelist(allow_guest=True)
def delete_user(email):
    try:
        user = frappe.get_doc("User", email)
        
        user.delete(ignore_permissions=True)
        return {"status": "success", "message": f"User '{email}' deleted successfully."}
    except frappe.DoesNotExistError:
        return {"status": "failed", "message": f"User '{email}' does not exist."}




