from time import sleep


class searchClient :

    def __init__(self,page):
        self.page = page

    def searchClientInClientList(self,clientId):
        # self.page.evaluate("document.body.style.zoom=0.8")
        self.page.get_by_role("link", name=" Clients").is_visible()
        self.page.get_by_role("link", name=" Clients").click()
        sleep(25)
        self.page.get_by_placeholder("Names, address, phone, SSN, all IDs").click()
        self.page.get_by_placeholder("Names, address, phone, SSN, all IDs").fill("Automation")
        self.page.get_by_role("link", name="AutomationLast AutomationFirst | "+clientId+" florida, NewYork 12344",exact=True).click()