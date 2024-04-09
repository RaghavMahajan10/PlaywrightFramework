class ContactLog:

    def __init__(self,page):
        self.page=page

    def addContactLog(self):
        self.page.get_by_role("tab", name="Contact Log/Notes").click()
        self.page.get_by_role("link", name=" Add Contact Log").click()
        self.page.locator("#txtreason").click()
        self.page.locator("#txtreason").fill("automation")
        self.page.locator("#txtissue").click()
        self.page.locator("#txtissue").fill("automation")
        self.page.get_by_placeholder("Schedule Date").click()
        self.page.get_by_placeholder("Schedule Date").click()
        self.page.get_by_placeholder("Schedule Date").fill("10/10/2023")
        self.page.get_by_placeholder("FollowUp Date").click()
        self.page.get_by_placeholder("FollowUp Date").click()
        self.page.get_by_placeholder("FollowUp Date").fill("10/10/2026")
        self.page.locator("#ddlEmployeeId").select_option("470")
        self.page.locator("#ddlOfficeUserId").select_option("5")
        self.page.locator("#txtnotes").click()
        self.page.locator("#txtnotes").fill("Automation")
        self.page.locator("#txtactionTaken").click()
        self.page.locator("#txtactionTaken").fill("automation")
        self.page.locator("#txtisSchedule").check()
        self.page.get_by_role("button", name=" Save").click()


    def addNotes(self):
        self.page.get_by_role("link", name=" Add Note").click()
        self.page.locator("#ddlNoteType").get_by_role("textbox").click()
        self.page.get_by_role("option", name="Attempted contact").click()
        self.page.locator("#txtnotes").click()
        self.page.locator("#txtnotes").fill("hello automation")
        self.page.locator("#ddlofficeUserId").select_option("5")
        self.page.locator("#ddlempId").select_option("470")
        self.page.locator("#txtisText").check()
        self.page.locator("form[name=\"frmclientnote\"] div").filter(has_text="Screen").nth(3).click()
        self.page.locator("#txtisScreen").check()
        self.page.get_by_role("button", name=" Save Note").click()
