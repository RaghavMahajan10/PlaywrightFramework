class BillingDetails:

    def __init__(self,page):
        self.page=page

    def enterBilling(self):
        self.page.get_by_role("tab", name="Billing Details").click()
        self.page.get_by_placeholder("Contact Name").click()
        self.page.get_by_placeholder("Contact Name").fill("Automation")
        self.page.get_by_role("textbox", name="(123) 123-1234").click()
        self.page.get_by_role("textbox", name="(123) 123-1234").fill("(232) 134-44567")
        self.page.get_by_placeholder("Fax number").click()
        self.page.get_by_placeholder("Fax number").fill("12345")
        self.page.get_by_placeholder("Email Address").click()
        self.page.get_by_placeholder("Email Address").fill("automation@gmail.com")
        self.page.get_by_placeholder("Mailing address").click()
        self.page.get_by_placeholder("Mailing address").fill("Automation house")
        self.page.locator("select[name=\"day\"]").select_option("3")
        self.page.locator("select[name=\"type\"]").select_option("2")
        self.page.get_by_role("button", name=" Save").click()
        