import	cv2
import	numpy as np

cap = cv2.VideoCapture(0)

fourcc = cv2.cv.FOURCC(*"XVID")
out = cv2.VideoWriter('Output.avi',fourcc, 20.0, (640,480))

while (cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		frame = cv2.flip(frame,0)

		out.write(frame)

		cv2.imshow('Frame',frame)

		if cv2.waitKey(1) == ord('q'):
			break
	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows()