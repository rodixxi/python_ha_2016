
from behave import *

import operators as op

TYPES = {t.__name__: t for t in (int, float, complex)}


@given('the number "{number}" as "{typen}" and the number "{other_number}" as "{typeon}",')
def step_impl(context, number, typen, other_number, typeon):
    typen = TYPES[typen]
    typeon = TYPES[typeon]
    context.number = typen(number)
    context.other_number = typeon(other_number)

@given(u'i expect an error,')
def step_impl(context):
    def catch(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                context.error = err
        return inner
    context.catch = catch



@when('apply the function "{function}"')
def step_impl(context, function):
    function = getattr(op, function)
    if hasattr(context, "catch"):
        function = context.catch(function)
    context.function_result = function(context.number, context.other_number)


@then('i expect the result is "{result}" as "{typer}"')
def step_impl(context, result, typer):
    typer = TYPES[typer]
    result = typer(result)
    assert context.function_result == result, "{} != {}".format(context.function_result, result)


@then(u'i expect an error of type "{error_name}"')
def step_impl(context, error_name):
    actual = type(context.error).__name__
    assert actual == error_name, "{} != {}".format(actual, error_name)

