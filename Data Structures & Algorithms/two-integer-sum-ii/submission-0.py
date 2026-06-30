class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binary_search(i: int, search: int):
            left = i + 1
            right = len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == search:
                    return [i+1, mid+1]
                
                elif numbers[mid] > search:
                    right = mid - 1

                else:
                    left = mid + 1
            
            else:
                return [-1, -1]

        
        for i in range(len(numbers)):
            indices = binary_search(i, target - numbers[i])
            # some logic to check for valid answer
            if indices!= [-1, -1]:
                # return valid answer
                return indices
        return [-1,-1]