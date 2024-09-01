class BusBooking:
    def __init__(self,w=None,a=None):
        self.w=w
        self.a=a
        if self.w!=None:
            self.wl=[0 for i in range(self.w)]
            self.wname=[" " for i in range(self.w)]
            self.booking_idw=[" " for i in range(self.w)]
        else:
            self.wl=[]
            self.wname=[]
            self.booking_idw=[]
        if self.a!=None:    
            self.al=[0 for i in range(self.a)]
            self.aname=[" " for i in range(self.a)]
            self.booking_ida=[" " for i in range(self.a)]
        else:
            self.al=[]
            self.aname=[]
            self.booking_ida=[]
        self.wa=[]
    def book(self,name,preference=None):
        if self.w==None and self.a==None:
            return("It is an empty bus")
        elif self.w!=None and self.a==None:
            l=["w","W","a","A","Window","window","Aisle","aisle",None]
            if preference not in l:
                return("Enter a valid preference")
            else:
                kw=-1
                for i in range(self.w):
                    if self.wl[i]==0:
                        kw=i
                        self.wl[i]=1
                        booking_id=name+" "+"W"+" "+str(kw+1)
                        self.booking_idw[kw]=booking_id
                        outcome="W"+" "+str(kw+1)
                        return( booking_id,outcome)
                if kw==-1:                
                    l=len(self.wa)
                    self.wa.append(name+" "+"WL"+" "+str(l+1))
                    booking_id=name+" "+"WL"+" "+str(l+1)
                    outcome="WL-"+str(l+1)
                    return(booking_id,outcome)
        elif self.w==None and self.a!=None:
            l=["w","W","a","A","Window","window","Aisle","aisle",None]
            if preference not in l:
                return("Enter a valid preference")
            else:
                ka=-1
                for i in range(self.a):
                    if self.al[i]==0:
                        ka=i
                        self.al[i]=1
                        booking_id=name+" "+"A"+" "+str(ka+1)
                        self.booking_ida[ka]=booking_id
                        outcome="A"+" "+str(ka+1)
                        return(booking_id,outcome)
                if ka==-1:
                    l=len(self.wa)
                    self.wa.append(name+" "+"WL"+" "+str(l+1))
                    booking_id=name+" "+"WL"+" "+str(l+1)
                    outcome="WL-"+str(l+1)
                    return(booking_id,outcome)
        elif self.w!=None and self.a!=None:                           
            if preference=="W" or "Window" or "w" or "window":
                kw=-1
                for i in range(self.w):
                    if self.wl[i]==0:
                        kw=i
                        self.wl[i]=1
                        booking_id=name+" "+"W"+" "+str(kw+1)
                        self.booking_idw[kw]=booking_id
                        outcome="W"+" "+str(kw+1)
                        return( booking_id , outcome)                                
                if kw==-1:
                    ka=-1
                    for i in range(self.a):
                        if self.al[i]==0:
                            ka=i
                            self.al[i]=1
                            booking_id=name+" "+"A"+" "+str(ka+1)
                            self.booking_ida[ka]=booking_id
                            outcome="A"+" "+str(ka+1)
                            return(booking_id,outcome)
                    if ka==-1:
                        l=len(self.wa)
                        self.wa.append(name+" "+"WL"+" "+str(l+1))
                        booking_id=name+" "+"WL"+" "+str(l+1)
                        outcome="WL-"+str(l+1)
                        return(booking_id,outcome)
            elif preference=="A" or "Aisle" or "a" or "aisle":
                ka=-1
                for i in range(self.a):
                    if self.al[i]==0:
                        ka=i
                        self.al[i]=1
                        booking_id=name+" "+"A"+" "+str(ka+1)
                        self.booking_ida[ka]=booking_id
                        outcome="A"+" "+str(ka+1)
                        return(booking_id,outcome)
                if ka==-1:
                    kw=-1
                    for i in range(self.w):
                        if self.wl[i]==0:
                            kw=i
                            self.wl[i]=1
                            booking_id=name+" "+"W"+" "+str(kw+1)
                            self.booking_idw[kw]=booking_id
                            outcome="W"+" "+str(kw+1)
                            return( booking_id,outcome)
                    if kw==-1:
                        l=len(self.wa)
                        self.wa.append(name+" "+"WL"+" "+str(l+1))
                        booking_id=name+" "+"WL"+" "+str(l+1)
                        outcome="WL-"+str(l+1)
                        return(booking_id,outcome)
            elif preference==None:
                ka=-1
                for i in range(self.a):
                    if self.al[i]==0:
                        ka=i
                        self.al[i]=1
                        booking_id=name+" "+"A"+" "+str(ka+1)
                        self.booking_ida[ka]=booking_id
                        outcome="A"+" "+str(ka+1)
                        return(booking_id,outcome)
                if ka==-1:
                    kw=-1
                    for i in range(self.w):
                        if self.wl[i]==0:
                            kw=i
                            self.wl[i]=1
                            booking_id=name+" "+"W"+" "+str(kw+1)
                            self.booking_idw[kw]=booking_id
                            outcome="W"+" "+str(kw+1)
                            return( booking_id,outcome)
                if kw==-1:
                    l=len(self.wa)
                    self.wa.append(name+" "+"WL"+" "+str(l+1))
                    booking_id=name+" "+"WL"+" "+str(l+1)
                    outcome="WL-"+str(l+1)
                    return(booking_id,outcome)
        else:
            return("Enter a valid Preference")               
    def cancel(self,booking_id):
        if booking_id in self.booking_idw:
            k=self.booking_idw.index(booking_id)
            self.booking_idw[k]=" "
            self.wl[k]=0
            if len(self.wa)>0:
                self.wl[k]=1
                g=self.wa[0].split()
                h=g[0]+" "+"W"+" "+str(k+1)
                self.booking_idw[k]=h
                self.wa.remove(self.wa[0])
            if len(self.wa)>0:
                for i in range(len(self.wa)):
                    n=self.wa[i].split()
                    self.wa[i]=n[0]+" "+"WL"+str((int(n[2])-1))
            return True
        elif booking_id in self.booking_ida:
            k=self.booking_ida.index(booking_id)
            self.booking_ida[k]=" "
            self.al[k]=0
            if len(self.wa)>0:
                self.al[k]=1
                g=self.wa[0].split()
                h=g[0]+" "+"A"+" "+str(k+1)
                self.booking_ida[k]=h
                self.wa.remove(self.wa[0])
            if len(self.wa)>0:
                for i in range(len(self.wa)):
                    n=self.wa[i].split()
                    self.wa[i]=n[0]+" "+"WL"+" "+str((int(n[2])-1))                    
            return True    
        elif booking_id in self.wa:
            k=self.wa.index(booking_id)
            self.wa.remove(self.wa[k])
            if len(self.wa)>0:
                for i in range(k,len(self.wa)):
                     n=self.wa[i].split()
                     self.wa[i]=n[0]+" "+"WL"+" "+str((int(n[2])-1))                     
            return True
        return False
    def status(self,booking_id):
        if booking_id in self.booking_idw and booking_id!=" ":
            g=booking_id.split()
            k=self.booking_idw.index(booking_id)
            return(g[0],"W"+" "+str(k+1))
        elif booking_id in self.booking_ida and booking_id!=" ":
             g=booking_id.split()
             k=self.booking_ida.index(booking_id)
             return(g[0],"A"+" "+str(k+1))
        elif booking_id in self.wa:
            g=booking_id.split()
            k=self.wa.index(booking_id)
            return(g[0],"WL"+" "+str(k+1))
        else:
            return("booking_id does not exist")    
            
    def __str__(self):
        l1=[]
        l2=[]
        l3=[]
        for i in range(len(self.booking_idw)):
            if self.booking_idw[i]!=" ":
                g=self.booking_idw[i].split()
                l1.append((self.booking_idw[i],g[0],self.status(self.booking_idw[i])))
                
        for i in range(len(self.booking_ida)):
            if self.booking_ida[i]!=" ":
                g=self.booking_ida[i].split()
                l2.append((self.booking_ida[i],g[0],self.status(self.booking_ida[i])))
                
        for i in range(len(self.wa)):
            if self.wa[i]!=" ":
                g=self.wa[i].split()
                l3.append((self.wa[i],g[0],self.status(self.wa[i])))
        l=l1+l2+l3
        l.sort()
        return(l)


        

    
    
                    
        
        
        
