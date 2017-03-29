from __future__ import division
import pandas as pd
import csv

lablval={}
col={}
data=[]
s_data={}
result={}
global val
val=['empty']

def diff_lablval(value):
    valfound=0
    for x in lablval:
        if(x==value):
            valfound=1
    if(valfound==0):
        lablval[value]=1
    else:
        lablval[value]+=1
        
def diff_value(values):
    already=0
    for index in val:
        if(index==values):
            already=1
    if(already==0):
        val.append(values)

#function prompts the user to enter values for the attributes. entering invalid values crasjhes the program abruptly        
def get_attr_data(prediction_value):
    for key in col:
        attribute_no=1
        if(key!=prediction_value):
            for i in range(0,end):
                diff_value(data[i][col[key]])
            del val[0]
            for fields in val:
                print('%d. %s'%(attribute_no,fields))
                attribute_no+=1
            what_data=int(input(' >> For attribute col - %s ,(Enter no) : '%(col[key])))
            s_data[col[key]]=val[what_data-1]
            del val[:]
            val.append('empty')
            print("\n")
            
#choose predictor attribute            
def choose_predictor():
    global classval
    classval=int(input(' >> Choose the column you want to predict, (please enter the number(1,2,3...) besides your choice):'))
    print(' \n >> Predictor Attribute column : %s  '%(col[classval]))
    global end
    end=len(data)
    for i in range(0,end):
        diff_lablval(data[i][col[classval]])
    print("\nPLEASE INSERT ATTRIBUTE VALUES FOR EACH OF THE ATTRIBUTES ( ENTER THE KEY NUMBER CORRESPONDING TO ATTRIBUTE VALUE ):")
    get_attr_data(classval)

#probability calculation       
def find_prob(sample,classes):
    for c in col:
        if(sample==col[c]):
            index = c
    k=0
    for i in range(0,end):
        if(s_data[sample]==data[i][col[index]] and classes==data[i][col[classval]]):
            k+=1
    return k

#find maximum value of class labels
def find_max(vall):
     v=list(vall.values())
     k=list(vall.keys())
     return k[v.index(max(v))]

#perform laplcaian smoothing and probability calculation
def laplacian_smooth(flag):
    calc=[]
    for values in probability_dictionary:
        for classes in lablval:
            if(flag==True):
                lap_value=probability_dictionary[values][classes]+1
                lap_div=lablval[classes]+1
            else:
                lap_value=probability_dictionary[values][classes]
                print("lapvalue",lap_value);
                lap_div=lablval[classes]
                print("lapdiv",lap_div);
            probability=(lap_value/lap_div)
            print("prob",probability);
            probability_dictionary[values][classes]=probability
    for classes in lablval:
        del calc[:]
        total=0
        for values in probability_dictionary:
            calc.append(probability_dictionary[values][classes])
        for i in range(0,len(calc)):
            if(i==1):
                total=calc[i]*calc[i-1]
            if(i>1):
                total=calc[i]*total
        if(flag==True):
            lap_total=end+1
            lap_class=lablval[classes]+1
        else:
            lap_total=end
            lap_class=lablval[classes]
        total=total*(lap_class/lap_total)
        print("total",total);
        result[classes]=total
        print(result)
    res=find_max(result)
    print(res);
    return res
#print dictionary table 
def print_table(dict):
    df = pd.DataFrame(dict).T
    df.fillna(0, inplace=True)
    print(df)
#read a file and make call to other methods
def compute():
    print('\n**************************************************\n')
    print('* SIMPLE NAIVE BAYES IMPLEMENTATION               *\n')
    print('**************************************************\n')

    with open('buycomp.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        sr_no=1
        for row in reader:
            #print('%s'%(row))
            data.append(row)
            sr_no+=1
    print('\nDATA FILE CONTENTS :\n')
    print(pd.DataFrame(data,index=list(range(1,len(data)+1))))
    print('\nPLEASE SELECT A PREDICTOR COLUMN: \n')
    no_2=1
    for key in data[0]:
        print('%d. %s'%(no_2,key))
        col[no_2]=key
        no_2+=1
    choose_predictor()
    global probability_dictionary
    laplacian=False
    probability_dictionary={}
    for samples in s_data:
        temp_dict={}
        for classes in lablval:

            prob=find_prob(samples,classes)
            temp_dict[classes]=prob
        probability_dictionary[samples]=temp_dict
    print('\nCHOOSE ATTRIBUTE VALUES FOR THE FOLLOWING ATTRIBUTES: \n')
    for s in s_data:
        print(' >> %s :  %s'%(s,s_data[s]))
    
    print('\nFREQUENCY TABLE FOR THE ATTRIBUTES : \n')
    print_table(probability_dictionary)
    for prob in probability_dictionary:
        for classes in lablval:
            if(probability_dictionary[prob][classes]== 0):
                laplacian=True
    print("\nLAPLACIAN SMOOTHING AND PROBABILITY calcS: \n")
    if(laplacian==True):
        print('>> Applying Laplacian Smoothing.(Laplacian Smoothing = True)\n')
        lap=True
        predicted_val=laplacian_smooth(lap)
    else:
        lap=False
        predicted_val=laplacian_smooth(lap)
    print("\n PROBABILITY OF CLASS OCCURING: \n")
    print_table(probability_dictionary)
    return predicted_val
#main function which calls compute to     
if __name__=="__main__":
    res=compute()
    print(res);
    print('\n************************* FINAL PROBABILITY FOR THE PREDICTORS *************************\n')
    for i in result:
        print(' >> %s  : %s '%(i,result[i]))
    print('\n PREDICTION USING NAIVE BAYES CLASSIFER IS, %s = %s'%(col[classval],res))
    print('\n\n\n');