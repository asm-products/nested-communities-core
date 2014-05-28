# -*- coding: utf-8 -*-

from lettuce import step, before, after

from helpers import (setup_session, teardown_session, create_volunteer,
                     create_duty, create_campaign, assert_campaign_has_duties)
from dothis.features.helpers import login_as_the_admin, the, assert_was_created


@before.each_scenario
def setup(scenario):
    setup_session()


@after.each_scenario
def teardown(scenario):
    teardown_session()


@step(u'^Given a admin user is logged in$')
def given_a_admin_user_is_logged_in(step):
    login_as_the_admin()


@step(u'^Given a coordinator is logged in$')
def given_a_coordinator_is_logged_in(step):
    login_as_the_admin()


@step(u'^When he creates a campaign called "([^"]*)" with duties:$')
def when_he_creates_a_campaign_called_group1_with_duties(step, campaign_name):
    duty_names = [h['Name'] for h in step.hashes]
    create_campaign(campaign_name, duty_names)


@step(u'^Then he sees the "([^"]*)" campaign with the duties:$')
def then_he_sees_the_group1_campaign_with_the_duties(step, campaign_name):
    assert_was_created(campaign_name)
    duty_names = [h['Name'] for h in step.hashes]
    campaign = the('Campaign', name=campaign_name)
    assert_campaign_has_duties(campaign, duty_names)


@step(u'^When he creates a volunteer called "([^"]*)"$')
def when_he_creates_a_volunteer_called_group1(step, volunteer_name):
    create_volunteer(volunteer_name)


@step(u'^Then he sees that the volunteer "([^"]*)" was created$')
def then_he_sees_that_the_volunteer_group1_was_created(step, volunteer_name):
    assert_was_created(volunteer_name)


@step(u'When a volunteer views her plan')
def when_a_volunteer_views_her_plan(step):
    assert False, 'This step must be implemented'


@step(u'Then she sees the available duties for which she could volunteer')
def then_she_sees_the_available_duties_for_which_she_could_volunteer(step):
    assert False, 'This step must be implemented'


@step(u'When he creates a duty called "([^"]*)" in the "([^"]*)" campaign')
def when_he_creates_a_duty_called_group1_in_the_group2_campaign(step,
                                                                duty_name,
                                                                campaign_name):
    create_campaign(campaign_name)
    create_duty(duty_name, campaign_name)


@step(u'Then he sees that the duty "([^"]*)" was created in the "([^"]*)" campaign')
def then_he_sees_that_the_duty_group1_was_created_in_the_group2_campaign(step, duty_name, campaign_name):
    assert_was_created(campaign_name)
    assert_was_created(duty_name)
