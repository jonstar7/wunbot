import psutil

for proc in psutil.process_iter():
	#if proc.name() == row[2]:
		#proc.kill()
	print(proc.name())