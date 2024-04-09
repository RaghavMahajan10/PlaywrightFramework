from time import sleep


class PlanOfCare:

    def __init__(self,page):
        self.page=page

    def createPOC(self):
        self.page.get_by_role("tab", name="Plan Of Care/Accommodation").click()
        self.page.get_by_role("link", name=" Add Plan of Care").click()
        self.page.locator("#chk_0_isChecked").check()
        self.page.locator("#chk_1_isChecked").check()
        self.page.locator("#txt_0_frequency").click()
        self.page.locator("#txt_0_frequency").fill("5")
        self.page.locator("#txt_1_frequency").fill("5")
        self.page.locator("#txt_1_frequency").click()
        self.page.locator("#txt_0_serviceNote").click()
        self.page.locator("#txt_0_serviceNote").fill("auromation")
        self.page.locator("#txt_1_serviceNote").click()
        self.page.locator("#txt_1_serviceNote").fill("automation")
        self.page.locator("//button[text()='Save changes']").click()
        sleep(5)

    def addAccomdation(self):
        self.page.locator("//label[text()=' Require work with children ']/../following-sibling::div/input").first.check()
        self.page.locator("//label[text()=' Smokers in household ']/../following-sibling::div/input").check()
        self.page.get_by_role("button", name=" Save Changes").click()