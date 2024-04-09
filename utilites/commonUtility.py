import sqlite3
import pandas
from jproperties import Properties

def readValue(key):
    configs = Properties()
    with open('../resources/config.properties', 'rb') as config_file:
        configs.load(config_file)
    print(configs.get(key).data)
    return configs.get(key).data

def convertExcelIntoDatabase(excelFile):
    try:
        db = sqlite3.connect('sqlite.db')
        dfs = pd.read_excel(excelFile, engine='openpyxl', sheet_name=None)
        for workflow, df in dfs.items():
            df.to_sql(workflow, db, if_exists='replace')
            print(f'{df} inserted successfully')
        return db
    except Exception as e:
        print("Error")

def releaseDbConnection(db):
    try:
        db.close()
        print("dataconnection closed")
    except:
        print("Error while closing file")

def getData(fName, arg):
    try:
        db=convertExcelIntoDatabase('../resources/dataSheet.xlsx')
        cursor = db.cursor()
        cursor.execute(f'SELECT {arg} from Workflow WHERE FunctionName = ?',(fName,))
        for row in cursor:
            return str(row[0])
        releaseDbConnection(db)
    except:
        print("Error while fetching actiontype")