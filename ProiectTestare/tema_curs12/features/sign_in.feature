Feature: SignIn Page

  Scenario: Try to sign in with correct email and no password
    Given I am on the SignIn page
      When I enter a correct email
      And I leave password empty
      Then The login button is disabled
      And A message error with text: "Please enter your password!" appears

    Scenario: Try to see the password
      Given I am on the SignIn page
        When I enter a correct email
        And I enter a password
        And I press the eye button
        Then I should see the password