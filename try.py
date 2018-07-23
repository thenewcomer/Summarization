from pprint import pprint

'''
from evaluation import evaluate as evaluate_final

f = open('result_label.txt', "r")
lines = f.readlines()
label_list = []
prediction_list = []
for line in lines:
    label_list.append(line.split(" ")[1])
    prediction_list.append(line.split(" ")[3].rstrip())
evaluate_final(prediction_list, label_list)
'''
out=[['%-6s'%'Label']+[('%6s'%lab) for lab in ['N_correct','N_present','N_predict','Precision','Recall','F1']]]
print(out)