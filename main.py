mala1=int(input("Ievadi kvadrāta malu (cm):"))
if mala1>=5:
  kv_1=mala1*mala1
  kv_2=(mala1+5)*(mala1+5)
  procenti=int((kv_2/kv_1)*100)
  atbilde=str(procenti)+"%"
  print(f"Laukums mainās par {atbilde}")
  

else:
  print("Ievadi lielāku skaitli")