'''
# A Dynamic Programming solution for subset sum problem 
# Returns true if there is a subset of 
# set[] with sun equal to given sum 

# Returns true if there is a subset of set[] 
# with sun equal to given sum 

Ref: # https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
'''
def isSubsetSum(set,n,sum): 
	
	# The value of subset[i][j] will be 
	# true if there is a 
	# subset of set[0..j-1] with sum equal to i 
	subset=([[False for i in range(sum+1)] 
			for i in range(n+1)]) 
	
	# If sum is 0, then answer is true 
	for i in range(n+1): 
		subset[i][0] = True
		
		# If sum is not 0 and set is empty, 
		# then answer is false 
		for i in range(1,sum+1): 
			subset[0][i]=False
			
		# Fill the subset table in botton up manner 
		for i in range(1,n+1): 
			for j in range(1,sum+1): 
				if j<set[i-1]: 
					subset[i][j] = subset[i-1][j] 
				if j>=set[i-1]: 
					subset[i][j] = (subset[i-1][j] or
								subset[i - 1][j-set[i-1]]) 
	
		# uncomment this code to print table 
		# for i in range(n+1): 
		# for j in range(sum+1): 
		#	 print (subset[i][j],end=" ") 
		# print() 
	return subset[n][sum] 
		
# Driver program to test above function 
if __name__=='__main__': 
	set = [10000001111, 10011110000, 1000110011, 1011001100, 101010101, 110101010,
         10000000, 20000000, 1000000, 2000000, 100000, 200000, 10000, 20000,
         1000, 2000, 100, 200, 10, 20, 1, 2]
	sum = 11144444444
	n =len(set) 
	if (isSubsetSum(set, n, sum) == True): 
		print("Found a subset with given sum") 
	else: 
		print("No subset with given sum") 
		
# This code is contributed by 
# sahil shelangia. 
