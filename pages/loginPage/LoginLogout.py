from utilites import commonUtility
class LoginLogout:

    def __init__(self,page):
        self.page = page

    def login(self):
        self.page.get_by_placeholder("Username").click()
        self.page.get_by_placeholder("Username").fill(commonUtility.readValue('USERNAME'))
        self.page.get_by_placeholder("Username").press("Tab")
        self.page.get_by_placeholder("Password").fill(commonUtility.readValue('PASSWORD'))
        self.page.get_by_placeholder("Password").press("Enter")


    def logout(self):
        self.page.get_by_role("button", name="admin@admin.com").click()
        self.page.get_by_text("Log Out").click()