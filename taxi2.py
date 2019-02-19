try:
	b=raw_input()
	a=0
	if (b.isalpha()):
	  print('wrong input')
	elif not b:
	  print('enter anything')
	elif float(b)<=0:
	  print("wrong destination")
	else:
	            km=a+float(b)
	            print ('total km=',km)
	            print("1.micro\n 2.mini\n 3.premium\n")
	            n=float(raw_input())
	            key=round(n)
	            if float(key)==1:
	              fare=km*10
	            elif float(key)==2:
	              fare=km*15
	            elif float(key)==3:
	              fare=km*30
	            else:
	              print("invalid choice")
except ValueError:
	print("false input")
finally:
  print("***Invoice of your travel***")
  print('fare','km',fare,km)
  print("thank you..")
