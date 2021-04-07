import cv2
import face_recognition
import os
import glob

vc = cv2.VideoCapture(0)

known_faces = []
known_names = []
known_faces_paths = []

registered_faces_path = "D:\\python\\Workspace\\New folder\\registered\\"
for name in os.listdir(registered_faces_path):
    images_mask = '%s%s/*.jpg' % (registered_faces_path, name)
    images_paths = glob.glob(images_mask) 
    known_faces_paths += images_paths
    known_names += [name for x in images_paths]

def get_encodings(img_path):
    image = face_recognition.load_image_file(img_path)
    encoding = face_recognition.face_encodings(image)
    return encoding[0]

known_faces = [get_encodings(img_path) for img_path in known_faces_paths]


while True:
    ret, frame = vc.read()
    if not ret:
        break
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(frame_rgb)
    for face in faces: # top, right, bottom, left
        top, right, bottom, left = face
        cv2.rectangle(frame, (left, top), (right, bottom),(0,0,255), 2)
        face_code = face_recognition.face_encodings(frame_rgb, [face])[0]

        results = face_recognition.compare_faces(known_faces, face_code, tolerance=0.6)
        if any(results):
            name = known_names[results.index(True)]
        else:
            name = 'unknown'
        cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)

    cv2.imshow('Face Recog', frame)
    k = cv2.waitKey(1)
    if ord('q') == k:
        break
cv2.destroyAllWindows()
vc.release()
