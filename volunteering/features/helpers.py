from __future__ import print_function

from django.core import management
from django.core.wsgi import get_wsgi_application
from lettuce import world
from nose.tools import assert_in
from webtest import TestApp

from dothis.features.helpers import visit, click, form, submit, body


def setup_session():
    world.browser = TestApp(get_wsgi_application())
    management.call_command('flush', interactive=False)


def teardown_session():
    pass


def create_campaign(campaign_name, duty_names=[]):
    visit('/admin/volunteering/campaign/')
    click(description='Add')
    form()['name'] = campaign_name
    for idx, name in enumerate(duty_names):
        form()['duty_set-%s-name' % idx] = name
    submit()


def assert_campaign_has_duties(campaign, duty_names):
    visit('/admin/volunteering/campaign/%s/' % campaign.id)
    for name in duty_names:
        assert_in(name, body())


def create_volunteer(volunteer_name):
    visit('/admin/volunteering/volunteer/')
    click('Add')
    form()['name'] = volunteer_name
    submit()


def create_duty(duty_name, campaign_name):
    visit('/admin/volunteering/duty/')
    click('Add')
    form()['name'] = duty_name
    form().select('campaign', text=campaign_name)
    submit()
