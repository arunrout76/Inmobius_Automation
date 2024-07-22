Feature: Inmobious Login Functionalty

 Scenario: Login With Correct credentials
 
    Given I am on the login page
    When I enter username "13831ZQTX"
    And I enter password "qwerty"
    And I click the login button
    Then It should display "Login ID:" after logged in successfully