*** Settings ***
Library  ../AppLibrary.py
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  Opaa
    Set Password  Heppa123
    Confirm Password  Heppa123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  Ab
    Set Password  Heppa123
    Confirm Password  Heppa123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  Opaa
    Set Password  Ab
    Confirm Password  Ab
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
    
    Set Username  Opaa
    Set Password  password
    Confirm Password  password
    Submit Credentials
    Register Should Fail With Message  Password must contain at least one number and one uppercase letter

Register With Nonmatching Password And Password Confirmation
    Set Username  Opaa
    Set Password  Heppa123
    Confirm Password  Heppa456
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  Lelle
    Set Password  Leikkii12
    Confirm Password  Leikkii12
    Submit Credentials
    Register Should Fail With Message  User with that username already exists

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  Lelle  Leikkii12
    Go To Register Page