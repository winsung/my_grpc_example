1. 가상환경 설정 및 필요 패키지 설치
 > $ python -m pip install virtualenv
 > $ virtualenv venv python=python3.6
 > $ source venv/bin/activate
 > $ pip install -r requirements.txt

2. gRPC 통신을 위한 .proto compile
 - 이미 컴파일 해놓은 파일이 있으나 새로 컴파일 필요시 아래의 명령 사용
 > $ sh make_proto.sh

3. 서버 구동
 > $ python server.py

4. 테스트용 클라이언트 구동
 > $ python client.py

--------------
파일 설명
--------------
 - lbs.proto : gRPC 를 위한 proto 파일
 - lbs_pb2.py : proto 컴파일하여 gRPC 통신에 사용되는 객체 정보
 - lbs_pb2_grpc.py : proto 컴파일 gRPC 통신에 사용되는 함수 정보
 - server.py : gRPC 서비스 구현하여 서버 가동
 - memory_db.py : 실제로 서비스의 실행이 구현
 - utility.py : 이진 탐색과 범위내 탐색 등을 구현하기 위한 유틸리티 모음
 - client.py : server 통신을 해보기 위한 임시 클라이언트
 - lbs_db.json : 프로그램 중지 상황에 대응하기 위한 차량정보 저장 파일 ()
