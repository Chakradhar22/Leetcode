
class Solution:
    def trappingWater(self, height,n):
        #Code here
        l,r,lmax,rmax,area=0,len(height)-1,0,0,0
        while l<r:
            if height[l]>height[r]:
                if height[r]>rmax:
                    rmax=height[r]
                else:
                    area+=rmax-height[r]
                r-=1
            else:
                if height[l]>lmax:
                    lmax=height[l]
                else:
                    area+=lmax-height[l]
                l+=1
        return area


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends