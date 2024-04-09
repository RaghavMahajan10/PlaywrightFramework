from time import sleep


class AddInvoice:

    def __init__(self,page):
        self.page=page

    def addInvoice(self,fromDate,toDate):
        self.page.get_by_role("link", name=" Billing").click()
        self.page.get_by_role("button", name="Create Invoice »").click()
        self.page.locator(".input-group-addon").first.click()
        self.page.get_by_placeholder("From").click()
        self.page.get_by_placeholder("From").click()
        self.page.get_by_placeholder("From").fill(fromDate)
        self.page.get_by_placeholder("To").click()
        self.page.get_by_placeholder("To").click()
        self.page.get_by_placeholder("To").fill(toDate)
        #self.page.locator("//label[text()='Client']//following-sibling::select").select_option(clientId)
        self.page.locator("//label[text()=' Billing Status']//following-sibling::select").select_option("All")
        self.page.get_by_role("button", name="GO").click()
        sleep(5)
        self.page.locator("//strong[text()=' AutomationLast AutomationFirst ']/../preceding-sibling::div/label/input").click()
        sleep(5)
        self.page.locator("//strong[text()='Nonbillable']/../following-sibling::div/a[text()=' Add Invoice ']").click()
        sleep(5)