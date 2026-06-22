# AI-Powered Traffic Violation Analytics System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object_Detection-green)
![EasyOCR](https://img.shields.io/badge/EasyOCR-OCR-orange)

## Overview

AI-Powered Traffic Violation Analytics System is a computer vision-based solution designed to automatically detect traffic violations from road images using YOLOv8 object detection models and OCR techniques.

The system identifies multiple traffic violations, localizes vehicle number plates, extracts plate information using OCR, and automatically generates structured reports for further analysis.

---

## Features

### Traffic Violation Detection

* Helmet Violation Detection
* Triple Riding Detection
* Wrong-Side Driving Detection
* Illegal Parking Detection

### License Plate Analysis

* License Plate Localization
* OCR-Based Number Plate Extraction

### Automated Reporting

* Annotated Evidence Image Generation
* JSON Report Generation
* PDF Violation Report Generation

---

## System Architecture

Input Image

↓

YOLOv8 Detection Models

├── Rider Safety Detection

├── Wrong-Side Detection

├── Illegal Parking Detection

└── License Plate Detection

↓

Violation Analysis Engine

↓

OCR-Based Number Plate Extraction

↓

Evidence Generation

↓

JSON Report

↓

PDF Report

---

## Technologies Used

### Machine Learning & Computer Vision

* YOLOv8
* OpenCV
* EasyOCR

### Programming Language

* Python

### Reporting

* JSON
* ReportLab PDF Generation

---

## Models Used

| Model                         | Purpose                                    |
| ----------------------------- | ------------------------------------------ |
| Rider Safety Model            | Helmet Detection & Triple Riding Detection |
| Wrong-Side Detection Model    | Wrong Direction Vehicle Detection          |
| Illegal Parking Model         | Parking Violation Detection                |
| License Plate Detection Model | Number Plate Localization                  |

---

## Sample Output

### Supported Violations

- No Helmet
- Triple Riding
- Wrong-Side Driving
- Illegal Parking

### Generated Outputs

* Annotated Evidence Image
* JSON Report
* PDF Violation Report

Refer to the `sample_outputs/` folder for example outputs.

---

## Output Screenshots

### Evidence Image

![Evidence Image](docs/evidence_output.jpg)

### JSON Report

![JSON Output](docs/json_output.png)

### PDF Report

![PDF Output](docs/pdf_output.png)

---

## Project Structure

traffic-violation-analytics-system/

├── app.py

├── README.md

├── requirements.txt

├── models_info.md

├── docs/

├── sample_inputs/

└── sample_outputs/

---

## Example JSON Output

```json
{
  "vehicle_type": "Motorcycle",
  "violations": [
    "No Helmet",
    "Triple Riding"
  ],
  "plate_number": "Detected via OCR"
}
```

---

## Future Enhancements

* Real-Time CCTV Integration
* Video-Based Violation Detection
* Vehicle Tracking
* Automatic Challan Generation
* Cloud Deployment

---

## Results

The system successfully performs:

* Multi-model traffic violation detection
* Automated license plate localization
* OCR-based plate extraction
* Evidence image generation
* Structured JSON report generation
* PDF violation report generation

---

## Notes

- License plate localization is performed using a custom YOLOv8 model.
- OCR-based plate extraction is integrated using EasyOCR.
- OCR performance may vary depending on image resolution, plate visibility, camera angle, lighting conditions, and motion blur.

---

## Author

Kashvi Dashore

B.Tech – Artificial Intelligence & Data Engineering

Indian Institute of Information Technology Kota (IIIT Kota)
