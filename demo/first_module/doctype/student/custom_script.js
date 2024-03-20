// File: custom_script.js

frappe.ui.form.on('Student', {
    onload: function(frm) {
        // Call the function to update full name on load
        updateFullName(frm);
    },
    first_name: function(frm) {
        // Call the function to update full name when first name changes
        updateFullName(frm);
    },
    middle_name: function(frm) {
        // Call the function to update full name when middle name changes
        updateFullName(frm);
    },
    last_name: function(frm) {
        // Call the function to update full name when last name changes
        updateFullName(frm);
    }
});

function updateFullName(frm) {
    var first_name = frm.doc.first_name || '';
    var middle_name = frm.doc.middle_name || '';
    var last_name = frm.doc.last_name || '';

    var full_name = [first_name, middle_name, last_name].filter(Boolean).join(' ');

    // Set the value of the Full Name field
    frm.set_value('full_name', full_name);
}
