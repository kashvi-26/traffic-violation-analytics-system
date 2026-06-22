
# AI-Powered Traffic Violation Analytics System

## Overview

An intelligent computer vision system that automatically detects traffic violations from road images using YOLOv8 and OCR technologies.

The system identifies multiple traffic violations, extracts vehicle number plates, generates evidence images, creates structured reports, and produces downloadable PDF reports.

---

## Key Features

✅ Helmet Compliance Detection

✅ Triple Riding Detection

✅ Wrong Side Driving Detection

✅ Illegal Parking Detection

✅ Red Light Violation Detection

✅ License Plate Detection

✅ OCR-Based Plate Extraction

✅ Evidence Image Generation

✅ JSON Report Generation

✅ PDF Report Generation

---

## System Workflow

Input Image

↓

YOLOv8 Detection Models

↓

Violation Analysis Engine

↓

License Plate Detection

↓

OCR Extraction

↓

Evidence Generation

↓

JSON Report

↓

PDF Report

---

## Models Used

| Model | mAP50 |
|--------|--------|
| License Plate Detection | 96.5% |
| Wrong Side Detection | 96.1% |
| Red Light Detection | 88.5% |
| Illegal Parking Detection | 87.7% |
| Rider Safety Detection | 73.6% |

---

## Technologies

- Python
- YOLOv8
- OpenCV
- EasyOCR
- ReportLab
- NumPy

---

## Sample Outputs

- Annotated Evidence Image
- Violation Report PDF
- Structured JSON Output

---

## Future Enhancements

- Real-Time CCTV Monitoring
- Police Analytics Dashboard
- Violation Heatmaps
- Traffic Hotspot Analysis
- Cloud Deployment
