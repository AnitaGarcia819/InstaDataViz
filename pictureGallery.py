import os

for x in range(20):
	os.system("scp file" + str(x) + ".jpg gradinsk@radinsky.me:/var/www/html/205/img/")
