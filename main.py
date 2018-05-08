x=open("demoText.txt",'r').read()

lines=x.split("\n")
charsPerLine=max(map(len,lines))
finalSentance=""
for i in range(0,len(lines)-2):
  line=lines[i]
  nextLine=lines[i+1]
  print(len(line)+len(nextLine.split()[0]))
  if((len(line)+len(nextLine.split()[0])) >= charsPerLine or not "." in line.split()[-1]):
    finalSentance+=line+" ";
  else:
    finalSentance+=line+"\n"
print (finalSentance)