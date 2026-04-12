# Gait Analysis for Health Monitoring

A Python-based computer vision project for analyzing human gait patterns using video data. This project focuses on extracting meaningful walking metrics (such as step length, cadence, and speed) to help identify potential indicators of neurological conditions like dementia or Parkinson’s disease.

---

## Project Overview

Gait analysis is the study of human walking patterns. Changes in gait can be early indicators of health issues, especially in elderly populations.

This project uses **pose estimation** to track body movement from video and compute key gait metrics automatically.

---

## Objectives

- Detect human pose from video using computer vision
- Extract key body landmarks (e.g., ankles, hips)
- Compute gait parameters:
  - Step length
  - Cadence (steps per minute)
  - Walking speed (approximate)
- Compare walking patterns across different conditions:
  - Normal walking
  - Simulated slow walking
  - Simulated short-step gait (Parkinson-like)

---

## Tech Stack

- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- Matplotlib

---

## 🎥 Input Data

Place your walking videos inside the `data/` folder.

### Recommended recording setup:

- Camera fixed (no movement)
- Side view of the person walking
- Good lighting conditions
- Full body visible
- Walk in a straight line (5–10 meters)

---

## ⚙️ Installation

## ⚙️ Installation

To set up the environment, follow these steps:

### 1. Create a virtual environment (recommended)
```bash
python -m venv gaitenv
.\gaitenv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Authors
- Paula Frías Arroyo
- Rebeca Piñol Galera
- Nicolás Cañas Muñoz-Blanco
- Abderrahmene Chikh
- Jonhas Fortem Mbah