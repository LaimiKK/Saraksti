print("kuru no cipariem vēlies risināt?")
print("izvēlies ciparu")
print("1 - pirmo uzdevumu")
print("2 - otro uzdevumu")
print("3 - trešo uzdevumu")
i = int(input(": "))
print("_______________________")
if i == 1:
  print("Tu izvēlējies uzdevumu nr. 1")
if i == 2:
  print("Tu izvēlējies uzdevumu nr. 2")
if i == 3:
  print("Tu izvēlējies uzdevumu nr. 3")
  Q=["Cik ir 2+2?", "cik ir 5*5?","Latvijas galvaspilsētas nosaukums ir?", "Cik ir 50*0?","Cik dienu ir nedēļā?"]
  A=["4","25","Rīga","0","7"]
  g=len(Q)
  p=0
  n=0
  for s in range(0, g):
    print("----------------------------")
    h=[]
    cc = (input(f"{Q[s]} atbilde:"))
    h.append(cc)
    if h[0]==A[s]:
      p= p+1
    else:
      n= n+1 
  if p== 5:
    print("viss ir pareizi")
  else:
    print("pareizo atbilžu bija",p)
    print("nepareizo atbilžu bija",n)
