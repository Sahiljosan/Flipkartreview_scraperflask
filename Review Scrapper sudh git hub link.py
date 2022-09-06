from flask import Flask , render_template , request , jsonify
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as urReq

flipcart_url = "https://www.flipkart.com/search?q="+"iphone11"

response_website = urReq(flipcart_url)

response_website.read()

data_flipcart = response_website.read()

bigbox = beautifyed_html.find_all("div" , {"class":"_1AtVbE col-12-12" })


product6 = "https://www.flipkart.com" + bigbox[6].div.div.div.a['href']

import requests

product66 = requests.get(product6)

product66.encoding= 'utf-8'

bs(product66.text,"html.parser")



https://drive.google.com/drive/folders/17XAlmtcjT1ceYyGWutaYn_IZOw1mTIzc?usp=sharing


https://docs.google.com/document/d/1E7W4JZY_77NqdF6cUfWE3u3ukvCb3hhJ/edit?usp=sharing&ouid=118282207943964605599&rtpof=true&sd=true



1). Heroku Deployment

- First install Heroku cli as per your system compatibility: https://devcenter.heroku.com/articles/heroku-cli
- Create a heroku account.
- Will push our project in github.
- Create a new repository in github.Open you cmd, be in your project folder first then run the below commands:
      - git init
      - git add .
      - git commit -m "first commit"
      - git branch -M main
      - git remote add origin 'your own .git' file(like this git remote add origin https://github.com/vikash130795/era.git)
      - git push -u origin main

In last command, it'll ask for token.
- On right-hand side at the top, you'll get your profile in which you'll get 'Settings' option.
- After clicking on 'Settings', it will redirect us to next page. On the left-hand side at bottom 'Developer settings' is there.
- Then, select 'Personal access tokens' in which you can 'Generate new token'.
- Place the generated token in the last command option, your project would be pushed in your github repository.

- Check in your cmd heroku is installed or not by this command, 'heroku'.
- If its available then, do login in heroku using this command 'heroku login'.
- Be in your project folder and run this command 'heroku git:remote -a <your appname>'
- Then, push your code with this command 'git push heroku master'
- Now, your app is successfully deployed in heroku.