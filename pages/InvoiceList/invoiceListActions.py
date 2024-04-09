from time import sleep


class InvoiceList:
    def __init__(self,page):
        self.page=page

    def invoiceListActions(self,fromDate,toDate):
        #downloadPdf
        self.page.get_by_role("link", name=" Billing").click()
        self.page.get_by_role("button", name="Invoice List »").click()
        self.page.get_by_placeholder("From").click()
        self.page.get_by_placeholder("From").click()
        self.page.get_by_placeholder("From").fill(fromDate)
        self.page.get_by_placeholder("To").click()
        self.page.get_by_placeholder("To").click()
        self.page.get_by_placeholder("To").fill(toDate)
        self.page.locator("#ddlfStatus").select_option("1")
        #self.page.locator("//label[text()='Client']/following-sibling::select[@id='ddlpayer']").select_option("")
        self.page.get_by_role("button", name="GO").click()
        self.page.locator("//a[text()=' AutomationLast  AutomationFirst ']/../preceding-sibling::td//input").click()
        self.page.get_by_role("button", name="Download", exact=True).click()
        sleep(5)
        ####Send Email
        self.page.get_by_role("button", name="Send Email").click()
        sleep(5)
        ####Download Timesheet
        self.page.locator("//a[text()=' AutomationLast  AutomationFirst ']/../preceding-sibling::td//input").click()
        self.page.get_by_role("button", name='Timesheet').click()
        sleep(5)
        ### Status Open,paid,billed,hold
        self.page.locator("//a[text()=' AutomationLast  AutomationFirst ']/../preceding-sibling::td//input").click()
        self.page.get_by_role("button", name="Billed").click()
        sleep(5)
        self.page.get_by_role("link", name=" Billing").click()
        self.page.get_by_role("button", name="Invoice List »").click()
        self.page.get_by_placeholder("From").click()
        self.page.get_by_placeholder("From").click()
        self.page.get_by_placeholder("From").fill(fromDate)
        self.page.get_by_placeholder("To").click()
        self.page.get_by_placeholder("To").click()
        self.page.get_by_placeholder("To").fill(toDate)
        self.page.locator("#ddlfStatus").select_option("3")
        self.page.get_by_role("button", name="GO").click()
        self.page.locator("//a[text()=' AutomationLast  AutomationFirst ']/../preceding-sibling::td//input").click()
        self.page.get_by_role("button", name="Hold").click()
        sleep(5)
        self.page.get_by_role("link", name=" Billing").click()
        self.page.get_by_role("button", name="Invoice List »").click()
        self.page.get_by_placeholder("From").click()
        self.page.get_by_placeholder("From").click()
        self.page.get_by_placeholder("From").fill(fromDate)
        self.page.get_by_placeholder("To").click()
        self.page.get_by_placeholder("To").click()
        self.page.get_by_placeholder("To").fill(toDate)
        self.page.locator("#ddlfStatus").select_option("4")
        self.page.get_by_role("button", name="GO").click()
        self.page.locator("//a[text()=' AutomationLast  AutomationFirst ']/../preceding-sibling::td//input").click()
        self.page.get_by_role("button", name="Open").click()
        sleep(5)
        self.page.get_by_role("link", name=" Billing").click()
        self.page.get_by_role("button", name="Invoice List »").click()
        self.page.get_by_placeholder("From").click()
        self.page.get_by_placeholder("From").click()
        self.page.get_by_placeholder("From").fill(fromDate)
        self.page.get_by_placeholder("To").click()
        self.page.get_by_placeholder("To").click()
        self.page.get_by_placeholder("To").fill(toDate)
        self.page.locator("#ddlfStatus").select_option("1")
        self.page.get_by_role("button", name="GO").click()
        sleep(5)
        ## ManualPayment
        self.page.locator("//a[text()=' AutomationLast  AutomationFirst ']/../preceding-sibling::td//input").click()
        self.page.get_by_role("button", name="Payment").click()
        self.page.get_by_label("Payment Type").select_option("3")
        self.page.get_by_label("Payment Date").fill("2023-12-03")
        self.page.get_by_label("Document #").click()
        self.page.get_by_label("Document #").fill("automation")
        self.page.get_by_label("Payment Amount").click()
        self.page.get_by_label("Payment Amount").fill("62")
        self.page.get_by_label("Remainder").click()
        self.page.get_by_role("button", name="Register").click()
        self.page.get_by_role("button", name="GO").click()
        self.page.locator("#ddlfStatus").select_option("2")
        self.page.get_by_role("button", name="GO").click()
        sleep(5)

