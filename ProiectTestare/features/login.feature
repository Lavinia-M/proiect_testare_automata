#Feature: Login
#
#    Scenario: Log in with invalid user and password
#        Given I am on the login page
#            When I enter username "popescu"
#            And I enter a password "1234"
#            And I press the login button
#            Then I receive an error message
#
#    Scenario: Log in with valid username and password
#        Given I am on the login page
#            When I enter username tomsmith
#            And I enter a password SuperSecretPassword!
#            And I press the login button
#            Then I am redirected to the secured area
#
#    Scenario: Log in with empty username and password
#        Given I am on the login page
#            When I press the login button
#            Then I receive an error message