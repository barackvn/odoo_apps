# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Task Timer",
    
    "author": "Softhealer Technologies",
    
    "website": "https://www.softhealer.com",
        
    "support": "info@softhealer.com",   

    "version": "12.0.1",
    
    "category": "Project",
    
    "summary": "This module allow user to start/stop time of task.",
        
    "description": """This module allow user to start/stop time of task. Easy to calculate duration of time taken for task.""",
     
    "depends": ['project','hr_timesheet','analytic'],
    
    "data": [
        'security/ir.model.access.csv',
        'views/project_task_time.xml',
    ],    
    
    "images": ["static/description/background.png",],
                 
    "installable": True,
    "auto_install": False,
    "application": True,  
      
    "price": "9",
    "currency": "EUR"          
}
