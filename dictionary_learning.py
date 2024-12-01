from datetime import date

recordid = int(1)
balancedue = float(740.45)
duedate = date(2024, 12, 31)
monthlypayment = float(100.42)
runningtotal = float(200.84)

recordid2 = int(2)
balancedue2 = float(740.45)
duedate2 = date(2025, 1, 31)
monthlypayment2 = float(100.42)
runningtotal2 = float(200.84 + 100.42)


newdict = {
    "Record ID" : recordid,
    "Balance Due" : balancedue,
    "Due Date" : duedate,
    "monthly payment" : monthlypayment,
    "Running Total" : runningtotal

}

newdict.update({
    "Record ID" : recordid2,
    "Balance Due" : balancedue2,
    "Due Date" : duedate2,
    "monthly payment" : monthlypayment2,
    "Running Total" : runningtotal2
})

print("Naked dictionary print:")
print(newdict)
print("_________________________________________________")

def printTable(myDict, colList=None):
    if not colList: 
        colList = list(myDict[0].keys() if myDict else [])
    myList = [colList] # 1st row = header
    for item in myDict: 
        myList.append([str(item[col] or '') for col in colList])
    #maximun size of the col for each element
    colSize = [max(map(len,col)) for col in zip(*myList)]
    #insert seperating line before every line, and extra one for ending. 
    for i in  range(0, len(myList)+1)[::-1]:
         myList.insert(i, ['-' * i for i in colSize])
    #two format for each content line and each seperating line
    formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
    formatSep = '-+-'.join(["{{:<{}}}".format(i) for i in colSize])
    for item in myList: 
        if item[0][0] == '-':
            print(formatSep.format(*item))
        else:
            print(formatStr.format(*item))

printTable([newdict])
