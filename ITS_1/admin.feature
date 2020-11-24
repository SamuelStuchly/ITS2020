Feature: Admin login/logout

    Scenario: Log in as Admin
        Given I am on the admin login page
        When I input admin username and password
        Then I am logged in as Admin
        And  Admin view of page is displayed

    Scenario: Fail to log in as Admin
        Given I am on the admin login page
        When I input wrong username or password
        Then I am not logged in as admin
        And  warning is displayed

    Scenario: Logout from Admin
        Given I am logged in as Admin
        When I click logout button
        Then Admin login page is displayed
        And I am logged out
