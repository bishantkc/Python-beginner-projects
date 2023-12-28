import requests

my_data = {"name": "Tom", "email": "tom@example.com"}
r = requests.post("https://www.w3schools.com/php/welcome.php", data= my_data) #url is just for sample u need some other valid website

f = open("../myfile.html", "w+")
f.write(r.text)