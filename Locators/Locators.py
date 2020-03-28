class Locators(object):
    # Locator Objects for Online Shopping Launch Page
    txt_searchItem_By_ID = "search_query_top"
    btn_searchButton_By_CSS = ".button-search"
    link_signin_By_LinkText = "Sign in"

    # Locator Objects for Online Shopping Login Page
    txt_createAccount_email_By_CSS = "#email_create"
    btn_createAccount_email_By_CSS = "#SubmitCreate"
    txt_creatingAccount_email_error_By_CSS = "#create_account_error ol li"
    txt_registeredEmail_By_CSS = "#email"
    txt_registeredPassword_By_CSS = "#passwd"
    btn_registeredLogin_By_CSS = "#SubmitLogin"
    txt_registeredEmail_error_By_CSS = ".alert-danger>ol>li"

    # Locator Objects for Online Shopping New Customer Account Creation Page
    radio_title_option_By_Xpath = "//input[@name='id_gender']"  # Values : 1 or 2
    txt_customerfirstName_By_CSS = "#customer_firstname"
    txt_customerlastName_By_CSS = "#customer_lastname"
    txt_password_By_CSS = "#passwd"
    select_Days_By_CSS = "#days"
    select_Months_By_CSS = "#months"
    select_Years_By_CSS = "#years"
    txt_firstname_By_CSS = "#firstname"
    txt_lastname_By_CSS = "#lastname"
    txt_address_By_CSS = "#address1"
    txt_city_By_CSS = "#city"
    select_state_By_CSS = "#id_state"
    txt_ZipPostalCode_By_CSS = "#postcode"
    select_Country_By_CSS = "#id_country"
    txt_mobilePhone_By_CSS = "#phone_mobile"
    txt_address_alias_By_CSS = "#alias"
    btn_submitAccountCreation_By_CSS = "#submitAccount"
