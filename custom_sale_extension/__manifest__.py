{
    'name': 'Custom Sale Extension',
    'version': '1.0',
    'summary': 'Add delivery charges and product details',
    'category': 'Sales',
    'author': 'Your Name',
    'depends': ['sale', 'account', 'product'],
    'data': [
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
        'views/product_template_view.xml',
        'views/sale_order_line_view.xml',
    ],
    'installable': True,
    'application': False,
}
