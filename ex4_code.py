
# coding: utf-8

import sqlite3
from reportlab.pdfgen import canvas

conn = sqlite3.connect('C:/Users/User/Desktop/FIS/Exercise3/database.db')
cur = conn.cursor()
period1 = input('Parakalw dwste enakthria hmeromhnia:(DD/MM/YYYY)')
period2 = input('Parakalw dwste telikh hmeromhnia:(DD/MM/YYYY)')
cust_id = input('Select id to return info:')
args = (cust_id)
cur.execute("SELECT field1, field3, CAST(field5 AS INT), field2 FROM Sample_Trans3 WHERE field4= ? AND field1 BETWEEN ? AND ?" , (cust_id,period1,period2,))
list1 = cur.fetchall()
list1

c = canvas.Canvas("customer_"+cust_id+".pdf")
c.setFont('Helvetica', 18)
c.drawString(250,800,"West Ham United Bank")
c.setFont('Helvetica', 12)
c.drawImage('west_ham.png', 25, 665, width=None, height=None, mask=None, preserveAspectRatio=True, anchor='c')
c.drawString(25,645,"Customer Id:")
c.drawString(105,645,cust_id)
c.setFont('Helvetica', 15)
c.drawString(400,730,"Statement Period")
c.setFont('Helvetica', 10)
c.drawString(400,720,period1)
c.drawString(458,720,'--')
c.drawString(470,720,period2)
c.setFont('Helvetica', 13)
c.drawString(20,620,"DATE")
c.drawString(75,620,"TRANSACTIONS")
c.drawString(220,620,"AMOUNT")
c.drawString(340,620,"BALANCE")
c.setFont('Helvetica', 9)
r1 = 610
rp = 10
balance = int(cust_id)%997
print(balance)
for row in list1:
    r1 = r1 - 10
    if r1 == 20:
        c.showPage()
        r1 = 800
        if row[3] == '1' and row[1] != 'CHEQUE DEPOSIT':
            c.setFont('Helvetica', 9)
            c.drawString(350,r1,str(balance + row[2]))
        elif row[3] == '-1' and row[1] != 'CHEQUE PAYMENT':
            c.setFont('Helvetica', 9)
            c.drawString(350,r1,str(balance - row[2]))
        else:
            c.setFont('Helvetica', 9)
            c.drawString(350,r1,str(balance))
        c.setFont('Helvetica', 9)
        c.drawString(20,r1,row[0])
        c.drawString(80,r1,row[1])
        c.drawString(230,r1,str(row[2]))        
    else:
        if row[3] == '1' and row[1] != 'CHEQUE DEPOSIT':
            c.setFont('Helvetica', 9)
            c.drawString(350,r1,str(balance + row[2]))
        elif row[3] == '-1' and row[1] != 'CHEQUE PAYMENT':
            c.setFont('Helvetica', 9)
            c.drawString(350,r1,str(balance - row[2]))
        else:
            c.setFont('Helvetica', 9)
            c.drawString(350,r1,str(balance))
        c.setFont('Helvetica', 9)
        c.drawString(20,r1,row[0])
        c.drawString(80,r1,row[1])
        c.drawString(230,r1,str(row[2])) 
c.save()




