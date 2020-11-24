Feature: Add/Edit products
    Accessing pages for product management.
    creating new and editing existing products.

    Background: Logged in as admin
        Given I am logged in as Admin

    Scenario: Expand Catalog option in side menu
        Given there is a side menu
        And there is a Catalog option
        When I click Catalog option
        Then Catalog option expands into multiple options

    Scenario: Access product page
        Given Catalog option on the side menu is expanded
        And there is a Products option
        When I click on the Products option
        Then Products page is displayed

    Scenario: Access Edit Product page
        Given I am on the Products page
        And a product is displayed in a product list
        When I click on products Edit button
        Then I access its Edit Product page

    Scenario: Edit product
        Given I am on Edit Product page
        And I edited some information
        And all required fields are filled
        When I click the Save button
        Then edited information is saved
        And the Product list is displayed

    Scenario: Access Add product page
        Given I am on the Products page
        When I click Add New button
        Then Add product page is displayed

    Scenario: Add product
        Given I am on the Add product page
        And all required fields are filled
        When I click the Save button
        Then new product is added
        And the Product list is displayed