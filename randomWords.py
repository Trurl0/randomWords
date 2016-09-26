#!usr/bin/env python  
#coding=utf-8
######
# randomWords
# Arrealist poetry on python
# author: Trurl
# July 2015
######


import random
import time
import sys
import subprocess

check_pyttsx = False
try:
    import pyttsx
    check_pyttsx = True
except:
    print "pyttsx not found"
    
def readWords(fileName):
    #Reads a file storing it by lines in a string list
    list = open(fileName).readlines()
    list=[x.strip("\n").strip(" ").strip("	") for x in list]
    return list

def cap(word):
    #Capitalizes first word of a string
    return word.capitalize()
    
def noun():
    return random.choice(nouns)
def pronoun():
    return random.choice(pronouns)
def verb():
    return random.choice(verbs)
def adverb():
    return random.choice(adverbs)
def adjective():
    return random.choice(adjectives)
def preposition():
    return random.choice(prepositions)
def structure():
    return random.choice(structures)
    
def getTense(input_verb, tense = "past"):
    irregularFlag = False
    for entry in tenses:
        entry_root = entry.split(" ")[0]
        if input_verb == entry_root:
            irregularFlag = True
            if tense == "participle":
                return_verb = entry.split(" ")[2]
            else:
                return_verb = entry.split(" ")[1]
    if not irregularFlag:
        if input_verb[-1] not in ["a","e","i","o","u",]:
            return_verb = input_verb+"ed"
        else:
            return_verb = input_verb+"d"
    return return_verb

def past_verse():
    phrase = structure()
    while "will" in phrase:
        phrase = structure()
    verse=""
    for word in phrase.split(" "):

        #Replace NOUNs before NOUN!!
        if "NOUNs" in word:
            nounTemp = noun()+"CHECK_END" #Check if noun ends with 's' or 'y'
            if "sCHECK_END" in nounTemp or "shCHECK_END" in nounTemp or "chCHECK_END" in nounTemp:
                nounTemp=nounTemp.replace("CHECK_END","")
                word=word.replace("NOUNs", nounTemp+"es")
            elif "yCHECK_END" in nounTemp:
                nounTemp=nounTemp.replace("yCHECK_END","i")
                word=word.replace("NOUNs", nounTemp+"es")
            else:
                nounTemp=nounTemp.replace("CHECK_END","")
                word=word.replace("NOUNs", nounTemp+"s")

        word=word.replace("NOUN", noun())
        word=word.replace("ADJ", adjective())
        word=word.replace("ADV", adverb())
        word=word.replace("PREP", preposition())
        
        word=word.replace("VERB", getTense(verb(), "past"))
        

        verse=verse+word+" "
    for vowel in ["a","e","i","o","u"]:
        verse=verse.replace(" a "+vowel," an "+vowel) #Probably some more grammatical checks are needed...
        verse=verse.replace("A "+vowel,"An "+vowel)
    return cap(verse)

def verse():
    phrase = structure()
    verse=""
    for word in phrase.split(" "):

        #Replace NOUNs before NOUN!!
        if "NOUNs" in word:
            nounTemp = noun()+"CHECK_END" #Check if noun ends with 's' or 'y'
            if "sCHECK_END" in nounTemp or "shCHECK_END" in nounTemp or "chCHECK_END" in nounTemp:
                nounTemp=nounTemp.replace("CHECK_END","")
                word=word.replace("NOUNs", nounTemp+"es")
            elif "yCHECK_END" in nounTemp:
                nounTemp=nounTemp.replace("yCHECK_END","i")
                word=word.replace("NOUNs", nounTemp+"es")
            else:
                nounTemp=nounTemp.replace("CHECK_END","")
                word=word.replace("NOUNs", nounTemp+"s")

        word=word.replace("NOUN", noun())
        word=word.replace("ADJ", adjective())
        word=word.replace("VERB", verb())
        word=word.replace("ADV", adverb())
        word=word.replace("PREP", preposition())
        

        verse=verse+word+" "
    for vowel in ["a","e","i","o","u"]:
        verse=verse.replace(" a "+vowel," an "+vowel) #Probably some more grammatical checks are needed...
        verse=verse.replace("A "+vowel,"An "+vowel)
    return cap(verse)

def verseRhyme(rhyme):
    phrase = structure()
    verse=""
    for i, word in enumerate(phrase.split(" ")):
    
        #Replace NOUNs before NOUN!!
        if "NOUNs" in word:
            nounTemp = noun()+"CHECK_END" #Check if noun ends with 's' or 'y'
            if "sCHECK_END" in nounTemp or "shCHECK_END" in nounTemp or "chCHECK_END" in nounTemp:
                nounTemp=nounTemp.replace("CHECK_END","")
                word=word.replace("NOUNs", nounTemp+"es")
            elif "yCHECK_END" in nounTemp and not ["ay","ey","iy","oy","uy"] in nounTemp:
                nounTemp=nounTemp.replace("yCHECK_END","i")
                word=word.replace("NOUNs", nounTemp+"es")
            else:
                nounTemp=nounTemp.replace("CHECK_END","")
                word=word.replace("NOUNs", nounTemp+"s")

        word=word.replace("NOUN", noun())
        word=word.replace("ADJ", adjective())
        word=word.replace("VERB", verb())
        word=word.replace("ADV", adverb())
        word=word.replace("PREP", preposition())
        
                   
        #Override last with rhyming word
        if i == len(phrase.split(" "))-1:
            try:
                for list in nounsRhyme:
                    if rhyme in list:
                        rhymeCandidate = random.choice(list.split(","))
                        while rhymeCandidate in rhyme:#Don't pick the same as the model
                            rhymeCandidate = random.choice(list.split(","))
                        word = word.replace(word,rhymeCandidate)
                        break
            except:
                print "NO RHYME"
        verse=verse+word+" "
    for vowel in ["a","e","i","o","u"]:
        verse=verse.replace(" a "+vowel," an "+vowel) #Probably some more grammatical checks are needed...
        verse=verse.replace("A "+vowel,"An "+vowel)
    return cap(verse)

def writeCmd():
    paragraphCount=0
    verseCount=0
    while True:
        line = verse() #Creates a verse
        #Print a space after 4th verse
        if not paragraphCount:
            paragraphCount = 4
            print
            time.sleep(0.5)
        paragraphCount -= 1

        #Print letter by letter
        verseCount = 0
        while verseCount < len(line):
            sys.stdout.write(line[verseCount])
            verseCount+=1
            time.sleep(0.05)
        print #Line Feed
        time.sleep(0.5)
        
def writeTxt(filename):
    #title = verse()
    #poem = open(title+".txt",'w')
    poem = open(filename,'a')
    #poem.write(title+"\n")
    
    verseLimit=8
    for lineCount in range(verseLimit):
        line = verse() #Creates a verse
        #Print a space after 4th verse
        if lineCount%4 == 0:
            poem.write("\n")
        poem.write(line+"\n")
    poem.close()
 
def writeCmdAndTxt(filename):
    poem = open("poem.txt",'w')

    paragraphCount=0
    verseCount=0
    while True:
        line = random.choice([verse(), past_verse()]) #Creates a verse
        #Print a space after 4th verse
        if not paragraphCount:
            paragraphCount = 4
            print
            poem.write("\n")
            time.sleep(0.5)
        paragraphCount -= 1

        poem.write(line+"\n")

        #Print letter by letter
        verseCount = 0
        while verseCount < len(line):
            sys.stdout.write(line[verseCount])
            verseCount+=1
            time.sleep(0.05)
        print #Line Feed
        time.sleep(0.5)
        
def writeCmdRhyme():
    paragraphCount=0
    verseCount=0
    while True:
    
        #Print a space after 4th verse
        if not paragraphCount:
            paragraphCount = 4
            print
            time.sleep(0.5)
            #Choose rhyming word
            rhyme1=random.choice(random.choice(nounsRhyme).split(","))
        paragraphCount -= 1
        
        if paragraphCount%2==0:
            line = verseRhyme(rhyme1)
            rhyme1= line.split(" ")[-2]#Replace rhyme with last to avoid repetition
        else:
            line = verse() #Creates a verse
        
        #Print letter by letter
        verseCount = 0
        while verseCount < len(line):
            sys.stdout.write(line[verseCount])
            verseCount+=1
            time.sleep(0.05)
        print #Line Feed
        time.sleep(0.5)

