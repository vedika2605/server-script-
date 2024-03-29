// Copyright (c) 2024, Vedika Dixit and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Employees", {
// 	refresh(frm) {
// 	},
// });
frappe.ui.form.on("Employees", {
    refresh(frm) {
    },
    before_save: function(frm) {
        frm.doc.full_name = frm.doc.first_name + ' '+ frm.doc.last_name;
    },
});
