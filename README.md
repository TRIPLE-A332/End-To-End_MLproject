# End‑to‑End ML Project

A production‑ready, end‑to‑end machine learning project with a **Flask** web app, a **scikit‑learn** pipeline, and **AWS Elastic Beanstalk** deployment. It includes data preprocessing, model training, prediction serving, and CI/CD scaffolding.

---

## Live Demo

**Deployed URL:** http://endtoend-ml-project-env.eba-ihg2htjm.us-east-1.elasticbeanstalk.com/predictdata

> If the page is sleeping or cold‑starting, give it a moment. The home page responds with a simple “/”, and the **`/predictdata`** route serves the prediction form and handles submissions.

---

## What it Predicts

This app demonstrates tabular ML on student performance data. The model predicts a target score (**math_score**) from the following inputs:

- `gender` *(categorical)*  
- `race_ethnicity` *(categorical)*  
- `parental_level_of_education` *(categorical)*  
- `lunch` *(categorical)*  
- `test_preparation_course` *(categorical)*  
- `reading_score` *(numeric)*  
- `writing_score` *(numeric)*

These fields are shown in the **/predictdata** HTML form and posted to the same endpoint for inference.

---


>  Elastic Beanstalk expects a WSGI target like `module:object`.  
> If your file is `application.py` and contains `application = Flask(__name__)`, then the target is `application:application`.  
> If you have `app = Flask(__name__)` in `app.py`, then the target is `app:app` or `app:application` if you named it so.


---