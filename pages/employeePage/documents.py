class Documents:
    def __init__(self,page):
        self.page=page

    def uploadDocument(self):
        self.page.get_by_role("tab", name="Documents").click()
        self.page.locator("#ddlFolderId").select_option("172")
        #self.page.get_by_placeholder("Inlcude some file").click()
        self.page.get_by_placeholder("Inlcude some file").set_input_files("../resources/TimeSheet__06_Oct_2023_02_56_30_PM.pdf")
        self.page.get_by_role("button", name="Upload File").click()
        self.page.get_by_role("link", name=" Competency Evaluation (1 files)").click()

   