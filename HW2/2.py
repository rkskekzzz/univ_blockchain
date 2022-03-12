import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
G = Point(0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
		  0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)

def getUserInput():
	return int(input("개인키를 입력하세요 : "))

def extendedEuclidianAlgorithm(n, b):
	r1 = n; r2 = b
	t1 = 0; t2 = 1
	while r2 > 0:
		q = math.floor(r1 / r2)

		r = r1 - q * r2
		r1 = r2; r2 = r

		t = t1 - q * t2
		t1 = t2 ; t2 = t

	if r1 != 1:
		raise Exception('역원이 없습니다')

	return t1 if t1 >= 0 else t1 + n



def addTwoCoordinate(p, q):
	def getCoordinate(incl):
		x = (incl ** 2 - p.x - q.x) % n
		y = (incl * (p.x - x) - p.y) % n
		return Point(x, y)
	if p == q:
		incl = (3 * p.x ** 2) * extendedEuclidianAlgorithm(n, 2 * p.y) % n
	else:
		if q.x < p.x:
			p, q = q, p
		incl = (q.y - p.y) * extendedEuclidianAlgorithm(n, q.x - p.x) % n
	return getCoordinate(incl)

def doubleAndAddAlgorithm(k, G):
	ptr = 2 ** k.bit_length()
	res = 0
	while ptr != 0:
		if k & ptr != 0:
			res = addTwoCoordinate(addTwoCoordinate(res, res), G) if res != 0 else G
		else:
			res = addTwoCoordinate(res, res) if res != 0 else 0
		ptr = ptr >> 1
	return res


user_input = getUserInput()
res = doubleAndAddAlgorithm(user_input, G)

print(hex(res.x))
print(hex(res.y))

