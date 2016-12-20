from behave import given, when, then

from grupos_personas import *


@given(u'a person')
def a_person(context):
    context._p0 = Person("juan", 23)


@given(u'another person')
def another_person(context):
    context._p1 = Person("juan", 22)


@when(u'added one to another')
def added_one_to_another(context):
    context._g0 = context._p0 + context._p1


@then(u'I should get a group')
def i_should_get_a_group(context):
    assert isinstance(context._g0, Group)


@then(u'The group should have two person')
def the_group_should_have_two_person(context):
    assert len(context._g0) == 2


@then(u'I should have the first one in the group')
def i_should_have_the_first_one_in_the_group(context):
    assert context._p0 in context._g0


@then(u'I should have the second one in the group')
def i_should_have_the_second_one_in_the_group(context):
    assert context._p1 in context._g0


@given(u'the same person')
def the_same_person(context):
    context._p2 = context._p0


@when(u'added one to same')
def added_one_to_same(context):
    context._g1 = context._p0 + context._p2


@then(u'The group should have one person')
def the_group_should_have_one_person(context):
    assert len(context._g1) == 1


@then(u'I should have the person in the group')
def i_should_have_the_person_in_the_group(context):
    assert context._p0 in context._g1
