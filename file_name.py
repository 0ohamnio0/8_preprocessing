import pandas as pd
import os

# 엑셀 파일 경로 설정 (한글 경로 포함)
excel_file_path = r"D:\8\기초단체장재보궐선거.xlsx"

# 엑셀 파일에서 파일명과 새 파일명을 읽어오기
df = pd.read_excel(excel_file_path)

# 이미지 파일이 있는 디렉토리 경로 설정
image_dir = r"D:\8\8_hei\gicho_danche_again\crop\remove"

# 파일명을 엑셀 레이블 순서대로 변경
for index, row in df.iterrows():
    old_file_name = os.path.join(image_dir, row['현재_파일명'] + ".jpg")
    new_file_name = os.path.join(image_dir, row['새_파일명'] + ".jpg")  # 확장자 추가

    # 파일명 변경
    try:
        os.rename(old_file_name.encode('utf-8').decode('utf-8-sig'), new_file_name.encode('utf-8').decode('utf-8-sig'))
        print(f"{old_file_name}을(를) {new_file_name}으로 변경했습니다.")
    except FileNotFoundError:
        print(f"경로에 해당 파일이 없습니다: {old_file_name}")
    except FileExistsError:
        print(f"이미 같은 이름의 파일이 존재합니다: {new_file_name}")

print("작업 완료")
