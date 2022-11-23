# Product Backlog: ItemList

## User Stories

### User Story 1

As a new user, I need to be able to create a new account so that I can use the application.

**Size: Small -** Login and registration pages are created.

**Acceptance Criteria:**

    Given: I am a new user
    And:   I am on the registration page
    When:  I enter my username
    And:   I enter a valid password
    And:   I click on the "Login" button
    Then:  My account is created
    And:   I am redirected to the home page
<!-- tsk -->
    Given: I am a new user
    And:   I am on the registration page
    When:  I enter my username
    And:   I enter do not enter a password
    And:   I click on the "Login" button
    Then:  My account is not created
    And:   I should see an error message

### User Story 2

As a user, I need to be able to login so that I can use the application.

**Size: Small -** Login and registration pages are created.

**Acceptance Criteria:**

    Given: I am a user
    When:  I visit the login page
    And:   I enter my username
    And:   I enter my password
    And:   I click on the "Login" button
    Then:  I should be taken to the home page
<!-- tsk -->
    Given: I am a user
    When:  I visit the login page
    And:   I enter my username
    And:   I enter an invalid password
    And:   I click on the "Login" button
    Then:  I should be taken to the login page
    And:   I should see an error message
<!-- tsk -->
    Given: I am a user
    When:  I visit the login page
    And:   I enter my username
    And:   I do not enter a password
    And:   I click on the "Login" button
    Then:  I should be taken to the login page
    And:   I should see an error message

### User Story 3

As a user, I need to be able to add items to my list so that I can keep track of them.

**Size: Small -** Add item page is created.

**Acceptance Criteria:**

    Given: I am a user
    And:   I am logged in
    When:  I visit the add item page
    And:   I enter an item
    And:   I click on the "Add" button
    Then:  The item should be added to my list
