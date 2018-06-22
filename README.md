# Web-Scraping
A basic web scrapping in python and beautiful soup

## Steps for the installation in Windows:
* Open Command Prompt.
* Check wheather the python 3 is installed or not(To check you can type python --version in command prompt)
* If not install Python version 3.X from here.
* After Installing Python, Install requests, bs4(Beautiful Soup) and lxml.
* Commands for installation: <br>
  **pip install requests** <br>
  **pip install bs4** <br>
  **pip install lxml** <br>
  
 
## Steps to do request to page and importing data
- Open python IDLE.
- import requestes using command **import requests**
- Similarly, import bs4 and lxml.

![import](images/image-1.png)

- After importing, make request to the site want to scrap and store it in the object.Just copy the URL of the webpage and type following command on the IDLE. Replace the single quote with the site you want to scrap.

![request](images/image-2.png)
Here res is the object where all the information of the webpage is getting stored.

- You can check the type of res as shown below.

![Type](images/image-3.png)

- To see what is stored inside the object res type the following command.

![text](images/image-4.png)

- To move further or to do the further operation there is an awesome documentation from [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). You first need to conver the requests type object into bs4 object after that you can do numerous thing on that object listed in the documentaion.
- To convert the object into bs4 object write the following command where res in the object we have already created.

![conversion](images/image-5.png)

- For the confirmation you can check the type of object,it's converted into Beautiful Soup object.

![checkingObject](images/image-6.png)

- To view the the the data related to perticular tag let us suppose class yu can type (.class_name). Similarly for id type (#id_name). Just replace the single quote in the following command with the class or id or anything else you want to have.

![scrap](images/image-7.png)

- To extract the text part from the tag, You can have a loop as shown below.

![loop](images/image-8.png)

- If you want to find all the link in the webpage, run the following command on IDLE

![a_tages](images/image-8.png)

For more refer the documentation provided above.

