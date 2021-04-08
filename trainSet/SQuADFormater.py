import json
import numpy as np
import uuid
import array as arr








with open("data3.json") as b:
    b = json.load(b)

#tmp={"version":"v2.0", "data":{"title":"TK", "paragraphs":{"qas":{"question":"","id":"","answers":{"text":"","answer_start":0},"is_impossible":False},"context":""}}}
#tmp={"title":"TK", "paragraphs":{"qas":{"question":"","id":"","answers":{"text":"","answer_start":0},"is_impossible":False},"context":""}}

t = list()
idcounter=0

data = list()
ans=list()
qas = list()
for qa in b:
    print(qa["header"])
    print(qa["body"])


    question = {"question":qa["header"],"id":idcounter,"answers":ans,"is_impossible":False}

    qas.append({"qas":question,"context":qa["body"]})

    idcounter=idcounter+1

ans.append({"text":"","answer_start":0})

#titlePara = {"title": "TK", "paragraphs": t}
titlePara = {"title": "TK", "paragraphs": qas}

tt=list()
tt.append(titlePara)

test={"version":"v2.0", "data": tt}

with open("tKSQuADFormat.json", "w") as new_b:
    json.dump(test, new_b, indent=1, separators=(',', ': '),ensure_ascii=False)

