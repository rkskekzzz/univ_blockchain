import socket

# 포트 범위의 최소값과 최대값을 지정
minPort = 0
maxPort = 1024
# maxPort = 65535

# 스캐닝 함수
def scanning(target):
	print("\033[32m[ Start : ", target, "]\033[0m")
	# 포트 범위만큼 루프를 돌면서 스캔한다.
	for port in range(minPort, maxPort):
		try:
			# 소캣 fd를 새로 생성한다. with구문을 활용해서 스코프가 끝나면 자동으로 생성된 fd 가 닫힐 수 있도록 한다.
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as sock:
				# socket의 죽는 시간을 설정
				sock.settimeout(0.5)
				# target 과 port 를 활용해서 연결을 시도한다.
				# 연결이 되지 않으면 except로 빠진다.
				sock.connect((target, port))
				# 연결이 되면 아래 출력 문구를 출력한다.
				print("Port ", port, " open!")
		# 에러가 발생하면 아무런 동작을 하지않고 다음 동작을 진행한다.
		except: pass



# 주소 범위를 연산해주는 함수
def getRange(args):
	# ip주소의 마지막 8바이트 숫자범위를 리턴해준다.
	return int(args.target.split('.')[3]), int(args.target_range.split('.')[3])

# 주소 범위를 합쳐주는 함수
def combineTarget(args, addr):
	# 현재 스캔할 범위를 활용해 주소를 합쳐준다.
	return args.target.split('.')[0] + "." + args.target.split('.')[1] + "." + args.target.split('.')[2] + "." + str(addr)
