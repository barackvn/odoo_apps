{
    # Theme information
    'name' : 'Theme Octra',
    'category' : 'Theme/Corporate',
    'version' : '1.0',
    'summary': 'Fully Responsive, Clean, Modern & Sectioned Odoo Business Theme',
    'description': """.""",
    'license': 'OPL-1',

    # Dependencies
    'depends': [
            'website',  
           # 'octra_403',
           # 'octra_404',
           # 'octra_business_cms_blocks',
           # 'octra_business_carousel',
           # 'octra_customize_theme',
           # 'octra_event',
           # 'octra_footer',
           # 'octra_latest_blogs',
           # 'octra_signin',
           # 'octra_contactus',
           # 'octra_wishlist',
           # 'octra_rating',
           # 'octra_compare',
           # 'octra_blog',
           # 'octra_cart',
           # 'octra_product'
          
               

    ],


    # Views
    'data': [
       #   
    #     'data/company_data/company_data.xml',
    ],
   
    #Odoo Store Specific
    'live_test_url': 'https://goo.gl/uSKKFa',
    'images': [
       'static/description/main_poster.jpeg',
        'static/description/main_screenshot.jpeg',

    ],
    
    # Author
    'author': 'Emipro Technologies Pvt. Ltd.',
    'website': 'http://www.emiprotechnologies.com',
    'maintainer': 'Emipro Technologies Pvt. Ltd.',

    # Technical
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 99.00,
    'currency': 'EUR',
}
