#Subsets
nums = [1,2,3]

def subsets(nums):
        result = []
        subset = []

        def create_subset(i):
            if i == len(nums):
                result.append(subset[:])
                return
            subset.append(nums[i])
            create_subset(i+1)
            subset.pop()
            create_subset(i+1)
        create_subset(0)
        return result

print(subsets(nums))