# In-Cabin Driver Monitoring for Phone Distraction Detection
### 🎥 Demo Video

[![Watch the demo video](https://github.com/suyashi-agarwal/distracted-driver-monitoring/blob/main/demo_thumbnail.png)](https://drive.google.com/file/d/1iG5gxCYHgM8SMmmCD8QUvHeApCnwNCI_/view?usp=sharing)


## 📖 About the Project

This project is an end-to-end machine learning pipeline designed to enhance road safety by detecting mobile phone usage by drivers in real-time.
Leveraging a state-of-the-art YOLOv8 deep learning model, the system processes in-cabin visual data to identify signs of distraction, providing a foundation for creating timely alerts.
The pipeline covers the entire ML lifecycle, from data preprocessing and model training to evaluation, adhering to MLOps principles for maintainability and continuous improvement.

For more detailed documentation and project planning, please visit  **[Project Notion Page](https://www.notion.so/Driver-Monitoring-v1-2414999cae56807eae13fb3afdc56d96)**.
## ✨ Key Features

* **Real-time Distraction Detection**: Trained to identify drivers using a mobile phone and whether they are wearing a seatbelt or not.
* **State-of-the-Art Model**: Utilizes the YOLOv8 architecture, which is recognized for its high accuracy and speed.
* **Data Processing Pipeline**: Includes Python scripts for preprocessing raw visual data, including denoising and resizing, to prepare it for training.
* **Ethical Considerations**: The project acknowledges the importance of ethical AI, including data privacy and the prevention of algorithmic bias.

## 🛠️ Technologies Used

* **Python 3.11**
* **YOLOv8** (via Ultralytics)
* **PyTorch**
* **OpenCV**
* **Google Colab** (for GPU-accelerated training)
* **Git & GitHub**

## 🚀 How to Run This Project

Here are the steps to set up and run this project locally.

### 1. Prerequisites

* Python 3.8+
* Git

### 2. Setup and Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/YourUsername/your-repository-name.git](https://github.com/YourUsername/your-repository-name.git)
    cd your-repository-name
    ```
2.  **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```sh
    pip install opencv-python ultralytics
    ```
4.  **Download the Data:**
    * Download the required dataset from https://www.kaggle.com/c/state-FARM-distracted-driver-detection.
    * Place the data in the `data/raw/` directory according to the structure specified in the `prepare_data.py` script.

### 3. Usage

1.  **Prepare the data:**
    ```sh
    python prepare_data.py
    ```
2.  **Train the model:**
    * Upload the `processed` data to a cloud environment like Google Colab.
    * Run the training command:
        ```sh
        yolo train model=yolov8s.pt data=driver_dataset.yaml epochs=100 batch=16
        ```
3.  **Run inference:**
    ```sh
    yolo predict model=path/to/your/best.pt source=path/to/test_video.mp4
    ```

## 📈 Future Work

The operationalization of this system would require a strong commitment to MLOps principles. Future steps include:
* **Deployment**: Containerizing the application using Docker for deployment on an embedded system or cloud service[cite: 168].
* **Continuous Monitoring**: Implementing a monitoring system to track model performance and detect data drift over time[cite: 170, 171].
* **Automated Retraining**: Establishing a CI/CD pipeline for automatically retraining and deploying the model when performance degrades[cite: 187, 188].
