def countWords(s):
	if s.strip() == "":
		return 0
	words = s.split()
	return len(words)
if _name_ == "_main_":
	s = input("enter the string")
	print("No of words : ", countWords(s))
