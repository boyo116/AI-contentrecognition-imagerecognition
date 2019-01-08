import cv2
import time
import datetime

save_path = 'E:/code/face/'
face_cascade = cv2.CascadeClassifier('E:/tools/opencv/sources/data/haarcascades/haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('E:/tools/opencv/sources/data/haarcascades/haarcascade_frontalcatface_extended.xml')

camera = cv2.VideoCapture(0)


if (camera.isOpened()):
    print('Open')
else:
    print('camera is not available')


size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('size:'+repr(size))

fps = 5
pre_frame = None
i = 0
j = 0
while True:
    start = time.time()
    grabbed, frame_lwpCV = camera.read()
    gray_lwpCV = cv2.cvtColor(frame_lwpCV, cv2.COLOR_BGR2GRAY)

    if not grabbed:
        break
    end = time.time()


    faces = face_cascade.detectMultiScale(gray_lwpCV, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame_lwpCV, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray_lwpCV = gray_lwpCV[y:y + h // 2, x:x + w]
        roi_frame_lwpCV = frame_lwpCV[y:y + h // 2, x:x + w]
        cv2.imwrite(save_path + datetime.datetime.now().strftime("%Y-%m-%d") + str(i) + '.jpg', frame_lwpCV[y:y + h, x:x + w])
        i += 1
        eyes = eye_cascade.detectMultiScale(roi_gray_lwpCV, 1.03, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_frame_lwpCV, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('lwpCVWindow', frame_lwpCV)


    seconds = end - start
    if seconds < 1.0 // fps:
        time.sleep(1.0 // fps - seconds)
    gray_lwpCV = cv2.resize(gray_lwpCV, (500, 500))
    gray_lwpCV = cv2.GaussianBlur(gray_lwpCV, (21, 21), 0)

    if pre_frame is None:
        pre_frame = gray_lwpCV
    else:
        img_delta = cv2.absdiff(pre_frame, gray_lwpCV)
        thresh = cv2.threshold(img_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) < 1000:
                continue
            else:
                print("find something move")
                break
        pre_frame = gray_lwpCV
    key = cv2.waitKey(1) & 0xFF
	
    if key == ord('q'):
        break
# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()