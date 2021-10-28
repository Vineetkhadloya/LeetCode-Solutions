# Python3 program to find minimum
# number of denominations

def findMin(V):
	
	# All denominations of Indian Currency
	deno = [0.05, 0.10, 0.25, 1, 5, 10, 20, 0.01, 50, 100]
	n = len(deno)
	deno.sort()
	# Initialize Result
	ans = []

	# Traverse through all denomination
	i = n - 1
	while(i >= 0):
		
		# Find denominations
		while (V >= deno[i]):
			V -= deno[i]
			ans.append(deno[i])

		i -= 1

	# Print result
	for i in range(len(ans)):
		print(ans[i])

# Driver Code
if __name__ == '__main__':
	n = 100.06
	print("Following is minimal number of change for", n)
	findMin(n)
	
# This code is contributed by
# Surendra_Gangwar
