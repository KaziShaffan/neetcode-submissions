import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_nums = {}

        for i in nums:
            if(i in hash_nums.keys()):
                hash_nums[i] += 1
            else:    
                hash_nums[i] = 1

        heap_nums = []
        print(hash_nums)
        for j in hash_nums.keys():
            heapq.heappush(heap_nums, (hash_nums[j], j))
            if(len(heap_nums) > k):
                heapq.heappop(heap_nums)

        print(heap_nums)
        ans = []
        for i in heap_nums:
            ans.append(i[1])
            print(ans)
            

        
            
        return ans
            