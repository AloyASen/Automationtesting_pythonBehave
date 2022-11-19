Feature: Testing Google search
    Verify if google Search work on browser as expected

    Background:
        Given chromedriver page is opened 
    
    Scenario: Test google search
        Given Search term
        When Internet connectivity is available
        Then google shows atleast 12 records
    
    
    
    

    