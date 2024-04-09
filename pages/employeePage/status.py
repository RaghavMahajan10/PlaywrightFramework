from time import sleep


class Status:
    def __init__(self,page):
        self.page=page

    def addStatus(self):
        self.page.locator("//a//span[text()='Status']").click()
        self.page.locator("//a[text()=' Add Status']").click()
        self.page.locator("//select[@name='typeStatusId']").select_option("4: 85")
        self.page.get_by_placeholder("Effective Date").click()
        self.page.get_by_placeholder("Effective Date").click()
        self.page.get_by_placeholder("Effective Date").fill("11/11/2023")
        self.page.get_by_placeholder("Return Date").click()
        self.page.get_by_placeholder("Return Date").click()
        self.page.get_by_placeholder("Return Date").fill("12/11/2023")
        self.page.locator("#txtreason").select_option("notReliable")
        self.page.locator("input[name=\"Note\"]").click()
        self.page.locator("input[name=\"Note\"]").fill("automation testing")
        self.page.locator("#ddlScheduling").select_option("-1")
        self.page.get_by_role("button", name=" Save Changes").click()

        sleep(3)
        self.page.locator("//a[text()=' Add Status']").click()
        self.page.locator("#ddltypeStatusId").select_option("2: 83")
        self.page.locator("#txtreason").select_option("illness")
        self.page.get_by_placeholder("Effective Date").click()
        self.page.get_by_placeholder("Effective Date").fill("")
        self.page.get_by_placeholder("Effective Date").click()
        self.page.get_by_placeholder("Effective Date").fill("11/11/2023")
        self.page.get_by_placeholder("Return Date").click()
        self.page.get_by_placeholder("Return Date").click()
        self.page.get_by_placeholder("Return Date").fill("")
        self.page.locator("#ddlScheduling").select_option("1")
        self.page.get_by_role("button", name=" Save Changes").click()
        self.page.locator("//button//span[text()='×']").click()
