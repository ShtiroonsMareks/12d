"""
mala1=int(input("Ievadi kvadrāta malu (cm):"))
if mala1>=5:
  kv_1=mala1*mala1
  kv_2=(mala1+5)*(mala1+5)
  procenti=int((kv_2/kv_1)*100)
  atbilde=str(procenti)+"%"
  print(f"Laukums mainās par {atbilde}")
  

else:
  print("Ievadi lielāku skaitli")
"""
import math
rinka_r= float(input("Ievadi riņķa rādiusa garumu (cm): "))
tr_hip=float(input("Ievadi trijstūra hipotenūzas garumu (cm): "))

mala_a=tr_hip*math.sin(math.radians(45))
mala_b=math.sqrt(math.pow(tr_hip,2)-math.pow(mala_a,2))
lauk_tr=(mala_a*mala_b)/2

lauk_r=math.pi*math.pow(rinka_r,2)

starpība=round(lauk_r-lauk_tr,1)
print(f"Riņka laukums ir par {starpība} cm^2 lielāks nekā trijstūra laukums!")