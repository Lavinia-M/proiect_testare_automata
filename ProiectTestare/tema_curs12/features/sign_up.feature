Feature: Sign up

  Scenario: Verify if the url of Sign up and Sign in page are correct
    Given I am on the Jules SignIn page
      When I click sign up button
      Then I am redirected on the Sign up page
      Then I click login button
      Then I am again on the Signin page
