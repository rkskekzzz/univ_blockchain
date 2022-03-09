cipherText = "RVJZJSRJVUFERUVJZXEGIZETZGCVBEFNERJRJLSJKZKLKZFEGVIDLKRKZFEEVKNFIBREUZJVWWZTZVEKZESFKYJFWKNRIVREUYRIUNRIV"
asciiOfE = ord("E")

def asciiToChr(ch, diff):
	result = (ord(ch) - diff - 65) % 26 + 65
	return result

def makeDictionaryWithCipherText():
	resultDic = {}
	for ch in cipherText:
		if ch in resultDic:
			resultDic[ch] += 1
		else:
			resultDic[ch] = 1
	return resultDic

def sortDictinaryByValue(srcDic):
	return  sorted(srcDic.items(), key = lambda item: item[1], reverse = True)

def decryptText(sortedArr):
	for index, (key, elem) in enumerate(sortedArr):
		diff = ord(key) - asciiOfE
		for ch in cipherText:
			print(chr(asciiToChr(ch, diff)), end="")
		print()
		if index >= 4:
			break

cipherTextCharacterCountArr = makeDictionaryWithCipherText()
sortedArr = sortDictinaryByValue(cipherTextCharacterCountArr)
decryptText(sortedArr)

print("\n<Most Meaningful Text> \nAESIS BASED ON A DESIGN PRINCIPLE KNOW NASA SUBSTITUTION PERMUTATION NETWORK AND IS EFFICIENT IN BOTH SOFTWARE AND HARDWARE")
