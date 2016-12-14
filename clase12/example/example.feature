Feature: showing off behave

    Scenario: run a simple test of suma
        Given the number "1" as "int" and the number "2" as "int",
            when apply the function "suma"
            then i expect the result is "3" as "int"

    Scenario: run a simple test of division
        Given the number "1" as "int" and the number "2" as "float",
            when apply the function "division"
            then i expect the result is "0.5" as "float"

    Scenario: run a simple test of division by 0
        Given the number "1" as "int" and the number "0" as "float",
            and i expect an error,
            when apply the function "division"
            then i expect an error of type "ZeroDivisionError"



