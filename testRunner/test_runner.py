import pytest
from playwright.sync_api import sync_playwright
from pages.loginPage.LoginLogout import LoginLogout as lgt
from pages.clientPage.searchClient import searchClient as sc
from pages.clientPage.status import status as st
from pages.clientPage.personalInfo import  PersonalInfo as pi
from pages.clientPage.emergencyInfo import EmergencyInfo as ei
from pages.clientPage.meddaigonis import  MedDaigonis as md
from pages.clientPage.planOfCare import PlanOfCare as poc
from pages.clientPage.billingDetails import BillingDetails as bd
from pages.clientPage.authorization import Authorization as auth
from pages.clientPage.contactLog import ContactLog as cn
from pages.clientPage.compilance import Compilance as cp
from pages.clientPage.emrRecords import  EMRRecords as er
from pages.clientPage.groupInfo import GroupInfo as gi
from utilites import commonUtility
from pages.clientPage.schedule import Schedule as sch
from pages.employeePage.createEmployee import createEmoloyee as ce
from pages.employeePage.status import Status as statusEmp
from pages.employeePage.availability import Availability as ava
from pages.employeePage.rate import Rate as rate
from pages.employeePage.incidents import Incidents as inc
from pages.employeePage.compilance import Compilance as comp
from pages.employeePage.documents import Documents as doc
from pages.employeePage.hr import FillHr as hr

from pages.createInvoice.addInvoice import AddInvoice as createInvo
from pages.InvoiceList.invoiceListActions import InvoiceList as invoAction

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        yield browser
        browser.close()

@pytest.fixture(scope="module")
def record (browser):
    context = browser.new_context(record_video_dir="../output/", record_video_size={"width": 1920, "height": 1080})
    yield context
    context.close()

@pytest.fixture(scope="module")
def page(record):
    page = record.new_page()
    page.set_viewport_size({'width': 1024, 'height': 600})
    page.goto(commonUtility.readValue('URL'))
    yield page
    page.close()

@pytest.fixture(scope="module")
def loginPage(page):
    return lgt(page)


@pytest.fixture(scope="module")
def searchClient(page):
    return sc(page)

@pytest.fixture(scope="module")
def status(page):
    return st(page)

@pytest.fixture(scope="module")
def personalInfo(page):
    return pi(page)

@pytest.fixture(scope="module")
def emergencyInfo(page):
    return ei(page)

@pytest.fixture(scope="module")
def medication_daigonis(page):
    return md(page)

@pytest.fixture(scope="module")
def planOfCare(page):
    return poc(page)

@pytest.fixture(scope="module")
def billingDetails(page):
    return bd(page)

@pytest.fixture(scope="module")
def authorization(page):
    return auth(page)

@pytest.fixture(scope="module")
def contactNotes(page):
    return cn(page)


@pytest.fixture(scope="module")
def emrRecords(page):
    return er(page)

@pytest.fixture(scope="module")
def groupInfo(page):
    return gi(page)

@pytest.fixture(scope="module")
def schedule(page):
    return sch(page)

def test_login(loginPage):
    loginPage.login()

# @pytest.fixture
# def test_createNewClient(personalInfo):
#     clientId=personalInfo.CreateEditPersonalInfo()
#     return clientId
#
# def test_searchClient(searchClient,test_createNewClient):
#     client_id = test_createNewClient
#     searchClient.searchClientInClientList(client_id)

def test_searchClient(searchClient):
     searchClient.searchClientInClientList('852')

# def test_clientStatus(status):
#     status.clientStatus()
#     status.editStatus()
#
# def test_emergencyInfo(emergencyInfo):
#     emergencyInfo.fillPrimaryContact()
#     emergencyInfo.fillSecondaryContact()
#     emergencyInfo.addPayer()
#     emergencyInfo.editPayer()
#
# def test_Medication(medication_daigonis):
#     medication_daigonis.createMedication()
#     medication_daigonis.createDaigonis()
#
# def test_planOfCare(planOfCare):
#     planOfCare.createPOC()
#     #planOfCare.addAccomdation()
#
#
# def test_BillingDetails(billingDetails):
#     billingDetails.enterBilling()
#
#
# def test_Authorization(authorization):
#     authorization.createAuthorization()
#
#
# def test_contactNotes(contactNotes):
#     contactNotes.addContactLog()
#     contactNotes.addNotes()
#
# @pytest.fixture(scope="module")
# def clientCompilance(page):
#     return cp(page)
#
# def test_clientCompilance(clientCompilance):
#     clientCompilance.addCompilance()
#
# def test_emrRecords(emrRecords):
#     emrRecords.createFolder()
#     emrRecords.uploadFile()
#
#
# def test_groupInfo(groupInfo):
#     groupInfo.addGroup()

def test_createScheduleAndSignInSignOut(schedule):
    date='12/03/2023'
    schedule.createDaySchedule(date)
    schedule.doSignIn(date)
    schedule.doSignOut(date)

# def test_CreateWeeklyScheduleAndSignInSignOut(schedule):
#     date = '10/11/2023'
#     schedule.createWeeklySchedule()
#     schedule.doSignIn(date)
#     schedule.doSignOut(date)


####################################Employee TestCases################################
#
# @pytest.fixture(scope="module")
# def createEmoloyee(page):
#     return ce(page)
#
# def test_createEmployee(createEmoloyee):
#     createEmoloyee.createEmply()
#
# @pytest.fixture(scope="module")
# def fillHr(page):
#     return hr(page)
#
# def test_fillHrDetails(fillHr):
#     fillHr.fillPayroll()
#     fillHr.fillDirectDeposit()
# #     #fillHr.fillProfessionalInfo()
#
# @pytest.fixture(scope="module")
# def empStatus(page):
#     return statusEmp(page)
#
# def test_addStatus(empStatus):
#     empStatus.addStatus()
#
# @pytest.fixture(scope="module")
# def availability(page):
#     return ava(page)
#
# def test_availability(availability):
#     availability.addPreference()
#     availability.addAvailbility()
#
# @pytest.fixture(scope="module")
# def rates(page):
#     return rate(page)
#
# def test_addRates(rates):
#     rates.addRate()
#
# @pytest.fixture(scope="module")
# def incidents(page):
#     return inc(page)
#
# def test_incidents(incidents):
#     incidents.addIncidents()
#     incidents.addNotes()
#
# @pytest.fixture(scope="module")
# def employeeCompilance(page):
#     return comp(page)
#
# def test_mployeeCompilance(employeeCompilance):
#     employeeCompilance.addCompilance()
#     employeeCompilance.editCompilance()
#
# @pytest.fixture(scope="module")
# def documents(page):
#     return doc(page)
#
# def test_documents(documents):
#     documents.uploadDocument()

###################################Create Invoice ######################################
@pytest.fixture(scope="module")
def createInvoice(page):
    return createInvo(page)

def test_createInvoice(createInvoice):
    fromDate='12/03/2023'
    toDate='12/04/2023'
    createInvoice.addInvoice(fromDate,toDate)

@pytest.fixture(scope="module")
def invoiceAction(page):
    return invoAction(page)

def test_invoiceListAction(invoiceAction):
    fromDate='12/03/2023'
    toDate='12/04/2023'
    invoiceAction.invoiceListActions(fromDate,toDate)
