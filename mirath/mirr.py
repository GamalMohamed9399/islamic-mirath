'''
group 16   -   مشروع المواريث 

جمال محمد السيد عطية : 37
السيد عبدالعزيز حمدان زويد :29
حسام شاكر توفيق كسبر  رقم:39

'''


from tkinter import *
from fractions import Fraction as f

from tkinter.ttk import Combobox



class Super:
    def __init__(self, root):
        self.root = root
        self.root.title('Mirath')
        self.root.resizable(False, False)
        self.root.geometry('1400x1000+100+0')
        title = Label(root, text='الميراث الاسلامي', fg='black', bg='#e6e4c7', font=('tajawal', 30, 'bold'))
        title.pack(fill=X)
        self.amount = IntVar()
        amount = Label(root,text='التركه', fg='black', bg='#e6e4c7', font=('tajawal', 20, 'bold'))
        amount.place(x=550, y=60, height=40, width=100)
        entry_amount = Entry(root,font=('tajawal', 16, 'bold'),textvariable=self.amount)
        entry_amount.place(x=340, y=60, height=40, width=200)

        # INPUT FRAME
        f1=Frame(root, bd=2, width=850, height=650, bg='#e6e4c7')
        f1.place(x=50, y=120)

        # OUTPUT FRAME
        f2=Frame(root, bd=2, width=350, height=650)
        f2.place(x=900, y=120)
        scroll = Scrollbar(f2,orient=VERTICAL)
        self.textarea = Text(f2,height=25,width=45,bg='#e6e4c7',yscrollcommand=scroll.set)
        scroll.pack(side=LEFT,fill=Y)
        scroll.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # LABELES
        label1 = Label(f1, text='أنواع الورثة', font=('tajawal', 20, 'bold',))
        label1.place(x=700, y=10)
        label1 = Label(f1, text='أعداد الورثة', font=('tajawal', 20, 'bold'))
        label1.place(x=500, y=10)
        label1 = Label(f1, text='أنواع الورثة', font=('tajawal', 20, 'bold'))
        label1.place(x=300, y=10)
        label1 =Label(f1,text='أعداد الورثة',font=('tajawal', 20, 'bold'))
        label1.place(x=30,y=10)
      
        self.wife = IntVar()
        self.husband = IntVar()
        self.son = IntVar()
        self.daughter = IntVar()
        self.grandson = IntVar()
        self.grandson2=IntVar()
        self.father = IntVar()
        self.mother = IntVar()
        self.grandfather = IntVar()
        self.grandmother = IntVar()
        self.brother = IntVar()
        self.sister = IntVar()
        self.paternal_sister=IntVar()
        self.paternal_brother=IntVar()
        self.mathernal_mother=IntVar()
        self.brother_son=IntVar()
        self.pathernal_brother_son=IntVar()
        self.uncle=IntVar()
        self.pathernal_uncle=IntVar()
        self.cousn=IntVar()

    
       
        list1 = [i for i in range(0,21)]
        list2=[0,1]
        list3=[0,1,2,3,4]
        
        typeCombo1  = Combobox(f1, value=list2, width="5",state='readonly')
        typeCombo1.place(x=450,y=60,height=30,width=200)
        typeCombo1.config(textvariable =self.husband)

        typeCombo2 = Combobox(f1, value=list3, width="5",state='readonly')
        typeCombo2.place(x=450,y=120,height=30,width=200)
        typeCombo2.config(textvariable =self.wife)
       

        typeCombo3 = Combobox(f1, value=list1, width="5",state='readonly')
        typeCombo3.place(x=450,y=180,height=30,width=200)
        typeCombo3.config(textvariable =self.son)
        
        typeCombo4 = Combobox(f1, value=list1, width="5",state='readonly')
        typeCombo4.place(x=450,y=240,height=30,width=200)
        typeCombo4.config(textvariable =self.daughter)

        typeCombo5 = Combobox(f1, value=list1, width="5",state='readonly')
        typeCombo5.place(x=450,y=300,height=30,width=200)
        typeCombo5.config(textvariable =self.grandson)

        typeCombo6 = Combobox(f1, value=list1, width="5",state='readonly')
        typeCombo6.place(x=450,y=360,height=30,width=200)
        typeCombo6.config(textvariable =self.grandson2)

        typeCombo7 = Combobox(f1, value=list2, width="5",state='readonly')
        typeCombo7.place(x=450,y=420,height=30,width=200)
        typeCombo7.config(textvariable =self.father)

        typeCombo8 = Combobox(f1, value=list2, width="5",state='readonly')
        typeCombo8.place(x=450,y=480,height=30,width=200)
        typeCombo8.config(textvariable =self.mother)

        typeCombo9 = Combobox(f1, value=list2, width="5",state='readonly')
        typeCombo9.place(x=450,y=540,height=30,width=200)
        typeCombo9.config(textvariable =self.grandfather)

        typeCombo10 = Combobox(f1, value=list2, width="5",state='readonly')
        typeCombo10.place(x=450,y=600,height=30,width=200)
        typeCombo10.config(textvariable =self.grandmother)
      
        typeCombo11 = Combobox(f1, value=list1, width="5",state='readonly')
        typeCombo11.place(x=20,y=60,height=30,width=200)
        typeCombo11.config(textvariable =self.brother)

        typeCombo12 = Combobox(f1, value=list1, width="5",state='readonly')
        typeCombo12.place(x=20,y=120,height=30,width=200)
        typeCombo12.config(textvariable =self.sister)

        typeCombo13 = Combobox(f1, value=list1, width="5",state='readonly')
        typeCombo13.place(x=20,y=180,height=30,width=200)
        typeCombo13.config(textvariable =self.paternal_sister)

        typeCombo14 = Combobox(f1, value=list1, width="5",state='readonly')
        typeCombo14.place(x=20,y=240,height=30,width=200)
        typeCombo14.config(textvariable =self.paternal_brother)

        typeCombo15 = Combobox(f1, value=list1, width="5",state='readonly')
        typeCombo15.place(x=20,y=300,height=30,width=200)
        typeCombo15.config(textvariable =self.mathernal_mother)

        typeCombo16 = Combobox(f1, value=list1, width="5",state='readonly')
        typeCombo16.place(x=20,y=360,height=30,width=200)
        typeCombo16.config(textvariable =self.brother_son)

        typeCombo17 = Combobox(f1, value=list1, width="5",state='readonly')
        typeCombo17.place(x=20,y=420,height=30,width=200)
        typeCombo17.config(textvariable =self.pathernal_brother_son)

        typeCombo18 = Combobox(f1, value=list1, width="5")
        typeCombo18.place(x=20,y=480,height=30,width=200)
        typeCombo18.config(textvariable =self.uncle)

        typeCombo19 = Combobox(f1, value=list1, width="5",state='readonly')
        typeCombo19.place(x=20,y=540,height=30,width=200)
        typeCombo19.config(textvariable =self.pathernal_uncle)

        typeCombo20 = Combobox(f1, value=list1, width="5",state='readonly')
        typeCombo20.place(x=20,y=600,height=30,width=200)
        typeCombo20.config(textvariable =self.cousn)
        
        

 
        #husband = typeCombo2
        #son = typeCombo3
        #daughter = typeCombo3
        #grandson = typeCombo4
        #grandson2 = typeCombo5
        #father = typeCombo6
        #mother = typeCombo7
        #grandfather=typeCombo8
        #grandmother = typeCombo9
        #maternal_grandmother=typeCombo10
        #brother = typeCombo11
        #sister =typeCombo12




        label1 = Label(f1, text='الزوج', font=('tajawal', 15, 'bold'))
        label1.place(x=750, y=60)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='الزوجه', font=('tajawal', 15, 'bold'))
        label1.place(x=750, y=120)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='الابن ', font=('tajawal', 15, 'bold'))
        label1.place(x=750, y=180)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='البنت', font=('tajawal', 15, 'bold'))
        label1.place(x=750, y=240)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='ابن الابن', font=('tajawal', 15, 'bold'))
        label1.place(x=750, y=300)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='بنت ابن', font=('tajawal', 15, 'bold'))
        label1.place(x=750, y=360)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='الأب', font=('tajawal', 15, 'bold'))
        label1.place(x=750, y=420)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='الأم', font=('tajawal', 15, 'bold'))
        label1.place(x=750, y=480)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='الجد لأب', font=('tajawal', 15, 'bold'))
        label1.place(x=750, y=540)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='الجدة لأب', font=('tajawal', 15, 'bold'))
        label1.place(x=750, y=600)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='الجدة لأم', font=('tajawal', 15, 'bold'))
        label1.place(x=750, y=660)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='الأخ الشقيق', font=('tajawal', 15, 'bold'))
        label1.place(x=320, y=60)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='الأخت الشقيقة', font=('tajawal', 15, 'bold'))
        label1.place(x=320, y=120)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='الأخت لأب', font=('tajawal', 15, 'bold'))
        label1.place(x=320, y=180)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='الأخ لأب', font=('tajawal', 15, 'bold'))
        label1.place(x=320, y=240)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='الإخوة لأم', font=('tajawal', 15, 'bold'))
        label1.place(x=320, y=300)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='ابن الأخ الشقيق', font=('tajawal', 15, 'bold'))
        label1.place(x=320, y=360)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='ابن الأخ لأب', font=('tajawal', 15, 'bold'))
        label1.place(x=320, y=420)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='العم الشقيق', font=('tajawal', 15, 'bold'))
        label1.place(x=320, y=480)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='العم لأب', font=('tajawal', 15, 'bold'))
        label1.place(x=320, y=540)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='ابن العم الشقيق', font=('tajawal', 15, 'bold'))
        label1.place(x=320, y=600)
        label1.config(bg='#e6e4c7')
        label1 = Label(f1, text='	ابن العم لأب	', font=('tajawal', 15, 'bold'))
        label1.place(x=320, y=660)
        label1.config(bg='#e6e4c7')

        # CALCULATION BUTTON
        button = Button(root,text='احسب',font=('tajawal', 20, 'bold'),command=self.mirath)
        button.place(x=1250,y=740 ,width =120,height=40)
        button.config(bg='#D5CEA3')

        button = Button(root,text='خروج',font=('tajawal', 20, 'bold'),command=root.destroy)
        button.place(x=1000,y=740 ,width =120,height=40)
        button.config(bg='#D5CEA3')

        e1 = self.husband.get()
        e2=self.wife.get()
        e3=self.son.get()
        e4=self.daughter.get()
        e5 = self.father.get()
        e6=self.mother.get()
        e7=self.grandson.get()
        e8=self.grandson2.get()
        e9 = self.grandfather.get()
        e10=self.grandmother.get()
        e11 = self.brother.get()
        e12=self.sister.get()
        e13=self.paternal_sister.get()
        e14=self.paternal_brother.get()
        e15 = self.mathernal_mother.get()
        e16=self.brother_son.get()
        e17=self.pathernal_brother_son.get()
        e18=self.uncle.get()
        e19 = self.pathernal_uncle.get()
        e20=self.cousn.get()
        list = []
        list.append(e1)
        list.append(e2)
        list.append(e3)
        list.append(e4)
        list.append(e5)
        list.append(e6)
        list.append(e7)
        list.append(e8)
        list.append(e9)
        list.append(e10)
        list.append(e11)
        list.append(e12)
        list.append(e13)
        list.append(e14)
        list.append(e15)
        list.append(e16)
        list.append(e17)
        list.append(e18)
        list.append(e19)
        list.append(e20)


      

        
        self.cal()
       
    
    def cal(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,'\tتقسيم الميراث')
        self.textarea.config(font=('tajawal',16,'bold'))
        self.textarea.insert(END,"\n-------------------------------------------------------------")
        self.textarea.insert(END,f'\n   نسبة\t         الكسر           \tالعدد\t\tالورثة')
        self.textarea.insert(END,"\n-------------------------------------------------------------")
    
    def mirath(self):
            #WIFE SHARE
            if self.wife.get()>0 and self.husband.get()==0:
                if self.daughter.get()>0 or self.son.get()>0:
                    self.w = 1/8*self.amount.get()
                    self.textarea.insert(END,f'\n   {self.w}\t       {f(1,8)}  \t \t  ({self.wife.get()})\t      الزوجات')
                else:
                    self.w = 1/4*self.amount.get()
                    self.textarea.insert(END,f'\n   {self.w}\t       {f(1,4)} \t \t   ({self.wife.get()})\t   الزوجات')
            else :
                self.textarea.insert(END,'')

            # HUSBAND SHARE
            if self.husband.get()>0 and self.wife.get()==0:
                if self.daughter.get()>0 or self.son.get()>0 :
                    self.h = self.husband.get()*1/8*self.amount.get()
                    self.textarea.insert(END,f'\n   {self.h}\t       {f(1,4)}  \t \t  ({self.husband.get()})\t      الزوج')
                else:
                    self.h = self.husband.get()*1/4*self.amount.get()
                    self.textarea.insert(END,f'\n   {self.h}\t       {f(1,2)} \t \t   ({self.husband.get()})\t   الزوج')
            else :
                self.textarea.insert(END,'')
          
            #SON SHARE
            '''
            if self.son.get()>0:
                
                self.s = self.son.get()
                
                self.textarea.insert(END,f'\n    الباقي تعصيبا للذكر مثل حظ الانثيين \t \t  ({self.son.get()})\t\t    الابن')
            else:
               self.textarea.insert(END,'')'''

            if self.son.get()>0 and self.daughter.get() == 0:
                self.textarea.insert(END,f'\n \t\t   الباقي تعصيبا  \t \t  ({self.son.get()})\t\t    الابن')
            elif self.son.get()>0 and self.daughter.get()>0:
                self.textarea.insert(END,f'\n    الباقي تعصيبا للذكر مثل حظ الانثيين \t \t  ({self.son.get()})\t\t    الابن')
            
            # DAUGHTER SHARE
            if self.daughter.get()>0 :
                if self.son.get()==0 and self.daughter.get()==1:
                    self.d =1/2*self.amount.get()
                    self.textarea.insert(END,f'\n   {self.d}\t      {f(1,2)}  \t \t  البنت')
                else:
                    if self.son.get()==0 and self.daughter.get()>=2:
                        self.d=2/3*self.amount.get()
                        self.textarea.insert(END,f'\n   {self.d}\t      {f(2,3)}  \t \t   ({self.daughter.get()})\t   البنت')
                    if self.son.get()>0:
                        self.d = self.daughter.get()
                        self.textarea.insert(END,f'\n    الباقي تعصيبا للذكر مثل حظ الانثيين \t \t  ({self.daughter.get()})\t\t    البنت')
            else:
                self.textarea.insert(END,'')

            # GRANDSON SHARE
            if self.grandson.get()>0:
                if self.son.get()>0:
                    self.textarea.insert(END,f'\n   \t      محجوب  \t \t  ({self.grandson.get()})\t    ابن الابن')
                else: 
                   if self.son.get()==0:
                      self.textarea.insert(END,f'\n   \t       تعصيب  \t \t  ({self.grandson.get()})\t   ابن الابن')
            else:
                 self.textarea.insert(END,'')

            # GRANDSON2 SHARE   GIRL
            if self.grandson2.get()>0:
                if self.son.get()>0 or self.daughter.get()>=2:
                    self.textarea.insert(END,f'\n   \t      محجوب  \t \t   ({self.grandson2.get()})\t   بنت الابن')
                else:
                    if self.son.get()==0 and self.daughter.get()==0:
                        if self.grandson2.get()==1:
                            self.d =1/2*self.amount.get()
                            self.textarea.insert(END,f'\n   {self.d}\t      {f(1,2)}  \t \t  بنت الابن')
                    else:
                        if self.son.get()==0 and self.daughter.get()==0:
                            if self.grandson2.get()>=2:
                               self.d =2/3*self.amount.get()
                               self.textarea.insert(END,f'\n   {self.d}\t      {f(2,3)}  \t \t   ({self.grandson2.get()})\t   بنت الابن')
                        else:
                            if self.son.get()==0 and self.daughter.get()<=1:
                                if self.grandson2.get()>=2:
                                   self.d =1/6*self.amount.get()
                                   self.textarea.insert(END,f'\n   {self.d}\t      {f(1,6)}  \t \t  بنت الابن')
            else:
                 self.textarea.insert(END,'')

            # FATHER SHARE
            if self.father.get()>0:
                if self.son.get()==0 or self.daughter.get()==0:
                    self.textarea.insert(END,f'\n   \t \t      الباقي تعصيبا  \t \t  الاب')
                else:
                    if self.father.get()>0 and self.son.get()>0 or self.grandson.get()>0:  
                        self.f = self.father.get()*1/6*self.amount.get()
                        self.textarea.insert(END,f'\n   {self.f}\t      {f(1,6)}  \t \t   الاب')
                    else:
                       if self.daughter.get()>0 or self.grandson2.get()>0:
                          self.f = self.father.get()*1/6*self.amount.get()
                          self.textarea.insert(END,f'\n   {self.f}\t      {f(1,6)}+التعصيب  \t \t   الاب')
            else:
                 self.textarea.insert(END,'')

            if self.mother.get()>0:
                if self.son.get()==0 and self.daughter.get()==0 and self.grandson.get()==0 and self.grandson2==0 or self.brother.get()==0 or self.sister.get()==0 :
                    self.m=(1/3)*self.amount.get()
                    self.textarea.insert(END,f'\n   {self.m}\t      {f(1,3)}  \t \t  الام')
                else:
                    if self.mother.get()>0:
                       if self.son.get()>0 and self.daughter.get()>0 and self.grandson.get()>0 and self.grandson2>0 or self.brother.get()>0 or self.sister.get()>0 :
                           self.m=(1/6)*self.amount.get()
                           self.textarea.insert(END,f'\n   {self.m}\t      {f(1,6)}  \t \t  الام')
            else:
                 self.textarea.insert(END,'')


            # GRANDFATHER SHARE
            if self.grandfather.get()>0:
                if self.father.get()>0:
                    self.textarea.insert(END,f'\n   \t       محجوب  \t \t  ({self.grandfather.get()})\t   الجد')
                else:
                    if self.grandfather.get()>0 and self.son.get()==0 or self.daughter.get()==0:
                            self.textarea.insert(END,f'\n   \t       تعصيب  \t \t  ({self.grandfather.get()})\t  الجد')
                    else:
                        if self.grandfather.get()>0 and self.son.get()>0 or self.grandson.get()>0:  
                            self.gf = self.grandfather.get()*1/6*self.amount.get()
                            self.textarea.insert(END,f'\n   {self.gf}\t      {f(1,6)}  \t \t ({self.grandfather.get()})\t   الجد')
                        else:
                            if self.daughter.get()>0 or self.grandson2.get()>0:
                                self.gf = self.grandfather.get()*1/6*self.amount.get()
                                self.textarea.insert(END,f'\n   \t      {f(1,6)}+التعصيب  \t \t({self.grandfather.get()})\t   الجد')
            else:
                self.textarea.insert(END,'')

            # GRANDMOTHER SHARE
            if self.grandmother.get()>0:
                if self.father.get()>0 and self.mother.get()>0:
                    self.textarea.insert(END,f'\n   \t       محجوب  \t \t ({self.grandmother.get()})\t  الجده')
                else:
                    self.gm = self.grandmother.get()*1/6*self.amount.get()
                    self.textarea.insert(END,f'\n   {self.gm}\t      {f(1,6)}  \t \t({self.grandmother.get()})\t   الجده')

            
            # BROTHER SHARE
            if self.brother.get()>0:
                if self.son.get()>0 or self.grandson.get()>0 or self.father.get()>0:
                    self.textarea.insert(END,f'\n   \t       محجوب  \t \t  ({self.brother.get()})\t  الاخ الشقيق')
                else:
                    self.textarea.insert(END,f'\n   \t      التعصيب  \t \t  ({self.brother.get()})\t  الاخ الشقيق')

            # SISTER SHARE
            if self.sister.get()>0:
                if self.son.get()>0 or self.grandson.get()>0 or self.father.get()>0:
                    self.textarea.insert(END,f'\n   \t       محجوب  \t \t ({self.sister.get()})\tالاخت الشقيقه')
                else:
                    if self.sister.get()==1:
                        self.s = self.grandmother.get()*1/2*self.amount.get()
                        self.textarea.insert(END,f'\n   {self.s}\t      {f(1,2)}  \t \t ({self.sister.get()})\tالاخت الشقيقه') 
                    else:
                        if self.sister.get()>1 and self.brother.get()==0:
                            self.s = self.grandmother.get()*2/3*self.amount.get()
                            self.textarea.insert(END,f'\n   {self.s}\t      {f(2,3)}  \t \t ({self.sister.get()})\tالاخت الشقيقه')
                        else:
                            if self.sister.get()>1 and self.brohter.get()>0:
                                self.textarea.insert(END,f'\n   \t    التعصيب  \t \t ({self.sister.get()})\tالاخت الشقيقه')
            else:
               self.textarea.insert(END,'')

            # PATERNAL SISTER
            if self.paternal_sister.get()>0 :
                if  self.brother.get()>0 or self.son.get()>0 or self.grandson.get()>0 or self.sister.get()>0:
                    self.textarea.insert(END,f'\n   \t       محجوبه  \t \t ({self.paternal_sister.get()})\t  الاخت لاب ')
                else:
                    if self.paternal_sister.get()==1 :
                        self.ps=self.paternal_sister.get()*1/2*self.amount.get()
                        self.textarea.insert(END,f'\n   \t       {f(1,2)}  \t \t ({self.paternal_sister.get()})\t  الاخت لاب ')
                    else:
                        if self.paternal_sister.get()>1 and  self.brother.get()==0 or self.son.get()==0 or self.grandson.get()==0 or self.sister.get()==0:
                            self.ps=self.paternal_sister.get()*2/3*self.amount.get()
                            self.textarea.insert(END,f'\n   \t       {f(2,3)}  \t \t ({self.paternal_sister.get()})\t  الاخت لاب ')

                        else:
                            self.textarea.insert(END,f'\n   \t    التعصيب  \t \t ({self.paternal_sister.get()})\tالاخت لاب')
             
            # PATERNAL BROTHER
            if self.paternal_brother.get()>0:
                if self.brother.get()>0 or self.son.get()>0 or self.grandson.get()>0 or self.father.get()>0:
                     self.textarea.insert(END,f'\n   \t       محجوب  \t \t ({self.paternal_brother.get()})\t  الاخ لاب ')

                else:
                    self.textarea.insert(END,f'\n   \t    التعصيب  \t \t ({self.paternal_brother.get()})\tالاخ لاب')

            # PATERNAL MOTHER
            if self.mathernal_mother.get()>0:
                if self.son.get()>0 or self.daughter.get()>0 or self.father.get()>0 or self.grandfather.get()>0 or self.grandson.get()>0:
                    self.textarea.insert(END,f'\n   \t       محجوب  \t \t ({self.mathernal_mother.get()})\t  الاخوه لام ')
                else:
                    if self.mathernal_mother.get()==1:
                        self.textarea.insert(END,f'\n   \t       {f(1,6)}  \t \t ({self.mathernal_mother.get()})\t  الاخوه لام ')

                    else:
                        if self.mathernal_mother.get()>1:
                            self.textarea.insert(END,f'\n   \t       {f(1,3)}  \t \t ({self.mathernal_mother.get()})\t  الاخوه لام ')

            # BROTHER SON 
            if self.brother_son.get()>0:
                if self.grandfather.get()>0 or self.brother.get()>0 or self.son.get()>0 or self.grandson.get()>0 or self.father.get()>0:
                     self.textarea.insert(END,f'\n   \t       محجوب  \t                  ({self.brother_son.get()})\t ابن الاخ الشقيق')
                else:
                    self.textarea.insert(END,f'\n   \t         تعصيب\t                  ({self.brother_son.get()})\t ابن الاخ الشقيق')

            # PATHERNAL BROTHER
            if self.pathernal_brother_son.get()>0:
                if self.brother_son.get()>0 or self.grandfather.get()>0 or self.brother.get()>0 or self.son.get()>0 or self.grandson.get()>0 or self.father.get()>0:
                     self.textarea.insert(END,f'\n   \t       محجوب  \t                  ({self.pathernal_brother_son.get()})\t   ابن الاخ لاب')
                else:
                    self.textarea.insert(END,f'\n   \t         تعصيب\t                  ({self.pathernal_brother_son.get()})\t ابن الاخ الشقيق')

            # UNCLE SHARE
            if self.uncle.get()>0:
                if self.pathernal_brother_son.get()>0 or self.grandfather.get()>0 or self.brother.get()>0 or self.son.get()>0 or self.grandson.get()>0 or self.father.get()>0:
                   self.textarea.insert(END,f'\n   \t       محجوب  \t                  ({self.uncle.get()})\t   العم الشقيق')
                else:
                    self.textarea.insert(END,f'\n   \t         تعصيب\t                  ({self.uncle.get()})\t  العم الشقيق')
    
            # PATHERNAL UNCLE
            if self.pathernal_uncle.get()>0:
                if self.uncle.get()>0 or self.pathernal_brother_son.get()>0 or self.grandfather.get()>0 or self.brother.get()>0 or self.son.get()>0 or self.grandson.get()>0 or self.father.get()>0:
                   self.textarea.insert(END,f'\n   \t       محجوب  \t                  ({self.pathernal_uncle.get()})\t   العم لاب') 
                else:
                    self.textarea.insert(END,f'\n   \t         تعصيب\t                  ({self.pathernal_uncle.get()})\t  العم لاب')
           
            # COUSIN'S SHARE 
            if self.cousn.get()>0:
                if self.pathernal_uncle.get()>0 or self.uncle.get()>0 or self.pathernal_brother_son.get()>0 or self.grandfather.get()>0 or self.brother.get()>0 or self.son.get()>0 or self.grandson.get()>0 or self.father.get()>0:
                   self.textarea.insert(END,f'\n   \t       محجوب  \t                  ({self.cousn.get()})\t   العم لاب') 
                else:
                    self.textarea.insert(END,f'\n   \t         تعصيب\t                  ({self.cousn.get()})\t  العم لاب')
            

            self.textarea.insert(END,"\n-------------------------------------------------------------")
            

root = Tk()
ob = Super(root)
root.mainloop()
