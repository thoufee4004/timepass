while True:
	try:
		b=raw_input()
		a=0
		if (b.isalpha()):
			print('wrong input')
		elif float(b)<=0:
			print("wrong destination")
		elif float(b)>0:
				km=a+float(b)
            	print ('total km=',km)
            	print("1.micero\n 2.mini\n 3.premium\n")
            	n=float(raw_input())
            	key=round(n)
            	if float(key)==1:
            		print("fare=",km*10)
            	elif float(key)==2:
            		print("fare=",km*15)
            	elif float(key)==3:
            		print("fare=",km*30)
            	else:
            		print("invalid choice")
    	except:
		print("false entry")
		break
