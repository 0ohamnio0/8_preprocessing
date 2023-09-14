import pandas as pd

# 엑셀 파일 경로 설정 (한글 경로 포함)
excel_file_path = r"your_directory/excel_file.xlsx"

# 엑셀 파일 읽어오기
df = pd.read_excel(excel_file_path)

# 모든 텍스트에서 | 기호 제거
df = df.applymap(lambda x: str(x).replace('|', ' '))

# 새로운 엑셀 파일 생성 (기존 파일 덮어쓰기)
with pd.ExcelWriter(excel_file_path) as writer:
    df.to_excel(writer, index=False, header=False)

print("텍스트에서 | 기호를 제거하고 엑셀 파일을 저장했습니다.")
