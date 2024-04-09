from time import sleep


class EMRRecords:

    def __init__(self,page):
        self.page=page

    def createFolder(self):
        self.page.get_by_role("tab", name="EMR Records/files").click()
        self.page.get_by_placeholder("Folder Name").click()
        self.page.get_by_placeholder("Folder Name").fill("Automation")
        self.page.get_by_role("button", name=" Add Folder").click()



    def uploadFile(self):
        self.page.locator("#ddlFolderId").select_option("Automation")
        #self.page.get_by_placeholder("Inlcude some file").click()
        self.page.get_by_placeholder("Inlcude some file").set_input_files("../resources/TimeSheet__06_Oct_2023_02_56_30_PM.pdf")
        self.page.get_by_role("button", name="Upload File").click()
        sleep(5)
