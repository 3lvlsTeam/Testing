import re
index=0
word=['A','A','A','A','A','A','A','A','0','0','!','!']
end_L=125
start_L=33


def check_if_liget(text):

    cheknum=False
    cheksmall=False
    chekcap=False
    chekchar=False

    word= str(text)

    chaar=0
    cap=0
    som=0
    num=0
    som=0

    num = len(re.findall(r"\d", word ))
    if num == 2 :
        cheknum=True
    small = len(re.findall(r"[a-z]",word))
    if small >= 1:
        cheksmall=True
    cap = len(re.findall(r"[A-Z]",word))
    if cap >=1:
        chekcap=True

    chaar = small+ cap
    if chaar == 8 :
        chekchar=True

    if chekcap and chekchar and cheknum and cheksmall  :
        return True


word_list='Words_list.txt'

print("generating...")

while True:   
    if check_if_liget(word):    
        with open(word_list,'a') as f:
            f.writelines(word)
            f.writelines('\n')
                
    try:
        while ord(word[index]) > end_L:
            word[index]=chr(start_L)
            index=index+1
        
        word[index]=chr(ord( word[index])+1)
        index=0
    except:
        print("Done!")
        break

input()