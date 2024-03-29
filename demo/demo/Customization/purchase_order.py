def print_message_when_purchase_list_added(Purchase Order,method):
    """
    Print a message when a purchase list is added.
    """
    if method == "refresh":
        frappe.msgprint("Purchase list added successfully!")
    