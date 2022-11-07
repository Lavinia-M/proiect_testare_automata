Feature: Sign up guideline

  Scenario Outline: Steps to sign up correctly
    Given I am on the Sign in page
    When I click Sign up link
    And I click Person option
    And I click continue
    And I input "Popescu" to the first name field
    And I click continue
    And I input "Ion" to the last name
    And I click continue
    And I input "<email>" to the email field
    Then A message is <on/off>

    Examples: Typing a wrong email, then try a correct email
    |email             |on/off       |
    |popescu@yaahoo    |displayed    |
    |popescu@yahoo.com |not displayed|