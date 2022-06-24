
def mode(lyst):
    lyst.sort() 
    list_elem = dict()
    for i in lyst:
        
        list_elem[i] = list_elem.get(i, 0) + 1
    
    return max(list_elem, key=list_elem.get)

def median(lyst):
    lyst.sort() 
    return lyst[int(len(lyst)/2)]

def mean(lyst):
    sum=0 
 
    for i in range(0,len(lyst)):
        sum=sum+lyst[i] 
    
    return sum/len(lyst)

def main():
    lyst=[27,5,18,66,12,5,9]
    print("List:",lyst)
    print("Mode:",mode(lyst))
    print("Median:",median(lyst))
    print("Mean:",mean(lyst))

if __name__=="__main__":
    main() 