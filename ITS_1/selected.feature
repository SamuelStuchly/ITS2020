Feature: Delete/Copy selected products
    Actions with selected products from Product list.

    Background: Logged in as admin, on product page, selected product
        Given I am logged in as Admin
        And I am on the Products page
        And at least one product is selected

    Scenario: Delete product
        When I click delete button
        Then selected products are deleted

    Scenario: Copy product
        When I click the Copy button
        Then for each selected product a copy is added into Product list
