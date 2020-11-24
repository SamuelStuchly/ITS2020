Feature: Organise Product list
    Filtering and ordering of products displayed in Product list.

    Background: Logged in as admin, on Product page
        Given I am logged in as Admin
        And I am on the Products page

    Scenario: Display filtered Product list
        Given I have set filters to desired values
        When I press the filter button
        Then filtered Product list is displayed
