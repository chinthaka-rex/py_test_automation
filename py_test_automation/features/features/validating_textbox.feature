Feature: Validating textbox

  Scenario: Verify the full name textbox
    Given launch browser
    When navigate to the demoqa textbox page "https://demoqa.com/text-box"
    Then enter the name into fullname "Roy Miller" textbox
    And enter the name into email "royy92@yomail.com" textbox
    And enter the name into current address "royy92, new york" textbox
    And enter the name into permanent address "royy94, new york" textbox
    Then click on the submit button
    When check the name inserted is equal to "Roy Miller"
    And check the email inserted is equal to "royy92@yomail.com"
    And check the current address inserted is equal to "royy92, new york"
    Then check the permanent address inserted is equal to "royy94, new york"