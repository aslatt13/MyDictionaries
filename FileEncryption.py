#Write a program that uses a dictionary to assign “codes” to each letter 
# of the alphabet. For example:
#codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .} 
# Using this example, the letter A would be assigned the symbol %, 
# the letter a would be assigned the number 9, the letter B would 
# be assigned the symbol @, and so forth. The program should open 
# this file -  info_security.txt  Download info_security.txt, 
# read its contents, then use the dictionary to write an encrypted 
# version of the file’s contents to a second file (name it 'encrypted.txt'). 
# Each character in the second file should contain the code for 
# the corresponding character in the first file.

infile = open('info_security.txt','r')

reader = infile.read()

outfile = open('encrypted.txt','w')

reader = str(reader)

encryption = {'A': '=','a':'-','B':'0','b':'9','C':'8','c':'7','D':'6','d':'5','E':'4','e':'3','F':'2','f':'1','G':'~','g':'!','H':'@','h':'#','I':'$','i':'%','J':'^','j':'&','K':'*','k':'(','L':')','l':'-','M':'+','m':'=','N':'{','n':'[','O':'}',"o":"]","P":"|","p":":","Q":";","q":"<","R":",","r":">","S":"?","s":".","T":"/","t":"A","U":"b","u":"C","V":"d","v":"e","W":"F","w":"f","X":"G","x":"H","Y":"I","y":"j","Z":"k","z":"L"}

for letter, encrypted in encryption.items():
    reader = reader.replace(letter, encrypted)

outfile.write(reader)

infile.close()
outfile.close()
