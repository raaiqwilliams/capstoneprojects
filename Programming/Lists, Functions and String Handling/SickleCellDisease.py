def translate(dna):                                             #Defining function translate with parameters 'dna'
    count = 0                                                   #Establishing counter
    amino = ''                                                  #Empty string to be used for placing each amino acid symbol in sequence
    codeI = {'ATT','ATC','ATA'}                                 #Instead of using multiple comparison operators in my conditional statement,
    codeL = {'CTT','CTC','CTA','CTG','TTA','TTG'}               #I established dictionarys containing the abbreviations for each amino acid
    codeV = {'GTT','GTC','GTA','GTG'}
    codeF = {'TTT','TTC'}
    codeM = {'ATG'}
    for x in range(len(dna)):                                   #For loop that runs for the length of dna
        slcCode = dna[count:count+3]                            #Splicing string dna to each set of three characters ([0:3] on first iteration, [3:6] on second iteration, etc..)
        if  slcCode in codeI:
            amino += 'I'
        elif slcCode in codeL:
            amino += 'L'
        elif slcCode in codeV:                                  #Taking slcCode and comparing them to dictionaries to determine appropiate abbreviation
            amino += 'V'
        elif slcCode in codeF:
            amino += 'F'
        elif slcCode in codeM:
            amino += 'M'
        elif slcCode == '':                                     #My code continued running to the length of dna so I added this code to break the loop once slcCode was empty
            break
        else:
            amino += 'X'                                        #Value is X if code is not contained in dictionary
        count += 3                                              #Increasing counter by 3 to increment past characters that were previously contained in slcCode
    return amino                                                #Returning value

def mutate():
    f = open('DNA.txt','r',encoding='utf-8-sig')                #Opening file
    data = f.read()                                             #Reading entire file and setting it to variable data
    firstOccurence = data.find("a")                             #Finding first occurence of lowercase "a"
    normalDNA = open("normalDNA.txt", "w")                      
    mutatedDNA = open("mutatedDNA.txt","w")                     #Opening and creating files for ouput
    normalDNA.write(data.upper())                               #Set the entire file to uppercase, bypassing the need to use variable firstOccurence
    mutatedDNA.write(data.replace("a","T"))                     #Replacing lowercase "a" with uppercase "T"
    f.close()
    normalDNA.close()                                           #Closing files
    mutatedDNA.close()

def txtTranslate():
    mutate()                                                    #Calling mutate function
    with open('mutatedDNA.txt','r') as f:
        data = f.read()                                         
        mutatedDNA = translate(data)
    with open('normalDNA.txt','r') as g:                        #Opening output files and setting values to variables mutatedDNA and normalDNA, 
        data = g.read()                                         #along with passing variables to translate function
        normalDNA = translate(data)
    print(mutatedDNA)
    print(normalDNA)

txtTranslate()
userDNA = input("Please enter a DNA sequence: ")
print(translate(userDNA))
