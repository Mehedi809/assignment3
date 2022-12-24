#my project is image download in online site
import requests

def Dnload_pro(a):
    try:
        First_inp = int(input("Enter a total image: "))   #Total image user input
        url_dict = {}  # This is empty dictionary

        # This loop is input 
        for i in range (1, First_inp+1):
            img_name = input("Please image name here: ")
            img_url = input("Please 'copy image address' here: ")
            url_dict[img_name]=img_url

        # This loop is dict key and value different variable
        for x, y in url_dict.items():
            r = requests.get(y) #This url var is y  

            with open(x, "wb") as f: #This is print the name and url hit , then output at download image
                f.write(r.content)
    except:
        print("Sorry!, The program did not work. Please use the program properly.")

func_inp = input("This program will not download images from any paid online site, is the program really useful for you? If yes then write 'Yes' and if not then write 'No'.: ")
if func_inp=="Yes":
    Dnload_pro(func_inp)   #call function
else:
    print("Then this code will not be of any use to you, thanks.")

            
    # This my project, please check this program code and where is problem inform me