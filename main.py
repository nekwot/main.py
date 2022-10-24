#pip install PyQt5
#pip install pyodbc
import pyodbc
from datetime import datetime, timedelta
from form import *
import sys

#server = 'tcp:myserver.database.windows.net'
#database = 'mydb'
#username = 'myusername'
#password = 'mypassword'
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#cursor = cnxn.cursor()

#пример запроса
#cursor.execute('SELECT ID, BarCode, DateTm, EntryDoor FROM dbo.tab_Rolls WHERE (DateTm >= @startDate) AND (DateTm <= @endDate)')

#Выполнение запроса
#Функция cursor.execute может использоваться для извлечения результирующего набора из запроса
#базе данных SQL. Эта функция принимает запрос и возвращает результирующий набор, по которому
#может быть выполнена итерация с использованием cursor.fetchone().

#cursor.execute("SELECT @@version;")
#row = cursor.fetchone()
#while row:
#    print(row[0])
#    row = cursor.fetchone()


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

DD = datetime.now() + timedelta(days=-6) #отнимает 6 дней
ui.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
ui.dateEdit.setDateTime(DD)

def on_click():


    print("clicked!!!")

ui.buttonBox.clicked.connect(on_click)


sys.exit(app.exec_())

