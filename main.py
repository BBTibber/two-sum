from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:

    for i in range(0,len(nums)-1):
       for j in range(i+1,len(nums)):
            if int(int(nums[i])+int(nums[j])) == int(target) :
                print("Output:[",i,",",j,"]")
                return


def main():
    arr = input("Input : nums = ")
    arr = arr[1:len(arr)-1]
    arr = arr.split(',')
    tar = input("target = ")

    twoSum(arr,tar)
    return

if __name__=='__main__':
    main()