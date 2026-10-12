"""
Given an integer array nums of size n. Return all elements which appear more than n/3 times in the array. 
The output can be returned in any order.
"""

def majorityElementTwo(nums)->list:
    n=len(nums)
    ele1=-1
    ele2=-1
    cnt1=cnt2=0
    for i in nums:
        if ele1==i:
            cnt1+=1
        elif ele2==i:
            cnt2+=1
        elif cnt1==0:
            ele1=i
            cnt1+=1
        elif cnt2==0:
            ele2=i
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
    cnt1=cnt2=0
    for i in nums:
        if ele1==i:
            cnt1+=1
        elif ele2==i:
            cnt2+=1
    res=[]
    if cnt1>n//3:
        res.append(ele1)
    if cnt2>n//3 and ele1!=ele2:
        res.append(ele2)
    if len(res)>2 and res[0]>res[1]:
        res[0],res[1]=res[1],res[0]
    return res

if __name__ == "__main__":
    arr = [1, 2, 1, 1, 3, 2]
    print(majorityElementTwo(arr))