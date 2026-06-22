
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

def save_json_report(result):

```
with open(
    "output/result.json",
    "w"
) as f:

    json.dump(
        result,
        f,
        indent=4
    )
```

def save_evidence_image(image_path):

```
results = rider_model(
    image_path,
    conf=0.4
)

annotated = results[0].plot()

cv2.imwrite(
    "output/evidence.jpg",
    annotated
)
```

def generate_pdf_report(result):

```
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

pdf_path = "output/Violation_Report.pdf"

doc = SimpleDocTemplate(pdf_path)

styles = getSampleStyleSheet()

content = []

content.append(
    Paragraph(
        "TRAFFIC VIOLATION REPORT",
        styles["Title"]
    )
)

content.append(
    Spacer(1, 12)
)

content.append(
    Paragraph(
        f"<b>Vehicle Type:</b> {result['vehicle_type']}",
        styles["Normal"]
    )
)

content.append(
    Spacer(1, 10)
)

content.append(
    Paragraph(
        f"<b>Plate Number:</b> {result['plate_number']}",
        styles["Normal"]
    )
)

content.append(
    Spacer(1, 10)
)

content.append(
    Paragraph(
        "<b>Detected Violations:</b>",
        styles["Normal"]
    )
)

for violation in result["violations"]:

    content.append(
        Paragraph(
            f"• {violation}",
            styles["Normal"]
        )
    )

doc.build(content)
```


import os
import sys

if **name** == "**main**":

```
if len(sys.argv) != 2:

    print(
        "Usage: python app.py <image_path>"
    )

    exit()

os.makedirs(
    "output",
    exist_ok=True
)

image_path = sys.argv[1]

result = analyze_image(
    image_path
)

save_json_report(result)

save_evidence_image(
    image_path
)

generate_pdf_report(
    result
)

print(
    json.dumps(
        result,
        indent=4
    )
)

print(
    "\nOutputs saved in output/"
)
```

