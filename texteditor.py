from sys import argv
filename, doc = argv
input(f"""***PRIMITIVE TEXT EDITOR***
File to be edited: {doc}
Press Ctrl+c to abort the process or Enter to resume\n""")
print(f"""Press 
'o' to show contents
'c' to clear
'i' to insert line
'x' to exit""")
while True:
    prompt = input("\n==> ")
    if prompt == 'o':
        print(f"\nOpening...\n{open(doc,'r').read()}")
        #file need not be closed as compund statement is used
    elif prompt == 'c':
        open(doc,'w')
        print("\nFile cleared")
    elif prompt == 'i':
        open(doc,'a').write(input("\nEnter text: ")+'\n')#new line added to text
        print("\nLine inserted")
    elif prompt == 'x':
        print("\nExiting...")
        break
    else:
        print("\nWrong input try again :)")
