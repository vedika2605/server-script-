# Copyright (c) 2024, Vedika Dixit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

@frappe.whitelist(allow_guest=True)
def get_student_data():
    # Fetch data from the Students doctype
    students = frappe.get_all("Students", fields=["first_name", "middle_name"])
    return students





# class Student(Document):
# 	pass
