class Incidents:
    def __init__(self,page):
        self.page=page

    def addIncidents(self):
        self.page.get_by_role("tab", name="Notes/Incidents").click()
        self.page.get_by_role("link", name=" Add Incidents").click()
        self.page.locator("#ddlClientId").select_option("469")
        self.page.get_by_placeholder("Description").click()
        self.page.get_by_placeholder("Description").fill("automationtest")
        self.page.get_by_role("button", name=" Save Changes").click()

    def addNotes(self):
        self.page.get_by_role("link", name=" Add Notes").click()
        self.page.get_by_placeholder("employeeNotes Date").click()
        self.page.get_by_placeholder("employeeNotes Date").fill("09/09/2023")
        self.page.locator("#ddlClientId").select_option("469")
        self.page.get_by_placeholder("Description").click()
        self.page.get_by_placeholder("Description").fill("automationtest")
        self.page.get_by_role("button", name=" Save Changes").click()
