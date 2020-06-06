import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

from flask import Flask, render_template, url_for, flash, redirect, request
app = Flask(__name__)


@app.route("/", methods =['GET','POST'])
@app.route("/home", methods=['GET','POST']) 
def homepage():
    if request.method == 'GET':
        return render_template('homepage.html')
    elif request.method == 'POST':
        if request.form['Yo'] == 'Overall Attendance':
            return redirect(url_for('inputpage'))
        elif request.form['Yo'] == 'Student Attendance':
            return redirect(url_for('studentpage'))
        elif request.form['Yo'] == 'Predictions':
            return redirect(url_for('inputpage'))

@app.route("/student", methods = ['GET','POST'])
def studentpage():
    if request.method == 'GET':
        return render_template('studentpage.html' )

    elif request.method == 'POST':
        Subject = request.form.get("Subject")
        Roll_No = request.form.get("Roll_No")
        Month = request.form.get("Month")
        Day = request.form.get("Day")
        Roll_No = int(Roll_No)
        Present_days = 0
        Absent_days = 0

        if Subject == 'COA':
            file = pd.read_csv(r'C:\Users\user\Downloads\COA.csv',skiprows=1)
        elif Subject == 'MP':
            file = pd.read_csv(r'C:\Users\user\Downloads\MP.csv',skiprows=1)
        elif Subject == 'CG':
            file = pd.read_csv(r'C:\Users\user\Downloads\CG.csv',skiprows=1)
        elif Subject == 'ADS':
            file = pd.read_csv(r'C:\Users\user\Downloads\ADS.csv',skiprows=1)
        elif Subject == 'PPL':
            file = pd.read_csv(r'C:\Users\user\Downloads\PPL.csv',skiprows=1)
        elif Subject == 'All Subjects':
            file1 = pd.read_csv(r'C:\Users\user\Downloads\COA.csv',skiprows=1)
            file2 = pd.read_csv(r'C:\Users\user\Downloads\MP.csv',skiprows=1)
            file3 = pd.read_csv(r'C:\Users\user\Downloads\CG.csv',skiprows=1)
            file4 = pd.read_csv(r'C:\Users\user\Downloads\ADS.csv',skiprows=1)
            file5 = pd.read_csv(r'C:\Users\user\Downloads\PPL.csv',skiprows=1)

            Present_days1 = 0
            Present_days2 = 0
            Present_days3 = 0
            Present_days4 = 0
            Present_days5 = 0

            data1 = file1[1:]
            data2 = file2[1:]
            data3 = file3[1:]
            data4 = file4[1:]
            data5 = file5[1:]

            if Month == 'All Months':

                for i in data1.iloc[Roll_No,3:]:
                    if i == 'P':
                        Present_days1+=1

                for i in data2.iloc[Roll_No,3:]:
                    if i == 'P':
                        Present_days2+=1

                for i in data3.iloc[Roll_No,3:]:
                    if i == 'P':
                        Present_days3+=1

                for i in data4.iloc[Roll_No,3:]:
                    if i == 'P':
                        Present_days4+=1

                for i in data5.iloc[Roll_No,3:]:
                    if i == 'P':
                        Present_days5+=1
            
                plt.bar(['COA','MP','CG','ADS','PPL'],[Present_days1,Present_days2,Present_days3,Present_days4,Present_days5])
                plt.title("Bar graph")
                plt.ylabel("Attendance count")
                plt.xlabel("Subjects")
                plt.savefig('static/'+str(Roll_No)+'_'+Subject+'_'+Month+'_'+str(Day)+'_bar.jpg')
                plt.close()   

            else:
                if Day == 'All Days':
                    Particular_Month=[]
                    for i in data1.columns:
                        if i.endswith(Month):
                            Particular_Month.append(i)

                    for i in data1[Particular_Month].iloc[Roll_No]:
                        if i == 'P':
                            Present_days1+=1
                    for i in data2[Particular_Month].iloc[Roll_No]:
                        if i == 'P':
                            Present_days2+=1
                    for i in data3[Particular_Month].iloc[Roll_No]:
                        if i == 'P':
                            Present_days3+=1
                    for i in data4[Particular_Month].iloc[Roll_No]:
                        if i == 'P':
                            Present_days4+=1
                    for i in data5[Particular_Month].iloc[Roll_No]:
                        if i == 'P':
                            Present_days5+=1

                    plt.bar(['COA','MP','CG','ADS','PPL'], [Present_days1,Present_days2,Present_days3,Present_days4,Present_days5])
                    plt.title("Month wise Graph")
                    plt.xlabel("Subjects")
                    plt.ylabel("Count")
                    plt.savefig('static/'+str(Roll_No)+'_'+Subject+'_'+Month+'_'+str(Day)+'_bar.jpg')
                    plt.close()

                else:
                    Particular_Day=[]
                    for i in data1.columns:
                        if i.startswith(Day) and i.endswith(Month):
                            Particular_Day.append(i)

                    for i in data1[Particular_Day].iloc[Roll_No]:
                        if i == 'P':
                            Present_days1+=1
                    for i in data2[Particular_Day].iloc[Roll_No]:
                        if i == 'P':
                            Present_days2+=1
                    for i in data3[Particular_Day].iloc[Roll_No]:
                        if i == 'P':
                            Present_days3+=1
                    for i in data4[Particular_Day].iloc[Roll_No]:
                        if i == 'P':
                            Present_days4+=1
                    for i in data5[Particular_Day].iloc[Roll_No]:
                        if i == 'P':
                            Present_days5+=1

                    plt.bar(['COA','MP','CG','ADS','PPL'], [Present_days1,Present_days2,Present_days3,Present_days4,Present_days5])
                    plt.title("Particular Day Graph")
                    plt.xlabel("Subjects")
                    plt.ylabel("Count")
                    plt.savefig('static/'+str(Roll_No)+'_'+Subject+'_'+Month+'_'+str(Day)+'_bar.jpg')
                    plt.close()
            return render_template('outputpage.html',back = 'studentpage', link1 ='static/'+str(Roll_No)+'_'+Subject+'_'+Month+'_'+str(Day)+'_bar.jpg',
                                link2 = 'static/'+str(Roll_No)+'_'+Subject+'_'+Month+'_'+str(Day)+'_plot.jpg')

        data = file[1:]
        if Month == 'All Months':

            for i in data.iloc[Roll_No,3:]:
                if i == 'P':
                    Present_days+=1
                else:
                    Absent_days+=1           

            plt.plot(data.iloc[Roll_No,3:],linestyle='dashed',marker='o')
            plt.xticks([])
            plt.title("Line graph")
            plt.ylabel("Attendance status")
            plt.xlabel("All Days")
            plt.savefig('static/'+str(Roll_No)+'_'+Subject+'_'+Month+'_'+str(Day)+'_bar.jpg')
            plt.close()
            
            plt.bar(['Present Days','Absent Days'],[Present_days,Absent_days])
            plt.title("Bar graph")
            plt.ylabel("Number of Days")
            plt.xlabel("Status")
            plt.savefig('static/'+str(Roll_No)+'_'+Subject+'_'+Month+'_'+str(Day)+'_plot.jpg')
            plt.close()

        else:
            if Day == 'All Days':
                Particular_Month=[]
                for i in data.columns:
                    if i.endswith(Month):
                        Particular_Month.append(i)

                for i in data[Particular_Month].iloc[Roll_No]:
                    if i == 'P':
                        Present_days+=1
                    else:
                        Absent_days+=1

                plt.plot(Particular_Month,data[Particular_Month].iloc[Roll_No], linestyle = 'dashed',marker='o')
                plt.title("Month wise Graph")
                plt.xlabel("Date")
                plt.ylabel("Status")
                plt.savefig('static/'+str(Roll_No)+'_'+Subject+'_'+Month+'_'+str(Day)+'_plot.jpg')
                plt.close()

                plt.bar(['Present Days','Absent Days'], [Present_days,Absent_days])
                plt.title("Month wise Graph")
                plt.xlabel("Status")
                plt.ylabel("Count")
                plt.savefig('static/'+str(Roll_No)+'_'+Subject+'_'+Month+'_'+str(Day)+'_bar.jpg')
                plt.close()

            else:
                Particular_Day=[]
                for i in data.columns:
                    if i.startswith(Day) and i.endswith(Month):
                        Particular_Day.append(i)

                for i in data[Particular_Day].iloc[Roll_No]:
                    if i == 'P':
                        Present_days+=1
                    else:
                        Absent_days+=1

                plt.bar(['Present','Absent'], [Present_days,Absent_days])
                plt.title("Particular Day Graph")
                plt.xlabel("Status")
                plt.ylabel("Count")
                plt.savefig('static/'+str(Roll_No)+'_'+Subject+'_'+Month+'_'+str(Day)+'_bar.jpg')
                plt.close()

        return render_template('outputpage.html',back = 'studentpage', link1 ='static/'+str(Roll_No)+'_'+Subject+'_'+Month+'_'+str(Day)+'_bar.jpg',
                                link2 = 'static/'+str(Roll_No)+'_'+Subject+'_'+Month+'_'+str(Day)+'_plot.jpg')


