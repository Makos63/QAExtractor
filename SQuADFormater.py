import json
import numpy as np
import uuid
import array as arr
import re

with open("data3.json") as b:
    b = json.load(b)

t = list()
idcounter = 0

data = list()
ans = list()
qas = list()
question = list()
context = ''

for qa in b:

    bodyString=qa["body"]
    headerString=qa["header"]

    context += headerString
    context += bodyString
    #context += ' '
    context += ' '

with open("context.txt", "w") as new_b:
    new_b.write(context)

for qa in b:
    bodyString=qa["body"]
    headerString=qa["header"]

    #absolutePosition = re.search(bodyString, context)
    absolutePosition = context.find(bodyString)

    if absolutePosition is not None:
        absolutePosition = absolutePosition + 1
        #absolutePosition = absolutePosition.start()+1
    else:
        print("absolutePosition with regex could not be determined, following has been caught: ")
        print("<------------------------------->")
        print(headerString)
        print(bodyString)
        print("---------------------------------")
        print("Retrying with find() of string")
        print("<------------------------------->")
        #absolutePosition = context.find(bodyString)
        #absolutePosition=absolutePosition+1
        absolutePosition = re.search(bodyString, context)
        absolutePosition = absolutePosition.start() + 1

    ans.append({"text": bodyString, "answer_start": absolutePosition})
    ans.append({"text": bodyString, "answer_start": absolutePosition})
    ans.append({"text": bodyString, "answer_start": absolutePosition})
    ans.append({"text": bodyString, "answer_start": absolutePosition})

    question.append({"question": headerString, "id": idcounter, "answers": ans, "is_impossible": False})
    idcounter = idcounter + 1
    ans = list()

qas.append({"qas": question, "context": context})
# titlePara = {"title": "TK", "paragraphs": t}
titlePara = {"title": "TK", "paragraphs": qas}

tt = list()
tt.append(titlePara)

test = {"version": "v2.0", "data": tt}

with open("oneContextTrain.json", "w") as new_b:
    json.dump(test, new_b, indent=1, separators=(',', ': '), ensure_ascii=False)
