Feature: User Account Management

  Scenario: Register a new user successfully
    Given I am on the registration page
    When I enter a valid username and password
    Then my account should be created and I should be redirected to the homepage

  Scenario: Fail to register with an existing username
    Given I am on the registration page
    When I enter a username that already exists
    Then I should see an error message indicating that the username is already taken

  Scenario: Fail to register without a password
    Given I am on the registration page
    When I do not enter a password
    Then I should see an error message indicating that the password is required