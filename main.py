import numpy as np
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def threeSum(nums):
    myList = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k] == 0:
                    list = [nums[i], nums[j], nums[k]]
                    myList.append(list)
    return hashDups(myList)

def hashDups(lists):
    myDict = {}
    for i in range(len(lists)):
        newTuple = tuple(sorted(lists[i]))
        myDict.update({newTuple: i})
    return myDict.keys()



if __name__ == '__main__':
    practice = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    print(threeSum(practice))
