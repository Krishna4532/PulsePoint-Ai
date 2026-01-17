import cv2
import mediapipe as mp

def get_face_center(frame):
    # Initialize MediaPipe Face Detection
    mp_face_detection = mp.solutions.face_detection
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        # Convert the BGR image to RGB
        results = face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if results.detections:
            for detection in results.detections:
                # Get the bounding box
                bbox = detection.location_data.relative_bounding_box
                # Calculate the center X coordinate
                center_x = bbox.xmin + (bbox.width / 2)
                return center_x
        return 0.5  # Default to middle if no face found