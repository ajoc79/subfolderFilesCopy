# subfolderFilesCopy
하위 모든 파일들 복사

사용법 : /folder/ 밑 모든 파일들을 현재 디렉토리 (.)에 전부 복사

python .\copyfiles.py --sf .\folder\ --df .




# 이름 일괄변경
1. vi rename.sh

  #!/bin/sh
  for f in *.mp4.!qB; do
    mv "$f" "${f/.mp4.!qB/.mp4}"
  done

2. i 누르고 입력 후 Esc → :wq
3. 실행 권한 부여
   chmod +x rename.sh
   ./rename.sh
