// Copyright (c) 2024, Vedika Dixit and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student", {
//	refresh(frm) {
    frappe.ui.form.on('Student', {
        refresh: function(frm) {
            // Add custom button to create user
            frm.add_custom_button(__('Create User'), function() {
                createStudentUser(frm);
            });
        },
        before_save: function(frm) {
            // Concatenate full name before saving
            frm.doc.full_name = frm.doc.first_name + ' ' + frm.doc.middle_name + ' ' + frm.doc.last_name;
        }
    });
    
    


// 	},
// });
