'''write a class train which has methods to 
book a ticket , get status (no. of seats)
and get fare info. of train running under Indian Railways
'''
from random import randint

class Train:
     def __init__(self , TrainNo):
      self.TrainNo = TrainNo
     
     def book(self, fro ,to):
         print(f"Ticket is booked in train no. {self.TrainNo} from {fro} to {to}")
         
     def getStatus(self):
         print(f"TRain no: {self.TrainNo} is running on time!!")
     
     def fetFare(self , fro , to ):
         print(f"Ticket fare in train no: {self.TrainNo} from {fro} to {to} {randint(222,5555)}")
         
t = Train("SR1234")
t.book("rampur" , "sirohi")
t.getStatus()
t.fetFare("rampur" , "surat")