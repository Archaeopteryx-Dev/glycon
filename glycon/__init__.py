import os

from django.contrib import admin
from django.contrib.admin import sites
from django.contrib.admin.sites import AdminSite
from django.apps import apps
from django.core.urlresolvers import NoReverseMatch, reverse
from django.template.response import TemplateResponse
from django.utils import six
from django.utils.text import capfirst
from django.views.decorators.cache import never_cache


class GlyconAdminSite(AdminSite):

    @never_cache
    def index(self, request, extra_context=None):
        """
        Overridden version of the main admin page.
        """
        print("Using custom admin...")
        app_dict = {}
        for model, model_admin in self._registry.items():
            app_label = model._meta.app_label
            has_module_perms = model_admin.has_module_permission(request)

            if has_module_perms:
                perms = model_admin.get_model_perms(request)

                # Check whether user has any perm for this module.
                # If so, add the module to the model_list.
                if True in perms.values():
                    info = (app_label, model._meta.model_name)
                    model_dict = {
                        'name': capfirst(model._meta.verbose_name_plural),
                        'object_name': model._meta.object_name,
                        'perms': perms
                    }
                    if hasattr(model, "Data"):
                        model_dict['description'] = model.Data.description
                    else:
                        model_dict['description'] = None
                    if perms.get('change', False):
                        try:
                            model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=self.name)
                        except NoReverseMatch:
                            pass
                    if perms.get('add', False):
                        try:
                            model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=self.name)
                        except NoReverseMatch:
                            pass
                    if app_label in app_dict:
                        app_dict[app_label]['models'].append(model_dict)
                    else:
                        app_dict[app_label] = {
                            'name': apps.get_app_config(app_label).verbose_name,
                            'app_label': app_label,
                            'app_url': reverse(
                                'admin:app_list',
                                kwargs={'app_label': app_label},
                                current_app=self.name,
                            ),
                            'has_module_perms': has_module_perms,
                            'models': [model_dict],
                        }

        # Sort the apps alphabetically.
        app_list = list(six.itervalues(app_dict))
        app_list.sort(key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])

        context = dict(
            self.each_context(request),
            title=self.index_title,
            app_list=app_list,
        )
        context.update(extra_context or {})

        request.current_app = self.name

        return TemplateResponse(request, self.index_template or
                                'admin/index.html', context)

glycon_site = GlyconAdminSite()
admin.site = glycon_site
sites.site = glycon_site

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from glycon.models import SiteConfiguration

import django
django.setup()


def _current_theme(site):
    try:
        site_theme = SiteConfiguration.objects.get(site__id=site)
        print(site_theme.theme)
        return site_theme.theme
    except SiteConfiguration.DoesNotExist:
        return "alexander"
    except:
        return None


def template_directories(site):
    return [
        os.path.join(BASE_DIR, "glycon/templates"),
        os.path.join(BASE_DIR, "glycon/themes/{}/templates".format(_current_theme(site)))
    ]


def static_directories(site):
    return [
        os.path.join(BASE_DIR, "glycon/themes/{}/static".format(_current_theme(site))),
    ]

