import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class addCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    drpNewsletter_xpath = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']"
    lstitemTestStore2_xpath = "//option[text()='Test store 2']"
    lstitemYourStore_xpath = "//option[text()='Your store name']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerBtn(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def enterEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def enterFirstName(self, firstName):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(firstName)

    def enterLastName(self, lastName):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lastName)

    def selectGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()

    def enterDateOfBith(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def enterCompanyName(self, company):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(company)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)
        time.sleep(3)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def selectNewsLetter(self, value):
        self.driver.find_element(By.XPATH, self.drpNewsletter_xpath).click()
        time.sleep(5)
        if value == "Test store 2":
            self.driver.find_element(By.XPATH, self.lstitemTestStore2_xpath).click()
        elif value == "Your store name":
            self.driver.find_element(By.XPATH, self.lstitemYourStore_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.lstitemTestStore2_xpath).click()

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def getSuccessText(self):
        txtSuccess_xpath = "//div[@class='alert alert-success alert-dismissable']"
        text = self.driver.find_element(By.XPATH, txtSuccess_xpath).text
        return text
