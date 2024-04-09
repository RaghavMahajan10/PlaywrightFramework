class Compilance:
    
    def __init__(self,page):
        self.page=page
        
    def addCompilance(self):
        self.page.get_by_role("tab", name="Compliance").click()
        self.page.get_by_role("link", name=" Add Compliance").click()
        self.page.get_by_placeholder("Due Date").click()
        self.page.get_by_placeholder("Due Date").click()
        self.page.get_by_placeholder("Due Date").fill("12/10/2023")
        # self.page.get_by_placeholder("Completed On").click()
        # self.page.get_by_placeholder("Completed On").fill("12/30/2023")
        self.page.locator("//select[@name='category']").select_option("Initial Assessments")
        self.page.locator("#ddldocumentId").select_option("675_Client Assessment-Case Monitoring.pdf")
        self.page.locator("#ddlNurse").select_option("704")
        self.page.locator("#ddlisStatus").select_option("69")
        self.page.get_by_placeholder("Notes").click()
        self.page.get_by_placeholder("Notes").fill("Automation ")
        self.page.locator("//form[@name='frmIncident']//label[text()='Employee']//..//select").select_option("470")
        self.page.get_by_role("button", name=" Save Changes").click()

    def editCompilance(self):
        self.page.get_by_role("gridcell", name="").locator("a").click()
        self.page.get_by_placeholder("Notes").click()
        self.page.get_by_placeholder("Notes").fill("Automation Edit")
        self.page.get_by_role("button", name=" Save Changes").click()