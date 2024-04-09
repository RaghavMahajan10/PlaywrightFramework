from time import sleep


class Compilance:
    def __init__(self,page):
        self.page=page

    def addCompilance(self):
        self.page.get_by_role("tab", name="Compliance").click()
        self.page.get_by_role("link", name=" Add Compliance").click()
        self.page.get_by_placeholder("Due Date").click()
        self.page.get_by_placeholder("Due Date").click()
        self.page.get_by_placeholder("Due Date").fill("12/12/2024")
        self.page.get_by_placeholder("Completed On").click()
        self.page.get_by_placeholder("Completed On").click()
        self.page.locator("#ddlCategory").select_option("6")
        self.page.locator("#ddlCode").select_option("38")
        self.page.locator("#ddlNurse").select_option("723")
        self.page.get_by_role("textbox", name="Notes").click()
        self.page.get_by_role("textbox", name="Notes").fill("automation test")
        self.page.get_by_role("button", name=" Save Changes").click()

    def editCompilance(self):
        self.page.get_by_role("tabpanel").locator("label span").click()
        sleep(5)
