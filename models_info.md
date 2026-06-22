# Trained Models

## License Plate Detection

Purpose:

* Detect and localize vehicle number plates.

Performance:

* mAP50: 96.5%

Detected Classes:

* numberplate

---

## Wrong-Side Detection

Purpose:

* Detect vehicles travelling in the wrong direction.

Performance:

* mAP50: 96.1%

Detected Classes:

* right-side
* wrong-side

---

## Illegal Parking Detection

Purpose:

* Detect parking violations.

Performance:

* mAP50: 87.7%

Detected Classes:

* Melanggar (Violation)
* Tidak Melanggar (No Violation)

---

## Red Light Violation Detection

Purpose:

* Detect vehicles violating traffic signals.

Performance:

* mAP50: 88.5%

Detected Classes:

* Red Light Violation

---

## Rider Safety Detection

Purpose:

* Detect rider safety violations and motorcycle occupancy.

Performance:

* mAP50: 73.6%

Detected Classes:

* Helmet
* No Helmet
* Motorcycle
* Motorcyclist

Derived Violations:

* No Helmet
* Triple Riding (calculated from rider count)

---

## OCR-Based Number Plate Extraction

Technology:

* EasyOCR

Purpose:

* Extract vehicle registration numbers from detected number plate regions.

Note:

* OCR accuracy may vary depending on image resolution, lighting conditions, plate visibility, viewing angle, and motion blur.
