import cv2
import mediapipe as mp
import math
import time

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def is_straight_line(point1, point2, point3):
    # 三つの点がほぼ直線上にあるかどうかを計算
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    distance = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    length1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    length2 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

    return distance / (length1 * length2) < 0.1

video_path = 'glute_bridge_demo.mp4'
cap = cv2.VideoCapture(video_path)


with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    prev_count_state = False
    current_count_state = False
    count_count = 0
    frame_count = 0

    start_time = time.time()  # 始まる時間を記録

    while True:
        ret, frame = cap.read()
        if not ret:
            print('ビデオの読み込みが終了しました...')
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        annotated_image = frame.copy()

        mp_drawing.draw_landmarks(annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        #固定想检查的部分
        left_knee = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
        left_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
        left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]

        right_knee = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]
        right_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
        right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]

        if not prev_count_state and current_count_state:
            count_count += 1

        prev_count_state = current_count_state

        #feedback初始化
        feedback_message = ""

        if is_straight_line((left_knee.x, left_knee.y), (left_hip.x, left_hip.y), (left_shoulder.x, left_shoulder.y)) and \
           is_straight_line((right_knee.x, right_knee.y), (right_hip.x, right_hip.y), (right_shoulder.x, right_shoulder.y)):
            feedback_message = "Good glute bridge posture!"
            current_count_state = True
        else:
            feedback_message = "Adjust your posture to maintain a straight line from knees to hips to shoulders."

            current_count_state = False

        #FPS数値
        end_time = time.time()
        elapsed_time = end_time - start_time
        fps = frame_count / elapsed_time
        print(f"FPS: {fps:.2f}")

        # 計数を表示
        cv2.putText(annotated_image,
                    f"Count: {count_count}", (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # FPS数值

        cv2.putText(annotated_image,
                    f"FPS: {fps:.2f}", (50, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # feedback表示

        cv2.putText(annotated_image,
                    feedback_message, (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Glute Bridge Pose Estimation', annotated_image)



        # 計数を表示+1
        frame_count += 1

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
