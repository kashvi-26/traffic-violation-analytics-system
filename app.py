
from ultralytics import YOLO
import easyocr
import cv2
import json

# Load Models
rider_model = YOLO("models/best_rider_safety.pt")
plate_model = YOLO("models/best_license_plate.pt")
wrong_side_model = YOLO("models/best_wrong_side.pt")
parking_model = YOLO("models/best_parking.pt")

reader = easyocr.Reader(['en'])

def extract_plate_number(image_path):

    plate_results = plate_model(image_path)

    img = cv2.imread(image_path)

    plate_text = "Not Detected"

    for box in plate_results[0].boxes:

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        plate_crop = img[y1:y2, x1:x2]

        plate_crop = cv2.resize(
            plate_crop,
            None,
            fx=8,
            fy=8,
            interpolation=cv2.INTER_CUBIC
        )

        gray = cv2.cvtColor(
            plate_crop,
            cv2.COLOR_BGR2GRAY
        )

        ocr_result = reader.readtext(gray)

        if len(ocr_result) > 0:
            plate_text = ocr_result[0][1]

    return plate_text

def detect_wrong_side(image_path):

    results = wrong_side_model(image_path, conf=0.4)

    for box in results[0].boxes:

        cls = int(box.cls)

        label = wrong_side_model.names[cls]

        if label == "wrong-side":
            return True

    return False

def detect_illegal_parking(image_path):

    results = parking_model(image_path, conf=0.4)

    for box in results[0].boxes:

        cls = int(box.cls)

        label = parking_model.names[cls]

        if label == "Melanggar":
            return True

    return False

def analyze_image(image_path):

    violations = []

    results = rider_model(image_path, conf=0.4)

    motorcyclist_count = 0
    no_helmet_count = 0

    for box in results[0].boxes:

        cls = int(box.cls)
        label = rider_model.names[cls]

        if label == "motorcyclist":
            motorcyclist_count += 1

        if label == "no_helmet":
            no_helmet_count += 1

    if no_helmet_count > 0:
        violations.append("No Helmet")

    if motorcyclist_count >= 3:
        violations.append("Triple Riding")

    if detect_wrong_side(image_path):
        violations.append("Wrong Side Driving")

    if detect_illegal_parking(image_path):
        violations.append("Illegal Parking")

    plate_number = extract_plate_number(image_path)

    result = {
        "vehicle_type": "Motorcycle",
        "violations": violations,
        "plate_number": plate_number
    }

    return result

if __name__ == "__main__":

    image_path = "sample_inputs/sample_motorcycle.jpg"

    result = analyze_image(image_path)

    print(json.dumps(result, indent=4))
