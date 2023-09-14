from pdf2image import convert_from_path
import os

# Poppler의 경로 설정
poppler_path = r'C:\poppler-23.08.0\Library\bin'  # 여기에 실제 Poppler 설치 경로를 지정합니다.

# PDF 파일이 있는 디렉토리 경로
pdf_dir = 'your_directory'

# JPG 이미지를 저장할 디렉토리 경로
jpg_dir = 'your_directory'

# Poppler의 경로를 환경 변수에 설정
os.environ["PATH"] += os.pathsep + poppler_path

# PDF 디렉토리에 있는 모든 PDF 파일 목록 가져오기
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

# 각 PDF 파일을 이미지로 변환하여 저장
for pdf_file in pdf_files:
    # PDF 파일의 확장자를 추출하여 제거
    pdf_filename_without_extension = os.path.splitext(pdf_file)[0]

    pdf_path = os.path.join(pdf_dir, pdf_file)
    images = convert_from_path(pdf_path)

    # 이미지를 jpg_dir에 저장하고 새로운 파일명으로 지정
    for i, image in enumerate(images):
        jpg_filename = f"{pdf_filename_without_extension}_{i + 1}.jpg"
        jpg_path = os.path.join(jpg_dir, jpg_filename)
        image.save(jpg_path, 'JPEG')
