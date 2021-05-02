# Copyright 2017 Artyom Losev
# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": """E-commerce Category Cache""",
    "summary": """Use this module to greatly accelerate the loading of a page with a large number of product categories""",
    "category": "Website",
    "images": ["images/websale_cache.png"],
    "version": "13.0.1.0.1",
    "author": "IT-Projects LLC, Artyom Losev",
    "support": "apps@itpp.dev",
    "website": "https://www.it-projects.info",
    "license": "Other OSI approved licence",  # MIT
    "price": 25.00,
    "currency": "EUR",
    "depends": ["website_sale", "website", "base_action_rule"],
    "data": ["views.xml", "data/ir_action_server.xml", "data/base_action_rules.xml"],
    "installable": False,
}
