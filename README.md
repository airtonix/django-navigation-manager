Django Navigation Manager
=========================

Django application that helps other applications declare navigation bar items

Provides :
    + manager methods for applications to register navigation bar and bar items
    + template tags to render navigation bar

## Installation

1. You need to have python-setuptools installed
`sudo apt-get install python-setuptools`
1. `python ./setup.py install`

## Usage
If you want to override the default navigation bar template, create a template called "navigation_bar.html".

This is the default template :

    <div class="{{ Name }}">
     <ul>
     {% for item in Bar %}
      <li><a href="{{ item.url }}">{{ item.label }}</a></li>
     {% endfor %}
     </ul>
    </div>

Somewhere in your application, insert code similar to the following :

    from django_navigation_manager.lib.manager import NavigationManager

    navigation_manager = NavigationManager()
    navigation_manager.add_to_bar("main",[
        {    "label" : "Projects",
            "urlconf" : "project.projects.urls",
            "viewname" : "project-dashboard",
            "args" : None,
        },
        {    "label" : "Issues",
            "urlconf" : "project.projects.urls",
            "viewname" : "project-issue-list",
            "args" : None,
        }
    ])

Where the above relates to a project tree of :

    project/
      /projects/
        __init__.py
        models.py
        views.py
        urls.py
        templates/
        templatetags/

And a project.projects.urls which might look like :

    from django.conf.urls.defaults import *
    urlpatterns = patterns("project.projects.views",
        url(r'issue/all$', 'issue_list', name='project-issue-list'),
        url(r'project/$', 'project_dashboard', name='project-dashboard'),
    )


## Legal

### django_navigation_manager/*

+ Copyright (c) 2011 Zenobius Jiricek
+ Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

### Trademarks

Django and the Django logo are registered trademarks of Django Software Foundation.
http://www.djangoproject.com/contact/foundation/

