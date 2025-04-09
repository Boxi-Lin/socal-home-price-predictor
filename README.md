# 🏠 SoCal Home Price Predictor

A machine learning web app that predicts home prices in Southern California based on user input. Built with a full-stack approach using Python, Flask, scikit-learn, HTML/CSS/JS, and deployed on AWS EC2.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Deployment](#deployment)
- [What I Learned](#what-i-learned)

---

## 📖 Overview

The goal of this project was to develop a full end-to-end machine learning application that:
- Trains a linear regression model on housing data
- Exposes predictions through a Flask API
- Accepts user input via a responsive frontend
- Is deployed and accessible publicly via an AWS EC2 instance

---

## 🛠 Tech Stack

| Area       | Tech                       |
|------------|----------------------------|
| Data Science | Jupyter Notebook, pandas, scikit-learn |
| Backend    | Python, Flask, Flask-CORS  |
| Frontend   | HTML, CSS, JavaScript      |
| Deployment | AWS EC2, NGINX, WinSCP, GitHub |

---

## ⚙️ How It Works

1. **Modeling (Jupyter Notebook)**  
   A linear regression model is trained on Southern California housing data using `scikit-learn`.

2. **Backend (Flask)**  
   A simple REST API is built to serve predictions from the trained model using user-provided features.

3. **Frontend**  
   The user can input features like square footage, location, and more into an HTML form styled with CSS and JS.

4. **Deployment**  
   All components are deployed to an Ubuntu server on AWS EC2. Flask is served behind NGINX, and GitHub is used for version control.

---

## 🧪 Installation (Local Dev)

```bash
git clone https://github.com/Boxi-Lin/socal-home-price-predictor.git
cd socal-home-price-predictor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 server.py
