import cv2 as cv

# 카메라 캡처 객체 생성
cap = cv.VideoCapture(0)

# 해상도 가져오기
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# 초기 FPS
fps = 20

# 비디오 코덱 설정 (MJPG)
fourcc = cv.VideoWriter_fourcc(*'MJPG')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (width, height))

record_mode = False
flip_mode = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 좌우 반전
    if flip_mode:
        frame = cv.flip(frame, 1)

    # 모드 텍스트 표시
    if record_mode:
        cv.putText(frame, 'Recording', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv.circle(frame, (30, 30), 10, (0, 0, 255), -1)
        out.write(frame)
    else:   
        cv.putText(frame, 'Press Space to Record', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # FPS 표시
    cv.putText(frame, f'FPS: {fps}', (50, 90), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # 화면 출력
    cv.imshow('Camera', frame)

    key = cv.waitKey(1) & 0xFF

    if key == 27: # ESC
        break
    elif key == 32: # Space
        record_mode = not record_mode
    elif key == ord('f'):  # flip
        flip_mode = not flip_mode
    elif key == ord('+'):  # FPS 증가
        fps += 5
        out.release()
        out = cv.VideoWriter('output.avi', fourcc, fps, (width, height))
    elif key == ord('-'):  # FPS 감소
        fps -= 5
        out.release()
        out = cv.VideoWriter('output.avi', fourcc, fps, (width, height))

cap.release()
out.release()       
cv.destroyAllWindows()