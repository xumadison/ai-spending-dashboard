# **AI Spending Dashboard: Executive Summary**

The problem I'm solving is the financial literacy crisis among Americans regarding budgeting and managing personal finances. This dashboard is designed to help students build financial management habits by setting financial goals and tracking spending. This project is an interactive dashboard that analyzes your spending habits using an AI-powered backend built with Flask and a React frontend. It processes transaction data (CSV format) and provides insight into users' financial behavior. This dashboard helps you visualize your total spend, forecast future expenses, and receive personalized insights. It's designed to financial literacy gap among young adults by providing an interactive tool for budgeting and financial planning. It can identify where your money is going and give recommendations for how to allocate funds more wisely among different spending categories.

---

## **System Overview:**
* **Course Concept:** Infrastructure: Cloud Services / APIs / Containers - Docker
* **Architecture Diagram:** Here is the architecture diagram that shows how the components of the AI Spending Dashboard interact:![Architecture Diagram](./assets/architecture-diagram.png)
* **Data/Models/Services:** Upload a CSV file with your recent transaction data (Date, Merchant, Category, Amount) with a maximum of 10,000 rows. This project is licensed under the MIT License. The CSV file should be formatted with the following columns: 
* **Date**: The transaction date (in `YYYY-MM-DD` format)
* **Merchant**: The name of the merchant where the transaction occurred
* **Category**: The spending category (e.g., Groceries, Entertainment, Travel)
* **Amount**: The amount spent on the transaction (numeric)

---

## **Tech Stack:**

* **Frontend to visualize:**

  * React
  * CSS for styling (custom styles focusing on a minimalist design)

* **Backend to process:**

  * Flask API (Python web framework)
  * Gunicorn (WSGI server for Flask)
  * Pandas (for processing CSV data)
  * Logic for analyzing spending trends

* **Deployment:**

  * Docker (containerizing both frontend and backend)
---

## **How to Run (Local): Build**

1. Install **Docker** and **Docker Desktop**:

   * Download from [Docker](https://www.docker.com/products/docker-desktop).
   * Follow the installation instructions based on your OS.
```bash
# build
docker build -t ai-spending-dashboard .
# run
docker run --rm -p 8080:8080 --env-file .env.example ai-spending-dashboard
# health check 
curl http://localhost:8080/health

### **1. Clone the Repository**

Clone this repository to your local machine:

```bash
git clone https://github.com/xumadison/ai-spending-dashboard.git
cd ai-spending-dashboard
```

### **2. Backend Setup**

1. Navigate to the backend folder (usually where your `app.py` file is):

```bash
cd backend
```

2. **Create a virtual environment** and activate it:

   * On **Windows**:

     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

   * On **macOS/Linux**:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the required Python packages:**

```bash
pip install -r requirements.txt
```

4. **Run the Flask app locally:**

```bash
python app.py
```

Your Flask app should now be running on `http://localhost:8080`.

### **3. Frontend Setup**

1. Navigate to the frontend folder (usually where your `src` and `public` directories are):

```bash
cd frontend
```

2. **Install required dependencies:**

```bash
npm install
```

3. **Start the React development server:**

```bash
npm run dev
```

The React app should now be running on `http://localhost:5173`.

---

### **4. Running Together**

1. Start the Flask backend using:

```bash
python app.py
```

2. Start the React frontend using:

```bash
npm run dev
```

3. Open your browser and go to `http://localhost:5173` to interact with the dashboard!

---
## **Design Decisions:**
* **Why this concept?** I chose this concept because it aligns with the growing need for financial literacy, especially among students from 1st-generation and low-income households that are new to managing their finances. I considered alternatives such as creating a static web page to provide insights for financial tips on purchases, but decided that this data set dashboard would be more impactful in supporting with long-term spending behavior and visualizations.
* **Tradeoffs:** Performance concerns may arise with large datasets (100,000+ rows) due to the Pandas being in memory. It's a cost-effective alternative for introductory budget/spending platforms in comparison to purchasing financial management software for bookkeeping and tracking investments.
* **Security/Privacy:** Long-term data is not stored on the app and is only used to process insights for the user and is deleted after.
* **Ops:** Logs are captured for errors in the Flask app; the app could benefit from scaling in case of high traffic, and the app may have performance issues with large CSV files.

## **Results & Evaluation**
### **Sample outputs**
![Demo1](./assets/demo1.png)
![Demo2](./assets/demo2.png)
* **Validation** Unit tests for backend functionality and sample outputs were validated with manual calculation checks.

## **Whats Next**
### ** Planned improvements:** 
* Implementation of user authentication to save personal financial data
* More graphics and UI improvements
* Add a recommendation engine or chat bot to personalize financial advice
* STRETCH: Enhance the forecasting model for ARIMA or LSTM models for better accuracy

## **Links**
GitHub Repo: https://github.com/xumadison/ai-spending-dashboard.git
  
### **Analyze Your Spending**

Once the file is uploaded, the dashboard will:

* Display the **total spend** from the uploaded data.
* **Break down** your spending by **category** and **month**.
* **Forecast** your spending for the next month based on current trends.
* Provide **personalized insights** on your spending habits.
