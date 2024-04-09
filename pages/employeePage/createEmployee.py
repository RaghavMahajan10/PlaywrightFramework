from time import sleep


class createEmoloyee:
    
    def __init__(self,page):
        self.page=page
    
    def createEmply(self):
        self.page.get_by_role("link", name=" Employees").click()
        self.page.get_by_role("button", name=" Add Employee").click()
        self.page.get_by_placeholder("First Name").click()
        self.page.get_by_placeholder("First Name").fill("AutomationEmp")
        self.page.get_by_placeholder("Last Name").click()
        self.page.get_by_placeholder("Last Name").fill("AutomationLast")
        self.page.get_by_placeholder("000-00-0000").click()
        self.page.get_by_placeholder("000-00-0000").fill("12345678991")
        self.page.locator("#txtcellPhone").click()
        self.page.locator("#txtcellPhone").fill("(123) 445-67890")
        self.page.get_by_placeholder("Email").click()
        self.page.get_by_placeholder("Email").fill("automation@test.com")
        self.page.locator("#txtdOB").click()
        self.page.locator("#txtdOB").click()
        self.page.locator("#txtdOB").fill("10/01/1998")
        self.page.get_by_placeholder("Dependents").click()
        self.page.get_by_placeholder("Dependents").fill("2")
        self.page.locator("#ddlgender").select_option("8")
        self.page.locator("#ddlenthnicity").select_option("13")
        self.page.locator("#ddlempType").select_option("2")
        self.page.locator("#txtemgPhone").click()
        self.page.locator("#txtemgPhone").fill("(345) 566-55566")
        self.page.get_by_placeholder("Emergency Contact").click()
        self.page.get_by_placeholder("Emergency Contact").fill("3455666445")
        self.page.get_by_placeholder("Address").click()
        self.page.get_by_placeholder("Address").fill("135 test")
        self.page.get_by_placeholder("Apt / Unit").click()
        self.page.get_by_placeholder("Apt / Unit").fill("12")
        self.page.get_by_placeholder("City").click()
        self.page.get_by_placeholder("City").fill("test")
        self.page.locator("#ddlState").select_option("FL")
        self.page.get_by_placeholder("Zip Code").click()
        self.page.get_by_placeholder("Zip Code").fill("34535")
        self.page.locator("#ddltaxState").select_option("FL")
        self.page.locator("//button[text()='Save Employee']").click()
        sleep(5)
