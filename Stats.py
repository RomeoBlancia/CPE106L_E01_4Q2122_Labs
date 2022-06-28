def mean(arr):
    if len(arr)==0:
        return 0
    return sum(arr)/len(arr)
def median(arr):
    if len(arr)==0:
        return 0
    arr.sort()
    n=len(arr)
    if n%2==0:
        return (arr[n//2]+arr[n//2-1])/2
    else:
        return arr[n//2]
def mode(arr):
    if len(arr)==0:
        return 0
    cnt=0
    md=0
    arr.sort()
    for i in arr:
        if arr.count(i)>cnt:
            cnt=arr.count(i)
            md=i
    return md
def main():
    arr=[1,2,3,4,1,2,3,4,1,2,1,3]
    print("Mean:",mean(arr))
    print("Median:",median(arr))
    print("Mode:",mode(arr))
main()



