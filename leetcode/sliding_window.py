# Problem: Longest Subarray With At Most K Odd Numbers

# Given an array of integers nums and an integer k, return the length of the
# longest contiguous subarray that contains at most k odd numbers.


def oddNumbers(nums: list[int], k):
    i = 0

    currentOddCount = 0
    maxLength = 0

    for j in range(len(nums)):
        if nums[j] % 2 == 1:
            currentOddCount += 1

        while currentOddCount > k:
            if nums[i] % 2 == 1:
                currentOddCount -= 1

            i += 1

        maxLength = max(maxLength, j - i + 1)

    return maxLength


def distinctCharacters(s: str, k: int):
    i = 0
    freq = dict()

    numDistinct = 0

    maxL = 0

    for j in range(len(s)):
        if s[j] not in freq or freq[s[j]] == 0:
            numDistinct += 1

        freq[s[j]] = freq.get(s[j], 0) + 1

        while numDistinct > k:
            freq[s[i]] -= 1

            if freq[s[i]] == 0:
                numDistinct -= 1

            i+= 1

        maxL = max(maxL, j - i + 1)

    return maxL

def minWindowSubstring(s: str, t: str):

    tfreq = dict()

    for c in t:
        tfreq[c] = tfreq.get(c, 0) + 1
    
    i = 0
    sfreq = dict()
    formed = 0
    minL = float('inf')
    for j in range(len(s)):

        sfreq[s[j]] = sfreq.get(s[j], 0) + 1

        if sfreq[s[j]] == tfreq.get(s[j],0):
            formed += 1
        
        while formed == len(tfreq):

            minL = min(minL, j - i + 1)

            if s[i] in tfreq and sfreq[s[i]] == tfreq[s[i]]:
                formed -= 1
            
            sfreq[s[i]] -= 1
            i += 1
        
    return minL
    
from queue import PriorityQueue
def longestRepeatingCharReplacement(s: str, k: int):

    i = 0
    
    longestWindow = 0

    freq = dict()
    currentMaxChar = None

    for j in range(len(s)):

        freq[s[j]] = freq.get(s[j], 0) + 1

        if currentMaxChar is None:
            currentMaxChar = s[j]
        
        if freq[currentMaxChar] < freq[s[j]]:
            currentMaxChar = s[j]
        
        while j - i + 1 - freq[currentMaxChar] > k:

            freq[s[i]] -= 1

            if s[i] == currentMaxChar:
                currentMaxChar = max([c for c in freq], key=lambda r: freq[r])

            i += 1
        
        longestWindow = max(j - i + 1, longestWindow)


    return longestWindow



def minEatingSpeed(self, piles: list[int], h: int):

    def canFinishAll(piles: list[int], k: int, h: int):
        totalHours = 0
        for p in piles:
            if p % k == 0:
                totalHours += p // k
            else:
                totalHours += p // k + 1

        return totalHours <= h

    l = 1
    r = 1

    while not canFinishAll(piles, r, h):
        r *= 2
    

    while l < r:

        m = (l + r) // 2

        if canFinishAll(piles, m, h):
            r = m
        else:
            l = m + 1
    
    return l


def shipWithinDays(self, weights: list[int], days: int):

    def canShip(days: int, maxWeight):

        totalWeight = 0
        totalDays = 1
        for w in weights:

            if totalWeight + w > maxWeight:
                totalDays += 1
                totalWeight = w
            else:
                totalWeight += w


        return totalDays <= days


    l = max(weights)
    r = sum(weights)

    while l < r:

        m = (l +r ) // 2

        if canShip(days, m):
            r = m
        else:
            l = m + 1

    return l


def splitArray(self, nums: list[int], k: int):

    def canSplit(T: int):

        count = 1
        total = 0
        for n in nums:

            if total + n > T:
                count += 1
                total = n
            else:
                total += n

        
        return count <= k


    l = 0
    r = sum(nums)

    while l < r:
        m = (l + r) // 2

        if canSplit(m):
            r = m
        else:
            l = m + 1

    return l



def minDays(bloomDay: list[int], m: int, k: int):

    def canMake(day: int):

        i = 0
        boquets = 0
        for j in range(len(bloomDay)):
            

            if bloomDay[j] > day:
                i = j
                continue

            if j - i + 1 == k:
                boquets += 1
                i = j + 1
                continue
        
        return boquets >= m
            

    l = min(bloomDay)
    r = max(bloomDay)

    while l < r:

        mid = (l + r)//2

        if canMake(mid):
            r = mid
        else:
            l = mid + 1

    return l

print(minDays([1,10,3,10,2], 3, 1))































    