def writeCmdDoubleRhyme():
    paragraphCount=0
    verseCount=0
    while True:
    
        #Print a space after 4th verse
        if not paragraphCount:
            paragraphCount = 4
            print
            time.sleep(0.5)
            #Choose rhyming word
            rhyme1=random.choice(random.choice(nounsRhyme).split(","))
            rhyme2=random.choice(random.choice(nounsRhyme).split(","))
            rhymeLine = ""
            for line in nounsRhyme:
                if rhyme1 in line:
                    rhymeLine = line
            while rhyme2 in rhymeLine:
                rhyme2=random.choice(random.choice(nounsRhyme).split(","))
        paragraphCount -= 1
        
        if paragraphCount%2==0:
            line = verseRhyme(rhyme1)
        else:
            #line = verse() #Creates a verse
            line = verseRhyme(rhyme2)
        
        #Print letter by letter
        verseCount = 0
        while verseCount < len(line):
            sys.stdout.write(line[verseCount])
            verseCount+=1
            time.sleep(0.05)
        print #Line Feed
        time.sleep(0.5)

def sing(tts = "pyttsx"):
    lineCount=0
    while True:
        lineCount+=1
        line = verse() #Creates a verse
        print line
        #Pause after 4th verse
        if lineCount%4 == 0:
            sayPyTTSx("     ")
            print
        if tts.lower() == "espeak":
            sayEspeak(line)
        else:
            sayPyTTSx(line)
    
def singOutLoud2(tts = "pyttsx"):
    while True:
            paragraph = verse()+",\n "+verse()+",\n "+verse()+",\n "+verse()
            print paragraph
            sayPyTTSx(paragraph)
            print
    
def sayPyTTSx(text):  
    if check_pyttsx:
        engine = pyttsx.init()
        engine.setProperty('rate', 140)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
    else:
        print "no pyttsx found"

def sayEspeak(text):
    voice = "en+f5"
    volume = "200"
    pitch = "50"
    speed = "160"
    command = ["C:\Program Files (x86)\eSpeak\command_line\espeak",
               "-v",voice, 
               "-a",volume,
               "-p",pitch, 
               "-s",speed,
               text]
    subprocess.call(command)
   
   
adjectives=readWords("libs\\adjectives.txt")
nouns=readWords("libs\\nouns.txt")
verbs=readWords("libs\\verbs.txt")
adverbs=readWords("libs\\adverbs.txt")
pronouns=readWords("libs\\pronouns.txt")
prepositions=readWords("libs\\prepositions.txt")

nounsRhymeRaw=readWords("libs\\nounsRhyme.txt")

tenses = readWords("libs\\tenses.txt")

#Unnecessary when rhymed list is complete:
nounsRhyme = []
for i,line in enumerate(nounsRhymeRaw):
    if "," in line:
        nounsRhyme.append(line)

structures=[
  "As NOUN VERB",
  "VERB in the NOUNs",
  "The ADJ NOUN ADV VERBs the NOUN",
  "ADJ, ADJ NOUNs",
  "ADV VERB a ADJ, ADJ NOUN",
  "A NOUN is a ADJ NOUN",
  "The NOUN is a ADJ NOUN",
  "The NOUN VERBs like a ADJ NOUN",
  "NOUNs VERB like ADJ NOUNs",
  "VERB ADV like a ADJ NOUN",
  "NOUN, NOUN and NOUN",
  "All NOUNs VERB ADJ, ADJ NOUNs",
  #"Never VERB a NOUN",
  "ADV VERB a NOUN",
  "A NOUN, ADV VERB",
  "NOUNs, as ADJ NOUNs",
  "PREP the ADJ NOUN",
  
  "Why does the NOUN VERB?",
  "Why the ADJ NOUN?",
  "Where is the ADJ NOUN?",
  "When will the NOUN VERB?",
  "What NOUN will VERB the NOUNs?",
  "ADV a ADJ NOUN?",
  "ADV VERB?",
  "NOUN?",

  "NOUNs VERB!",
  "A ADJ NOUN!",
  "ADV VERB!",
  "NOUN!",
  "A ADJ NOUN!",
  ]

#MAIN:
if __name__ == "__main__":
    writeCmdAndTxt("mypoem.txt")
    