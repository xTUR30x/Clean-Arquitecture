#Task Feature
Feature: Task Management

  Scenario: Add a new task successfully
    Given I am on the task page
    When I enter a valid title and description
    Then the task should be added to the task list

  Scenario: Fail to add a task with an empty title
    Given I am on the task page
    When I enter an empty title
    Then I should see an error message indicating that the title is required