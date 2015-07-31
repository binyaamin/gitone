__author__ = 'Peiman'
import nltk
import re
import time

exampleArray = ['the incredibly intimidating NLP scares people away who are sissies']

def processlanguage():

    try:
        for item in exampleArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)

            print tagged

            chunkGram = r"""Chunk: {<RB\w?>*<VB\w?>*<NNP><VB\w>*}"""
            chunkParsser = nltk.RegexpParser(chunkGram)

            chunked = chunkParsser.parse(tagged)

            print chunked
            chunked.draw()



            #? = 0 or 1 rep
            #* = 0 or more rep
            #+ = 1 or more rep

            time.sleep(555)





    except Exception, e:
        print str(e)

processlanguage()