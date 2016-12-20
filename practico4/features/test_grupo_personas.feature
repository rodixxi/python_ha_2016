Feature: Adding two person generate a group

  Scenario: You can sum two persons and get a group 
    Given a person
      And another person
     When added one to another
     Then I should get a group

  Scenario: If you sum two different person they group have both of them 
    Given a person
      And another person
     When added one to another
     Then I should get a group
     Then The group should have two person
     Then I should have the first one in the group
     Then I should have the second one in the group

  Scenario: If you sum two person that are the same, the group have only one of them
    Given a person
      And the same person
     When added one to same
     Then I should get a group
     Then The group should have one person
     Then I should have the person in the group