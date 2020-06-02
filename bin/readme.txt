테스트 환경이 32비트이면 x86, 64비트이면 x64 디렉터리를 사용하면 된다.
테스트 환경에 맞는 디렉터리를 선택했다면 아래의 순서대로 테스트를 수행한다.

1. scanner_kicomav 를 빌드한다.
2. scanner.sys, scanuser.exe 빌드 결과물을 kavcore 디렉터리와 같은 위치에 복사한다.
3. scanner.inf 설치파일을 kavcore 디렉터리와 같은 위치에 복사한다.
4. scanner.inf 설치파일을 선택하고 오른쪽 마우스 버튼을 클릭하여 '설치'를 클릭한다.
5. 관리자 권한으로 command 창을 실행한 후 아래의 명령을 입력하여 드라이버를 로드한다.
   sc start scanner
6. 관리자 권한을 가지는 command 창에서 scanuser.exe 를 실행한다.
7. eicar.com 파일을 command 창에서 실행하여 테스트한다.
8. scanuser.exe가 실행중일 때와 그렇지 않을 때 eicar.com 파일의 실행 결과를 비교한다.