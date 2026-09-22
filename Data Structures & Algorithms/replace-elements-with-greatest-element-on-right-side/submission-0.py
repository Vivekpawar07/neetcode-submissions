class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_great = -1900029202920239

        for i in range(len(arr)):
            curr_great = -1
            for j in range(i+1,len(arr)):
                if arr[j] > curr_great:
                    curr_great = arr[j]
            
            arr[i]= curr_great

        return arr
