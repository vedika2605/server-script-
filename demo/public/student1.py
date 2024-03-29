import frappe
from frappe.utils.response import json_response
@frappe.whitelist(allow_guest=True)
def create_student(data):
    try:
        student = frappe.get_doc({
            "doctype": "Student",
            "first_name": data.get("first_name"),
            "last_name": data.get("last_name"),
        })
        student.insert(ignore_permissions=True)
        return json_response({"success": True, "message": "Student created successfully"})
    except Exception as e:
        frappe.log_error(e)
        return json_response({"success": False, "message": str(e)})
@frappe.whitelist(allow_guest=True)
def get_student(student_name):
    student = frappe.get_doc("Student", student_name)
    return student.as_dict()
@frappe.whitelist(allow_guest=True)
def update_student(student_name, data):
    try:
        student = frappe.get_doc("Student", student_name)
        student.update(data)
        student.save()
        return json_response({"success": True, "message": "Student updated successfully"})
    except Exception as e:
        frappe.log_error(e)
        return json_response({"success": False, "message": str(e)})
@frappe.whitelist(allow_guest=True)
def delete_student(student_name):
    try:
        frappe.delete_doc("Student", student_name)
        return json_response({"success": True, "message": "Student deleted successfully"})
    except Exception as e:
        frappe.log_error(e)
        return json_response({"success": False, "message": str(e)})