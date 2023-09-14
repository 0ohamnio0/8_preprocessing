import os
import io
from rembg import remove
from PIL import Image, ImageFilter

# 입력 이미지가 있는 디렉토리 경로
input_image_dir = r'D:\8\8_hei\guangyuk_danche\crop'

# 출력 이미지를 저장할 디렉토리 경로
output_image_dir = r'D:\8\8_hei\guangyuk_danche\result_2'

# 출력 디렉토리 생성
os.makedirs(output_image_dir, exist_ok=True)

# 입력 디렉토리에서 이미지 파일 목록 가져오기
image_files = [f for f in os.listdir(input_image_dir) if f.endswith('.jpg')]

# 원하는 이미지 크기
desired_size = (256, 256)

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

    # PIL Image로 변환
    output_image = Image.open(io.BytesIO(output_data))

    # 이미지 모드가 RGBA인 경우 RGB로 변환
    if output_image.mode == "RGBA":
        output_image = output_image.convert("RGB")

    # 이미지 크기 변경 (BILINEAR 필터 사용)
    output_image = output_image.resize(desired_size, Image.BILINEAR)

    # 이미지를 파일로 저장 (jpg 형식)
    output_image.save(output_image_path, "JPEG")

    # 파일 확장자를 jpg로 변경
    new_output_image_path = os.path.splitext(output_image_path)[0] + ".jpg"
    os.rename(output_image_path, new_output_image_path)

    print(f"{image_file} 처리 완료")

print("모든 이미지 처리 완료")
