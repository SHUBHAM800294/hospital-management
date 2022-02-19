from cProfile import label
from logging import root
from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="+HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",40,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #*****************Dataframe***********************
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=110,width=1022,height=400)


        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                    font=("arial",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=650,height=350)   

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                    font=("arial",12,"bold"),text="Prescription")
        DataframeRight.place(x=650,y=5,width=330,height=350) 

            #*********************Button frames*****************


        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=510,width=1022,height=70)


        #*********************Details frames*****************


        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=575,width=1025,height=140)

        #*********************DataFrameLeft*****************

        lblNameTablet=Label(DataframeLeft,text="Name of Tablet",font=("times new roman",11,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",font=("times new roman",10,"bold"),
                                                                                 width=20)
        
        comNametablet["values"]=("Nice","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",11,"bold"),text="Refrence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.ref,width=20)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",11,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.Dose,width=20)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("arial",11,"bold"),text="No of Tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.NumberofTablets,width=20)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("arial",11,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.Lot,width=20)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,font=("arial",11,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.Issuedate,width=20)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("arial",11,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.ExpDate,width=20)
        txtExpDate.grid(row=6,column=1)


        lblDailyDose=Label(DataframeLeft,font=("arial",11,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.DailyDose, width=20)
        txtDailyDose.grid(row=7,column=1)


        lblSideEffect=Label(DataframeLeft,font=("arial",11,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.sideEffect, width=20)
        txtSideEffect.grid(row=8,column=1)


        lblFurtherinfo=Label(DataframeLeft,font=("arial",11,"bold"),text="Further Information:",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.FurtherInformation,width=20)
        txtFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",11,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.DrivingUsingMachine,width=20)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("arial",11,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.StorageAdvice, width=20)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",11,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.HowToUseMedication,width=20)
        txtMedicine.grid(row=3,column=3,sticky=W)

        lblPatientId=Label(DataframeLeft,font=("arial",11,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.PatientId, width=20)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,font=("arial",11,"bold"),text="NHS Number :",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.nhsNumber, width=20)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label(DataframeLeft,font=("arial",11,"bold"),text=" Patient Name:",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.PatientName, width=20)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframeLeft,font=("arial",11,"bold"),text=" Date Of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.DateOfBirth, width=20)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("arial",11,"bold"),text=" Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.PatientAddress,width=20)
        txtPatientAddress.grid(row=8,column=3)


        #**************************DataFrameRight************************

        self.txtPrescription=Text(DataframeRight,font=("arial",11,"bold"),width=37,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #**********************Buttons**********************

        btnPrescription=Button(Buttonframe,text="Presciption",bg="green",fg="white",font=("arial",11,"bold"),width=17,padx=2,pady=10)
        btnPrescription.grid(row=0,column=0)

        
        btnPrescriptionData=Button(Buttonframe,text="Presciption Data",bg="green",fg="white",font=("arial",11,"bold"),width=17,padx=2,pady=10)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",11,"bold"),width=17,padx=2,pady=10)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",11,"bold"),width=17,padx=2,pady=10)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",11,"bold"),width=17,padx=2,pady=10)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",11,"bold"),width=17,padx=2,pady=10)
        btnExit.grid(row=0,column=5)

        #***********************Table******************************
        #************************scrollBar*************************


        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
       
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Daily Dose")
        self.hospital_table.heading("dailydose",text="Storage")
        self.hospital_table.heading("storage",text="NHS Number")
        self.hospital_table.heading("nhsnumber",text="Patient Name")
        self.hospital_table.heading("pname",text="DOB")
        self.hospital_table.heading("dob",text="Address")
        self.hospital_table.heading("address",text="Exp Date")

        self.hospital_table["show"]="headings"


        self.hospital_table.column("nameoftable",width=70)
        self.hospital_table.column("ref",width=70)
        self.hospital_table.column("dose",width=70)
        self.hospital_table.column("nooftablets",width=70)
        self.hospital_table.column("lot",width=70)
        self.hospital_table.column("issuedate",width=70)
        self.hospital_table.column("expdate",width=70)
        self.hospital_table.column("dailydose",width=70)
        self.hospital_table.column("storage",width=70)
        self.hospital_table.column("nhsnumber",width=70)
        self.hospital_table.column("pname",width=70)
        self.hospital_table.column("dob",width=70)
        self.hospital_table.column("address",width=70)

      
        self.hospital_table.pack(fill=BOTH,expand=1)


        #========================= Functinality Declaration =========================
        def iPrescriptionData(self):
            if self.Nameoftablets.get()=="" or self.ref.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="shubh988",database="Mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)",(

                                                                                                   self.Nameoftablets.get(),
                                                                                                   self.ref.get(),
                                                                                                   self.Dose.get(),
                                                                                                   self.NumberofTablets.get(),
                                                                                                   self.Lot.get(),
                                                                                                   self.Issuedate.get(),
                                                                                                   self.ExpDate.get(),                                                                                                   
                                                                                                   self.DailyDose.get(),
                                                                                                   self.StorageAdvise.get(),
                                                                                                   self.nhsNumber.get(),
                                                                                                   self.PatientName.get(),
                                                                                                   self.DateOfBirth.get(),
                                                                                                   self.PatientAddress.get(),

                
                                                                                                   ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Record has been inserted")




        








root=Tk()
ob=Hospital(root)
root.mainloop()        