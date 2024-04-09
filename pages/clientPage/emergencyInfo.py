class EmergencyInfo:
    def __init__(self,page):
        self.page = page

    def fillPrimaryContact(self):
        self.page.get_by_role("tab", name="Emergency Info").click()
        self.page.locator("form").filter(has_text="Primary Contact NameRelationshipPhoneEmail").locator("#txtname").click()
        self.page.locator("form").filter(has_text="Primary Contact NameRelationshipPhoneEmail").locator("#txtname").fill(
            "Automation")
        self.page.locator("form").filter(has_text="Primary Contact NameRelationshipPhoneEmail").locator(
            "#txtrelationship").click()
        self.page.locator("form").filter(has_text="Primary Contact NameRelationshipPhoneEmail").locator(
            "#txtrelationship").fill("Father")
        self.page.locator("form").filter(has_text="Primary Contact NameRelationshipPhoneEmail").get_by_placeholder(
            "(123) 123-1234").click()
        self.page.locator("form").filter(has_text="Primary Contact NameRelationshipPhoneEmail").get_by_placeholder(
            "(123) 123-1234").fill("(123) 456-78900")
        self.page.locator("form").filter(has_text="Primary Contact NameRelationshipPhoneEmail").locator("#txtemail").click()
        self.page.locator("form").filter(has_text="Primary Contact NameRelationshipPhoneEmail").locator("#txtemail").fill(
            "auto@gmail.com")
        self.page.locator("form").filter(has_text="Primary Contact NameRelationshipPhoneEmail").get_by_title(
            "Save Changes").click()

    def fillSecondaryContact(self):
        self.page.locator("form").filter(has_text="Secondary Contact NameRelationshipPhoneEmail").locator("#txtname").click()
        self.page.locator("form").filter(has_text="Secondary Contact NameRelationshipPhoneEmail").locator("#txtname").fill(
            "automatio1")
        self.page.locator("form").filter(has_text="Secondary Contact NameRelationshipPhoneEmail").locator(
            "#txtrelationship").click()
        self.page.locator("form").filter(has_text="Secondary Contact NameRelationshipPhoneEmail").locator(
            "#txtrelationship").fill("Mother")
        self.page.locator("form").filter(has_text="Secondary Contact NameRelationshipPhoneEmail").get_by_placeholder(
            "(123) 123-1234").click()
        self.page.locator("form").filter(has_text="Secondary Contact NameRelationshipPhoneEmail").get_by_placeholder(
            "(123) 123-1234").fill("(232) 454-33556")
        self.page.locator("form").filter(has_text="Secondary Contact NameRelationshipPhoneEmail").locator(
            "#txtemail").click()
        self.page.locator("form").filter(has_text="Secondary Contact NameRelationshipPhoneEmail").locator("#txtemail").fill(
            "auto1@gmail.com")
        self.page.locator("form").filter(has_text="Secondary Contact NameRelationshipPhoneEmail").get_by_title(
            "Save Changes").click()

    def fillPhysican(self):
        self.page.locator("#txtfirstName").click()
        self.page.locator("#txtfirstName").fill("Tester")
        self.page.locator("#txtlastName").click()
        self.page.locator("#txtlastName").fill("Mahajan")
        self.page.locator("#txttitle").click()
        self.page.locator("#txttitle").fill("DR")
        self.page.locator("#txtnPINumber").click()
        self.page.locator("#txtnPINumber").fill("12345")
        self.page.locator("#txtlicense").click()
        self.page.locator("#txtlicense").fill("2232422")
        self.page.get_by_placeholder("MM/dd/YYYY", exact=True).click()
        self.page.get_by_placeholder("MM/dd/YYYY", exact=True).fill("10/09/2025")
        self.page.locator("#txtaddress").click()
        self.page.locator("#txtaddress").fill("123fffwwf")
        self.page.locator("#txtcity").click()
        self.page.locator("#txtcity").fill("florida")
        self.page.locator("#txtstate").click()
        self.page.locator("#txtstate").fill("florida")
        self.page.locator("#txtzip").click()
        self.page.locator("#txtzip").fill("12344")
        self.page.locator("//form[@class='ng-pristine ng-valid ng-touched']//input[@id='txtemail']").click()
        self.page.locator("//form[@class='ng-pristine ng-valid ng-touched']//input[@id='txtemail']").fill("test@ymail.com")
        self.page.locator("//form[@class='ng-pristine ng-valid ng-touched']//input[@id='txtphone']").click()
        self.page.locator("//form[@class='ng-pristine ng-valid ng-touched']//input[@id='txtphone']").fill("(456) 746-63356")
        self.page.locator("#txtfax").click()
        self.page.locator("#txtfax").fill("23454343")
        self.page.locator("//form[@class='ng-pristine ng-valid ng-touched']//a[@title='Save Changes']").click()

    def addPayer(self):
        self.page.get_by_role("link", name=" Add Provider").click()
        self.page.get_by_role("dialog").locator("#txtfirstName").click()
        self.page.get_by_role("dialog").locator("#txtfirstName").fill("eweww")
        self.page.get_by_role("dialog").locator("#txtlastName").click()
        self.page.get_by_role("dialog").locator("#txtlastName").fill("rwwr")
        self.page.get_by_role("dialog").locator("#txttitle").fill("wr")
        self.page.get_by_role("dialog").locator("#txttitle").click()
        self.page.get_by_role("dialog").locator("#txttitle").fill("wrr")
        self.page.get_by_role("dialog").locator("#txtnPINumber").fill("w")
        self.page.get_by_role("dialog").locator("#txtnPINumber").click()
        self.page.get_by_role("dialog").locator("#txtnPINumber").fill("132324")
        self.page.get_by_role("dialog").locator("#txtlicense").fill("231")
        self.page.get_by_role("dialog").locator("#txtlicense").click()
        self.page.get_by_role("dialog").locator("#txtlicense").fill("2314243")
        self.page.get_by_role("dialog").get_by_placeholder("MM/dd/YYYY").click()
        self.page.get_by_role("dialog").get_by_placeholder("MM/dd/YYYY").click()
        self.page.locator("app-emergency-provider").get_by_placeholder("MM/dd/YYYY").fill("10/09/2028")
        self.page.locator("app-emergency-provider #txtaddress").click()
        self.page.get_by_role("dialog").locator("#txtaddress").fill("r333r")
        self.page.get_by_role("dialog").locator("#txtcity").click()
        self.page.get_by_role("dialog").locator("#txtcity").click()
        self.page.get_by_role("dialog").locator("#txtcity").fill("floria")
        self.page.get_by_role("dialog").locator("#txtstate").click()
        self.page.get_by_role("dialog").locator("#txtstate").fill("florida")
        self.page.get_by_role("dialog").locator("#txtzip").click()
        self.page.get_by_role("dialog").locator("#txtzip").fill("12345")
        self.page.get_by_role("dialog").locator("#txtemail").click()
        self.page.get_by_role("dialog").locator("#txtemail").fill("test@test.com")
        self.page.get_by_role("dialog").get_by_placeholder("(123) 123-1234").click()
        self.page.get_by_role("dialog").get_by_placeholder("(123) 123-1234").fill("(131) 231-33131")
        self.page.get_by_role("dialog").locator("#txtfax").fill("1")
        self.page.get_by_role("dialog").locator("#txtfax").click()
        self.page.get_by_role("dialog").locator("#txtfax").fill("131331")
        self.page.get_by_role("button", name="Save Provider").click()

    def editPayer(self):
        self.page.get_by_role("link", name="").click()
        self.page.get_by_role("dialog").locator("#txtfirstName").click()
        self.page.get_by_role("dialog").locator("#txtfirstName").click()
        self.page.get_by_role("dialog").locator("#txtfirstName").fill("reerre")
        self.page.get_by_role("button", name="Save Provider").click()