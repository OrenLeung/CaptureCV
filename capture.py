import cv2

cap = cv2.VideoCapture(0)

img_counter = 0

user_input = input("Enter: FACE/NO")

dir = ""

if user_input == "FACE":
    dir ="./images/FACE/opencv_frame_{}.png"
else:
    dir ="./images/NO/opencv_frame_{}.png"



while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    img_name = dir.format(img_counter)
    cv2.imwrite(img_name, gray)
    print("{} written!".format(img_name))
    img_counter += 1

cap.release()
