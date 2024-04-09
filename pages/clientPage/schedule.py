from time import sleep


class Schedule:

    def __init__(self,page):
        self.page=page

    def createDaySchedule(self,date):
        self.page.get_by_role("tab", name="Schedule", exact=True).click()
        #//strong[text()='10/02/2023']/../../following-sibling::div[2]//div//a
        self.page.get_by_role("cell", name=str(date)+" ").get_by_role("link").click()
        self.page.locator("//timepicker[@name='StartTime']//tr[2]/td/input[@placeholder='HH']").click()
        self.page.locator("//timepicker[@name='StartTime']//tr[2]/td/input[@placeholder='HH']").fill("01")

        self.page.locator("//timepicker[@name='StartTime']//tr[2]/td/input[@placeholder='MM']").click()
        self.page.locator("//timepicker[@name='StartTime']//tr[2]/td/input[@placeholder='MM']").fill("00")

        self.page.locator("//timepicker[@name='EndTime']//tr[2]/td/input[@placeholder='HH']").click()
        self.page.locator("//timepicker[@name='EndTime']//tr[2]/td/input[@placeholder='HH']").fill("03")

        self.page.locator("//timepicker[@name='EndTime']//tr[2]/td/input[@placeholder='MM']").click()
        self.page.locator("//timepicker[@name='EndTime']//tr[2]/td/input[@placeholder='MM']").fill("00")
        self.page.locator("//select[@id='ddlpayerId']").select_option("Private Pay (South Plainfield) HourlyPrivate 12/01/2021 - 07/31/2035")
        self.page.locator("select[name=\"EmpId\"]").select_option("470")
        self.page.get_by_role("button", name="SCHEDULE").click()


    def doSignIn(self,date):
        self.page.locator("//strong[text()='"+date+"']/../..//following-sibling::div//div//a//div[2]//div//span//span[text()='Sign In']").click()
        self.page.locator("//button[text()='Update Meeting ']").click()
        self.page.locator("//button[text()='SAVE']").click()
        sleep(5)

    def doSignOut(self,date):
        #self.page.locator("//strong[text()='"+date+"']/../..//following-sibling::div//div//a//div[2]//div//span//span[text()='Sign Out']").click()
        self.page.locator("//span[text()='Sign Out']").click()
        self.page.locator("//button[text()='Update Meeting ']").click()
        self.page.locator("//button[text()='SAVE']").click()
        sleep(5)


    def createWeeklySchedule(self):
        self.page.get_by_role("tab", name="Schedule", exact=True).click()
        sleep(5)
        self.page.get_by_role("button", name="Weekly Recurring Schedule").click()
        self.page.locator(".col-lg-6 > .form-control").first.select_option("12:00 AM")
        self.page.locator(".panel-body > div > div:nth-child(2) > .form-control").first.select_option("01:00 AM")
        self.page.locator(".col-lg-12 > .form-control").first.select_option("378")
        self.page.locator("div:nth-child(3) > .col-lg-12 > .form-control").first.select_option("708")
        self.page.locator(".col-lg-6 > .input-group > .form-control").first.click()
        self.page.locator(".col-lg-6 > .input-group > .form-control").first.fill("10/08/2023")
        self.page.locator("div:nth-child(4) > div:nth-child(2) > .form-control").first.click()
        self.page.locator("div:nth-child(4) > div:nth-child(2) > .form-control").first.fill("10/14/2023")
        self.page.locator("div:nth-child(4) > div:nth-child(2) > .form-control").first.click()
        self.page.get_by_role("cell", name="Start Date End Date  Copy").locator("a").click()
        self.page.get_by_role("cell", name="Start Date End Date  Paste").locator("a").click()
        self.page.get_by_role("cell", name="Start Date End Date  Paste").locator("a").click()
        self.page.get_by_role("cell", name="Start Date End Date  Paste").locator("a").click()
        self.page.get_by_role("cell", name="Start Date End Date  Paste").locator("a").click()
        self.page.get_by_role("cell", name="Start Date End Date  Paste").locator("a").click()
        self.page.get_by_role("cell", name="Start Date End Date  Paste").locator("a").click()
        self.page.get_by_role("button", name="ADD WEEKLY SCHEDULE").click()
        self.page.get_by_role("button", name="Cancel").click()
        self.page.get_by_role("tab", name="Authorizations").click()
        self.page.get_by_role("tab", name="Schedule", exact=True).click()
