class Availability:
    def __init__(self,page):
        self.page=page

    def addPreference(self):
        self.page.get_by_role("tab", name="Availability").click()
        self.page.locator("input[name=\"item\\[0\\]\"]").first.check()
        self.page.locator("input[name=\"item\\[1\\]\"]").first.check()
        self.page.get_by_role("textbox").first.click()
        self.page.get_by_role("textbox").first.click()
        self.page.get_by_role("textbox").first.fill("Fale")
        self.page.get_by_role("textbox").first.press("ArrowRight")
        self.page.get_by_role("textbox").first.fill("")
        self.page.get_by_role("textbox").first.click()
        self.page.get_by_role("textbox").first.fill("HINDI")
        self.page.get_by_role("button", name=" Save Changes").click()

    def addAvailbility(self):
        self.page.get_by_role("link", name=" Add Availability").click()
        self.page.get_by_label("Effective Date*").fill("2023-10-09")
        self.page.get_by_label("SATURDAY").check()
        self.page.get_by_label("SUNDAY").check()
        self.page.get_by_label("From Time").click()
        self.page.get_by_label("From Time").fill("09:00")
        self.page.get_by_label("To Time").click()
        self.page.get_by_label("To Time").fill("11:00")
        self.page.locator("div:nth-child(5) > .col-sm-3 > .time-inputs > div > #fromTime").click()
        self.page.locator("div:nth-child(5) > .col-sm-3 > .time-inputs > div > #fromTime").fill("08:00")
        self.page.locator("div:nth-child(5) > .col-sm-3 > .time-inputs > div:nth-child(2) > #toTime").click()
        self.page.locator("div:nth-child(5) > .col-sm-3 > .time-inputs > div:nth-child(2) > #toTime").fill("12:00")
        self.page.get_by_role("button", name=" Book Appointment").click()