@app.route("/overall", methods = ['GET','POST'])
def inputpage():
    if request.method == 'GET':
        return render_template('inputpage.html' )

    elif request.method == 'POST':
        Subject = request.form.get("Subject")
        Type = request.form.get("Type")

        if Subject == 'COA':
            file = pd.read_csv(r'C:\Users\user\Downloads\COA.csv',skiprows=1)
        elif Subject == 'MP':
            file = pd.read_csv(r'C:\Users\user\Downloads\MP.csv',skiprows=1)
        elif Subject == 'CG':
            file = pd.read_csv(r'C:\Users\user\Downloads\CG.csv',skiprows=1)
        elif Subject == 'ADS':
            file = pd.read_csv(r'C:\Users\user\Downloads\ADS.csv',skiprows=1)
        elif Subject == 'PPL':
            file = pd.read_csv(r'C:\Users\user\Downloads\PPL.csv',skiprows=1)
        elif Subject == 'All Subjects':
            file1 = pd.read_csv(r'C:\Users\user\Downloads\COA.csv',skiprows=1)
            file2 = pd.read_csv(r'C:\Users\user\Downloads\MP.csv',skiprows=1)
            file3 = pd.read_csv(r'C:\Users\user\Downloads\CG.csv',skiprows=1)
            file4 = pd.read_csv(r'C:\Users\user\Downloads\ADS.csv',skiprows=1)
            file5 = pd.read_csv(r'C:\Users\user\Downloads\PPL.csv',skiprows=1)

            data1 = file1[1:]
            data2 = file2[1:]
            data3 = file3[1:]
            data4 = file4[1:]
            data5 = file5[1:]
            columns1 = data1.columns.tolist()
            Absent_days1 = data1['Days Absent']
            Absent_days1 = [round(x) for x in Absent_days1]
            Absent_days2 = data2['Days Absent']
            Absent_days2 = [round(x) for x in Absent_days2]
            Absent_days3 = data3['Days Absent']
            Absent_days3 = [round(x) for x in Absent_days3]
            Absent_days4 = data4['Days Absent']
            Absent_days4 = [round(x) for x in Absent_days4]
            Absent_days5 = data5['Days Absent']
            Absent_days5 = [round(x) for x in Absent_days5]
            
            
            Total_days = len(columns1)-3
            Present_days1 = [Total_days-x for x in Absent_days1]
            Present_days2 = [Total_days-x for x in Absent_days2]
            Present_days3 = [Total_days-x for x in Absent_days3]
            Present_days4 = [Total_days-x for x in Absent_days4]
            Present_days5 = [Total_days-x for x in Absent_days5]

            Absent_percentage1 = [100*x/Total_days for x in Absent_days1]
            Absent_percentage2 = [100*x/Total_days for x in Absent_days2]
            Absent_percentage3 = [300*x/Total_days for x in Absent_days3]
            Absent_percentage4 = [100*x/Total_days for x in Absent_days4]
            Absent_percentage5 = [100*x/Total_days for x in Absent_days5]

            Present_percentage1 = [100-x for x in Absent_percentage1]
            Present_percentage2 = [100-x for x in Absent_percentage2]
            Present_percentage3 = [100-x for x in Absent_percentage3]
            Present_percentage4 = [100-x for x in Absent_percentage4]
            Present_percentage5 = [100-x for x in Absent_percentage5]

            if Type == 'Absent_Days':
                plt.bar(['COA','MP','CG','ADS','PPL'], [sum(Absent_days1),sum(Absent_days2),sum(Absent_days3),sum(Absent_days4),sum(Absent_days5)])
                plt.title("Bar graph")
                plt.xlabel("Subjects")
                plt.ylabel("Days Absent")
                plt.savefig('static/'+Subject+'_'+Type+'_bar.jpg')
                plt.close()

                plt.plot(['COA','MP','CG','ADS','PPL'], [sum(Absent_days1),sum(Absent_days2),sum(Absent_days3),sum(Absent_days4),sum(Absent_days5)], linestyle='dashed',marker='o')
                plt.title("Line graph")
                plt.xlabel("Subjects")
                plt.ylabel("Days Absent")
                plt.savefig('static/'+Subject+'_'+Type+'_plot.jpg')
                plt.close()

            elif Type == 'Present_Days':
                plt.bar(['COA','MP','CG','ADS','PPL'], [sum(Present_days1),sum(Present_days2),sum(Present_days3),sum(Present_days4),sum(Present_days5)])
                plt.title("Bar graph")
                plt.xlabel("Subjects")
                plt.ylabel("Days Present")
                plt.savefig('static/'+Subject+'_'+Type+'_bar.jpg')
                plt.close()

                plt.plot(['COA','MP','CG','ADS','PPL'], [sum(Present_days1),sum(Present_days2),sum(Present_days3),sum(Present_days4),sum(Present_days5)], linestyle='dashed',marker='o')
                plt.title("Line graph")
                plt.xlabel("Subjects")
                plt.ylabel("Days Present")
                plt.savefig('static/'+Subject+'_'+Type+'_plot.jpg')
                plt.close()

            elif Type == 'Present_Percentage':
                plt.bar(['COA','MP','CG','ADS','PPL'], [statistics.mean(Present_percentage1),statistics.mean(Present_percentage2),statistics.mean(Present_percentage3),statistics.mean(Present_percentage4),statistics.mean(Present_percentage5)])
                plt.title("Bar graph")
                plt.xlabel("Subjects")
                plt.ylabel("Present %")
                plt.savefig('static/'+Subject+'_'+Type+'_bar.jpg')
                plt.close()

                plt.plot(['COA','MP','CG','ADS','PPL'], [statistics.mean(Present_percentage1),statistics.mean(Present_percentage2),statistics.mean(Present_percentage3),statistics.mean(Present_percentage4),statistics.mean(Present_percentage5)], linestyle='dashed',marker='o')
                plt.title("Line graph")
                plt.xlabel("Subjects")
                plt.ylabel("Present %")
                plt.savefig('static/'+Subject+'_'+Type+'_plot.jpg')
                plt.close() 
                
            elif Type == 'Absent_Percentage':
                plt.bar(['COA','MP','CG','ADS','PPL'], [statistics.mean(Absent_percentage1),statistics.mean(Absent_percentage2),statistics.mean(Present_percentage3),statistics.mean(Present_percentage4),statistics.mean(Present_percentage5)])
                plt.title("Bar graph")
                plt.xlabel("Subjects")
                plt.ylabel("Absent %")
                plt.savefig('static/'+Subject+'_'+Type+'_bar.jpg')
                plt.close()

                plt.plot(['COA','MP','CG','ADS','PPL'], [statistics.mean(Absent_percentage1),statistics.mean(Absent_percentage2),statistics.mean(Present_percentage3),statistics.mean(Present_percentage4),statistics.mean(Present_percentage5)], linestyle='dashed',marker='o')
                plt.title("Line graph")
                plt.xlabel("Subjects")
                plt.ylabel("Absent %")
                plt.savefig('static/'+Subject+'_'+Type+'_plot.jpg')
                plt.close()

            return render_template('outputpage.html', link1='static/'+Subject+'_'+Type+'_plot.jpg',link2='static/'+Subject+'_'+Type+'_bar.jpg',
                                link3='static/'+Subject+'_'+Type+'_pie.jpg', back = 'inputpage')
        
        data = file[1:]
        columns = data.columns.tolist()
        Absent_days = data['Days Absent']
        Roll_No = data['Student Roll No.']
        Absent_days = [round(x) for x in Absent_days]
        Roll_No = [round(x) for x in Roll_No]
        Total_days = len(columns)-3
        Present_days = [Total_days-x for x in Absent_days]
        Absent_percentage = [100*x/Total_days for x in Absent_days]
        Present_percentage = [100-x for x in Absent_percentage]

        if Type == 'Absent_Days':
            plt.bar(Roll_No, Absent_days)
            plt.title("Bar graph")
            plt.xlabel("Roll No")
            plt.ylabel("Days Absent")
            plt.savefig('static/'+Subject+'_'+Type+'_bar.jpg')
            plt.close()

            plt.plot(Roll_No, Absent_days, linestyle='dashed',marker='o')
            plt.title("Line graph")
            plt.xlabel("Roll No")
            plt.ylabel("Days Absent")
            plt.savefig('static/'+Subject+'_'+Type+'_plot.jpg')
            plt.close()

        elif Type == 'Present_Days':
            plt.bar(Roll_No, Present_days)
            plt.title("Bar graph")
            plt.xlabel("Roll No")
            plt.ylabel("Days Present")
            plt.savefig('static/'+Subject+'_'+Type+'_bar.jpg')
            plt.close()

            plt.plot(Roll_No, Present_days, linestyle='dashed',marker='o')
            plt.title("Line graph")
            plt.xlabel("Roll No")
            plt.ylabel("Days Present")
            plt.savefig('static/'+Subject+'_'+Type+'_plot.jpg')
            plt.close()

        elif Type == 'Present_Percentage':
            plt.bar(Roll_No, Present_percentage)
            plt.title("Bar graph")
            plt.xlabel("Roll No")
            plt.ylabel("Present %")
            plt.savefig('static/'+Subject+'_'+Type+'_bar.jpg')
            plt.close()

            plt.plot(Roll_No, Present_percentage, linestyle='dashed',marker='o')
            plt.title("Line graph")
            plt.xlabel("Roll No")
            plt.ylabel("Present %")
            plt.savefig('static/'+Subject+'_'+Type+'_plot.jpg')
            plt.close() 
            
        elif Type == 'Absent_Percentage':
            plt.bar(Roll_No, Absent_percentage)
            plt.title("Bar graph")
            plt.xlabel("Roll No")
            plt.ylabel("Absent %")
            plt.savefig('static/'+Subject+'_'+Type+'_bar.jpg')
            plt.close()

            plt.plot(Roll_No, Absent_percentage, linestyle='dashed',marker='o')
            plt.title("Line graph")
            plt.xlabel("Roll No")
            plt.ylabel("Absent %")
            plt.savefig('static/'+Subject+'_'+Type+'_plot.jpg')
            plt.close()

        return render_template('outputpage.html', link1='static/'+Subject+'_'+Type+'_plot.jpg',link2='static/'+Subject+'_'+Type+'_bar.jpg',
                            link3='static/'+Subject+'_'+Type+'_pie.jpg', back = 'inputpage')

if __name__ == '__main__':
   app.run()