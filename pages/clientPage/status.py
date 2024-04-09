class status:

    def __init__(self,page):
        self.page = page

    def clientStatus(self):
       self.page.get_by_role("tab", name="Status").click()
       self.page.get_by_role("link", name=" Add Status").click()
       self.page.locator("select[name=\"ActivityId\"]").select_option("4")
       #self.page.get_by_placeholder("Date", exact=True).click()
       #self.page.get_by_text("28", exact=True).click()
       self.page.locator("select[name=\"ReferralCode\"]").select_option("49")
       self.page.locator("#txtNote").click()
       self.page.locator("#txtNote").fill("Hello testing through automation")
       self.page.locator("#ddlScheduling").select_option("5")
       self.page.locator("#ddlOfficeUserId").select_option("470")
       self.page.locator("#txtEmail").check()
       self.page.get_by_role("button", name=" Save Status").click()

    def editStatus(self):
       self.page.locator("//label[text()='Hello testing through automation']/../following-sibling::td[1]/a[@title='Edit']").click()
       self.page.locator("select[name=\"ActivityId\"]").select_option("1")
       self.page.locator("select[name=\"ReferralCode\"]").select_option("47")
       self.page.locator("#txtNote").click()
       self.page.locator("#txtNote").fill("Hello testing through automation editing")
       self.page.get_by_role("dialog").locator("div").filter(has_text="Save Changes").nth(4).click()

    def deleteStatus(self):

       self.page.once("dialog", lambda dialog: dialog.dismiss())
       self.page.locator("//label[text()='Hello testing through automation']/../following-sibling::td[1]/a[@title='Edit']").click()