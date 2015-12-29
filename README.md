Glycon
======

Glycon is a Django-based CMS.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Create a new django project.

2. Add django sites, glycon, and associated packages to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django.contrib.sites',
        'glycon',
        'glycon_summaries',
        'glycon_menu_blocks'       
    ]
    
3. Add glycon templates to your settings file like this:

    TEMPLATES = [
        {
            ....
            'DIRS': glycon.template_directories(SITE_ID),
            ....
        },
    ]

4. Add glycon static files to your settings file like this:

    STATICFILES_DIRS = [
                        ...
                       ] + glycon.static_directories(SITE_ID)
    

5. Include the glycon URLconf in your project urls.py like this::

    url(r'^', include('glycon.urls')),

6. Run `python manage.py migrate` to create the glycon models.

7. Run `python manage.py createsuperuser` to create an admin user.

8. Run `python manage.py runserver` and visit http://127.0.0.1:8000/ - follow the onscreen instructions.


Roadmap
-------

v0.2 - Features:

From functions required for glycon home site:
		
* Block model - part of glycon core DONE
* Menu blocks - add menus to blocks DONE
* Theme system - part of glycon core DONE
* Add a summary block to glycon_summaries
* Add configurable elements to a Theme (colours, background (upload to media), favicon (upload to media) etc.)
* Multi-site config DONE
* Finalise the Alexander and Lucian themes PARTIALLY DONE
* Override the main admin index to describe the features of each class of the Glycon system, and add links etc. DONE
* Ensure themes pick up images from the correct media root

Then add four more new modules:

	glycon_disqus
	glycon_google_analytics
	glycon_statcounter
	glycon_vimeo

Then we'll launch the Glycon web site, and create a video to show how to install it from scratch.

v0.3 - Features

* Add a script to /bin to do a full install of a Glycon CMS, including Django setup. 
* User logins - Admin, Editor, User.
* Permissions model for elements - lots of abstraction - use a decorator?

Then add more modules:

	glycon_contact_forms
	glycon_mailing_lists
	glycon_xml_sitemap
	glycon_addthis

v0.4 - Features

* Built-In Module Loader
* First version bundled up with Docker and other tools to allow immediate installation for lower-tech users.

v0.5 - Features

* Custom Admin
* Loader from scratch in /bin - installs django and glycon simultaneously.
* Visual js app for arranging blocks etc.
