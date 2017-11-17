def check_palindrome(s, i):
	print(s[i])
	if i == len(s)/2 and s[i] == s[len(s)/2]:
		return True
	if s[i] == s[len(s)-i-1]:
		check_palindrome(s, i+1)
	return False

if (check_palindrome("sator arepo tenet opera rotas", 0)):
	print("Palindrome!")
else:	
	print("No palindrome!")
