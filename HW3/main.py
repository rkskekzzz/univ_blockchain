from utils.scan import scanning
from utils.scan import getRange
from utils.scan import combineTarget
import argparse

def args():
	# Requried
	# 프로세스 실행 시 옵션으로 target을 지정할 수 있다.
	# 옵션 사용 방법
	# ex) python main.py -t 127.0.0.1 -tr 127.0.0.20
	parser = argparse.ArgumentParser(description='portscannder like nmap')
	# -t 옵션은 필수로 넣어주어야 프로세스가 실행된다. 하나의 타겟을 대상으로 할 때에는 -t 옵션만 지정하면 된다.
	parser.add_argument('--target', '-t', required=True, help='port scanning with target address')
	# -tr 옵션은 -t 옵션과 함께 사용된다. -t 옵션부터 -tr 옵션 범위까지의 주소 범위에 대해 동작한다.
	parser.add_argument('--target-range', '-tr', required=False, help='scanning the range between the target and the target-range option')

	# 옵션으로 입력받은 값을 객체에 담에 리턴한다.
	return  parser.parse_args()


# 프로그램 시작할 때 메인실행
if __name__ == "__main__":
	# 프로그램 설명
	print("\033[34mPort Scanning like nmap!\033[m")
	print("scanning port range : 0 to 1023")

	# 옵션 파싱해서 args에 받아온다.
	args = args()

	# args.target_range 옵션에 값이 들어왔을 때 (범위로 스캔할 떄)
	if args.target_range:
		print("\033[34mTarget Range\033[m")
		print(args.target, " ... ", args.target_range)

		# 시작할 범위와 끝날 범위를 가져온다.
		start, end = getRange(args)

		# 계산한 범위를 돌면서 스캔을진행한다.
		for addr in range(start, end):
			# 스캐닝 함수에서 포트 스캐닝을 진행한다.
			scanning(combineTarget(args, addr))

	# args.target_range에 값이 들어오지 않았을 때 (하나의 주소만 스캔할 때)
	else:
		print("\033[34mTarget\033[31m")
		print(args.target)

		# 하나의 타겟에 대해 스캐닝을 진행한다.
		scanning(args.target)

	print("\033[34mDone 😀\033[30m")
