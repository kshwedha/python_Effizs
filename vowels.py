# Python3 program to count permutations of 
# string such that no two vowels are adjacent 

# Factorial of a number 
def factorial(n) : 

	fact = 1; 
	for i in range(2, n + 1) : 
		fact = fact * i 

	return fact 

# Function to find c(n, r) 
def ncr(n, r) : 
	
	return factorial(n) // (factorial(r) *
							factorial(n - r)) 

# Function to count permutations of string 
# such that no two vowels are adjacent 
def countWays(string) : 

	freq = [0] * 26
	nvowels, nconsonants = 0, 0

	# Finding the frequencies of 
	# the characters 
	for i in range(len(string)) : 
		freq[ord(string[i]) - ord('a')] += 1

	# finding the no. of vowels and 
	# consonants in given word 
	for i in range(26) : 

		if (i == 0 or i == 4 or i == 8
			or i == 14 or i == 20) : 
			nvowels += freq[i] 
		else : 
			nconsonants += freq[i] 
	
	# finding places for the vowels 
	vplaces = nconsonants + 1

	# ways to fill consonants 6! / 2! 
	cways = factorial(nconsonants) 
	for i in range(26) : 
		if (i != 0 and i != 4 and i != 8 and
			i != 14 and i != 20 and freq[i] > 1) : 

			cways = cways // factorial(freq[i]) 

	# ways to put vowels 7C5 x 5! 
	vways = ncr(vplaces, nvowels) * factorial(nvowels) 
	for i in range(26) : 
		if (i == 0 or i == 4 or i == 8 or i == 14
			or i == 20 and freq[i] > 1) : 
			vways = vways // factorial(freq[i]) 

	return cways * vways; 

# Driver code 
if __name__ == "__main__" : 

	string = "permutation"

	print(countWays(string)) 

# This code is contributed by Ryuga 

