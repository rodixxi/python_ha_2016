
from behave import *

import operators as op


@given('the number "{number}" and the number "{other_number}",')
def step_impl(context, number, other_number):
    context.number = int(number)
    context.other_number = int(other_number)


@when('apply the function "{function}"')
def step_impl(context, function):
    function = getattr(op, function)
    context.function_result = function(context.number, context.other_number)


@then('i expect the result is "{result}"')
def step_impl(context, result):
    result = int(result)
    assert context.function_result == result, "{} != {}".format(context.function_result, result)
