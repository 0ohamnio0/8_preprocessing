import os
import io
from rembg import remove

# 입력 이미지가 있는 디렉토리 경로
input_image_dir = r'your_directory'

# 출력 이미지를 저장할 디렉토리 경로
output_image_dir = r'your_directory'

# 출력 디렉토리 생성
os.makedirs(output_image_dir, exist_ok=True)

# 입력 디렉토리에서 이미지 파일 목록 가져오기
image_files = [f for f in os.listdir(input_image_dir) if f.endswith('.jpg')]

for image_file in image_files:
    # 이미지 파일 경로
    input_image_path = os.path.join(input_image_dir, image_file)

    # 출력 이미지 경로
    output_image_path = os.path.join(output_image_dir, image_file)

    # 이미지 파일 열기
    with open(input_image_path, "rb") as input_file:
        input_data = input_file.read()

    # 배경 제거
    output_data = remove(input_data)

    # 출력 이미지 파일로 저장
    with open(output_image_path, "wb") as output_file:
        output_file.write(output_data)

    print(f"{image_file} 처리 완료")

print("모든 이미지 처리 완료")
