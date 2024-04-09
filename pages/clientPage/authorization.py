class Authorization:

    def __init__(self,page):
        self.page=page

    def createAuthorization(self):
        self.page.get_by_role("tab", name="Authorizations").click()
        self.page.get_by_role("link", name=" Add Authorization").click()
        self.page.locator("#payer").select_option("72")
        self.page.locator("input[name=\"contractClientId\"]").click()
        self.page.locator("input[name=\"contractClientId\"]").fill("1234")
        self.page.locator("input[name=\"authorizationNumber\"]").click()
        self.page.locator("input[name=\"authorizationNumber\"]").fill("1234")
        self.page.locator("#txtFromDateTime").click()
        self.page.locator("#txtFromDateTime").fill("01/01/2023")
        self.page.locator("#txtToDateTime").click()
        self.page.locator("#txtToDateTime").fill("01/01/2026")
        self.page.locator("#serviceCode").select_option("58")
        self.page.locator("#hoursAuthorizedPerWeek").click()
        self.page.locator("#hoursAuthorizedPerWeek").fill("20")
        self.page.locator("#periodEpisode_Notes").click()
        self.page.locator("#periodEpisode_Notes").fill("hello automation")
        self.page.get_by_role("button", name="Add").click()



