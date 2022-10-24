Feature: Home Page

    Scenario: Redirect to Form Authentication
        Given I am on the home page
            When I click the Form Authentication link
            Then I am redirected to the Form Authentication page

    Scenario: Redirect to Add Remove Elements
        Given I am on the home page
            When I click the Add Remove Elements link
            Then I am redirected to the Add Remove Elements page

    Scenario: Redirect to File Download
        Given I am on the home page
            When I click the File Download link
            Then I am redirected to the File Download page

