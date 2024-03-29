frappe.listview_settings['Customer'] = {
    onload(listview) {
        listview.page.add_button('Export',() =>{
            frappe.call({
                method :"demo.demo.Customization.Customer.export_Customer",
                callback:result => {
                    if (result.message){
                        let export_fields =[["customer ID","Customer Name","Customer Type","territory"]]
                        result.message.map(e=>export_fields.push(e))
                        frappe.tools.downloadify(export_fields,null,'Customer');
                    }
                }
            })
        })
    }}