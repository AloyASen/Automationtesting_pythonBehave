from behave import *

@given(u'chromedriver page is opened')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given chromedriver page is opened')


@given(u'Search term')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Search term')


@when(u'Internet connectivity is available')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Internet connectivity is available')


@then(u'google shows atleast 12 records')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then google shows atleast 12 records')