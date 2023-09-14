from pdf2image import convert_from_path
from pdf2image.exceptions import PDFInfoNotInstalledError
import os

# PDF 파일이 있는 폴더 경로 설정
pdf_folder = "your_directory"  # PDF 파일들이 있는 폴더 경로
output_folder = "your_directory"  # 이미지를 저장할 폴더 이름

# PDF 폴더 내의 모든 PDF 파일 가져오기
pdf_files = [os.path.join(pdf_folder, file) for file in os.listdir(pdf_folder) if file.endswith(".pdf")]

# PDF 파일 목록을 순회하면서 변환
for pdf_file_path in pdf_files:
    try:
        # 이미지로 변환할 PDF 파일 읽기 (ImageMagick 사용)
        images = convert_from_path(pdf_file_path)

        # 저장 폴더가 없는 경우 생성
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # 각 페이지 이미지를 저장
        for i, image in enumerate(images):
            # 원래 PDF 파일명을 기반으로 JPG 파일명 생성
            pdf_filename = os.path.basename(pdf_file_path)
            pdf_filename_without_extension = os.path.splitext(pdf_filename)[0]
            jpg_file_path = os.path.join(output_folder, f"{pdf_filename_without_extension}_page_{i+1}.jpg")

            # JPG 이미지로 저장
            image.save(jpg_file_path, "JPEG")

        print(f"{pdf_file_path}를 JPG 이미지로 변환 및 저장 완료.")
    except PDFInfoNotInstalledError as e:
        print(f"{pdf_file_path}를 이미지로 변환할 수 없습니다. 에러 메시지: {e}")

print("모든 PDF를 JPG 이미지로 변환 및 저장 완료.")
