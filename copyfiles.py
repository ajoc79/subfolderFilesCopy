import argparse
import os
import shutil

def recursion(folder):
    # 폴더 안에 있는 파일들의 이름을 리스트로 가져옵니다.
    files = os.listdir(folder)

    # 만약 파일이 있다면
    if files:
        # 각 파일에 대해 반복합니다.
        for file in files:
            if os.path.isdir(os.path.join(folder, file)):
                recursion(os.path.join(folder, file))
            elif os.path.isfile(os.path.join(folder, file)):
                # 원본 파일의 전체 경로를 만듭니다.
                src = os.path.join(folder, file)
                # 대상 파일의 전체 경로를 만듭니다.
                if opt.df == ".":
                    opt.df = os.getcwd()
                dst = os.path.join(opt.df, file)
                # 파일을 복사합니다.
                shutil.copy(src, dst)
                # 메타데이터도 복사 (느리지만 원본 데이터 유지하려면 copy2 쓸것)
                # shutil.copy2(src, dst)
                # print(f'src : {src}, dest : {dst}')
            else:
                print(file)

def proecss():
    # 현재 디렉토리에서 폴더를 검색합니다.
    folders = [f for f in os.listdir(opt.sf) if os.path.isdir(os.path.join(opt.sf, f))]
    print(folders)

    # 각 폴더에 대해 반복합니다.
    for folder in folders:
        recursion(os.path.join(opt.sf, folder))


    # 복사가 완료되었음을 출력합니다.
    print("All files copied to c:\\Woosan\\Works\\aaa")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sf', type=str, default='C:\\Downloads', help='source folder')
    parser.add_argument('--df', type=str, default='c:\\Downloads\\Dest', help='dest folder')
    opt = parser.parse_args()
    proecss();
