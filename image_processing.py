import cv2
import dlib
import os
from pathlib import Path

# 이미지 파일이 있는 디렉토리 경로 설정
image_dir = Path(r"your_directory")

# Dlib의 얼굴 검출기 초기화
detector = dlib.get_frontal_face_detector()

# 디렉토리 내의 이미지 파일 목록 가져오기
image_files = list(image_dir.glob("*.jpg"))

# 얼굴을 더 크게 자를 크기 설정 (예: 얼굴 크기의 2배)
scale_factor = 2.0

for image_file in image_files:
    image = cv2.imread(str(image_file))

    # 흑백 이미지로 변환 (Dlib는 흑백 이미지를 사용합니다)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 얼굴 검출
    faces = detector(gray)

    for index, face in enumerate(faces):
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # 얼굴 영역 확대
        x -= int(w * (scale_factor - 1) / 2)
        y -= int(h * (scale_factor - 1) / 2)
        w = int(w * scale_factor)
        h = int(h * scale_factor)

        # 이미지 경계를 벗어나지 않도록 조정
        x = max(0, x)
        y = max(0, y)
        w = min(image.shape[1] - x, w)
        h = min(image.shape[0] - y, h)

        # 얼굴 영역 잘라내기
        face_image = image[y:y+h, x:x+w]

        # 얼굴을 잘라낸 이미지를 저장
        output_dir = Path(r"your_directory")
        output_dir.mkdir(parents=True, exist_ok=True)
        new_file_name = f"{image_file.stem}_face{index}.jpg"
        output_file_path = output_dir / new_file_name
        cv2.imwrite(str(output_file_path), face_image)

        # 기존 파일을 삭제 (선택사항)
        #os.remove(str(image_file))

        print(f"얼굴을 검출하고 저장했습니다: {output_file_path}")

print("작업 완료")
