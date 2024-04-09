class MedDaigonis:
    
    def __init__(self,page):
        self.page=page
    
    def createMedication(self):
        self.page.get_by_role("tab", name="Medications/Diagnosis").click()
        self.page.get_by_role("link", name=" Add Medications").click()
        self.page.locator("#txtEndDate").click()
        self.page.locator("#txtEndDate").click()
        self.page.locator("#txtEndDate").fill("10/08/2026")
        self.page.locator("#txtcategory").click()
        self.page.locator("#txtcategory").fill("Automation")
        self.page.locator("#txtcode").click()
        self.page.locator("#txtcode").fill("automation")
        self.page.locator("input[name=\"StrengthText\"]").click()
        self.page.locator("input[name=\"StrengthText\"]").fill("automation")
        self.page.locator("input[name=\"TabsText\"]").click()
        self.page.locator("input[name=\"TabsText\"]").fill("automation")
        self.page.locator("input[name=\"DosageText\"]").click()
        self.page.locator("input[name=\"DosageText\"]").fill("automation")
        self.page.get_by_role("spinbutton").click()
        self.page.get_by_role("spinbutton").fill("5")
        self.page.locator("input[name=\"RouteText\"]").click()
        self.page.locator("input[name=\"RouteText\"]").fill("automation")
        self.page.locator("input[name=\"PrescriberText\"]").click()
        self.page.locator("input[name=\"PrescriberText\"]").fill("automation")
        self.page.get_by_placeholder("Classification").click()
        self.page.get_by_placeholder("Classification").fill("automation")
        self.page.get_by_placeholder("Instructions/Notes").click()
        self.page.get_by_placeholder("Instructions/Notes").fill("automation")
        self.page.locator("input[name=\"administrationcheck\"]").check()
        self.page.get_by_role("button", name=" Save changes").click()
    
    
    def createDaigonis(self):
        self.page.get_by_role("link", name=" Add", exact=True).click()
        self.page.locator("input[name=\"isPrimary\"]").check()
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill("A14")
        self.page.get_by_role("option", name="A14-Daibites").click()
        self.page.get_by_role("button", name=" Save").click()
        
        
    