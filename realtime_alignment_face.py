#importing the required libraries
import cv2
import dlib

#capture the video from default camera 
webcam_video_stream = cv2.VideoCapture(0)

#load the pretrained HOG SVN model
face_detection_classifier = dlib.get_frontal_face_detector()

# load shape predictor to predict face landmark points of individual facial structures
face_shape_predictor = dlib.shape_predictor('models/shape_predictor_5_face_landmarks.dat')

#initialize the array variable to hold all face locations in the frame
all_face_locations = []

#loop through every frame in the video
while True:
    # object to hold the 5 face landmark points for every face
    face_landmarks = dlib.full_object_detections()
    
    #get the current frame from the video stream as an image
    ret, current_frame = webcam_video_stream.read()

    #detect all face locations using the HOG SVN classifier
    all_face_locations = face_detection_classifier(current_frame, 1)    
    
    # kiểm tra nếu có khuôn mặt nào được phát hiện
    if len(all_face_locations) > 0:
        #looping through the face locations
        for index, current_face_location in enumerate(all_face_locations):
            #looping through all face detections and append shape predictions
            face_landmarks.append(face_shape_predictor(current_frame, current_face_location))
        
        # tạo face chips chỉ khi có khuôn mặt
        all_face_chips = dlib.get_face_chips(current_frame, face_landmarks, size=160, padding=0.25) 
        
        #loop through the face chips and show them
        for index, current_face_chip in enumerate(all_face_chips):
            #show the face chip
            cv2.imshow("Face no " + str(index + 1), current_face_chip)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    #showing the current face with rectangle drawn
    cv2.imshow("Webcam Video", current_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the stream and cam
#close all opencv windows open
webcam_video_stream.release()
cv2.destroyAllWindows()

