class GroupInfo:
    
    def __init__(self,page):
        self.page=page
    
    def addGroup(self):
        self.page.get_by_role("tab", name="Group Info").click()
        self.page.get_by_role("link", name=" Add Group Info").click()
        self.page.locator("#txtcommunitName").click()
        self.page.locator("#txtcommunitName").fill("Automation")
        self.page.locator("#ddlcommunityType").select_option("Community")
        self.page.locator("#txtcommunitaddr").click()
        self.page.locator("#txtcommunitaddr").fill("Automation house")
        self.page.locator("#txtauf").click()
        self.page.locator("#txtauf").fill("123")
        self.page.get_by_role("dialog").locator("#txtcity").click()
        self.page.get_by_role("dialog").locator("#txtcity").fill("Automation")
        self.page.locator("#ddlcountryId").select_option("AFG")
        self.page.locator("#ddlcountryId").select_option("USA")
        self.page.locator("#ddlstateId").select_option("NY")
        self.page.locator("input[name=\"zip\"]").click()
        self.page.locator("input[name=\"zip\"]").fill("14500")
        self.page.get_by_role("textbox", name="(123) 123-1234").click()
        self.page.get_by_role("textbox", name="(123) 123-1234").fill("(123) 435-45667")
        self.page.get_by_role("dialog").locator("#txtemail").click()
        self.page.get_by_role("dialog").locator("#txtemail").fill("automation@gmail.com")
        self.page.locator("#txtnotes").click()
        self.page.locator("#txtnotes").fill("Automationnotes")
        self.page.get_by_role("button", name="Add").click()

    def editGroupInfo(self):
        self.page.get_by_role("link", name="").click()
        self.page.locator("#ddlstateId").select_option("NM")
        self.page.get_by_role("button", name="Add").click()