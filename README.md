# **AI Spending Dashboard**

The problem I'm solving is the financial literacy crisis among Americans regarding budgeting and managing personal finances. This dashboard is designed to help students build financial management habits by setting financial goals and tracking spending. This project is an interactive dashboard that analyzes your spending habits using an AI-powered backend built with Flask and a React frontend. It processes transaction data (CSV format) and provides insight into users' financial behavior. This dashboard helps you visualize your total spend, forecast future expenses, and receive personalized insights. It's designed to financial literacy gap among young adults by providing an interactive tool for budgeting and financial planning. It can identify where your money is going and give recommendations for how to allocate funds more wisely among different spending categories.

---

## **Features:**
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

## **Setup & Installation**

1. Install **Docker** and **Docker Desktop**:

   * Download from [Docker](https://www.docker.com/products/docker-desktop).
   * Follow the installation instructions based on your OS.

2. Install **Node.js** and **npm** (for React frontend):

   * Download from [Node.js](https://nodejs.org/).

3. Install **Python 3.x** (for Flask backend):

   * Download from [Python](https://www.python.org/downloads/).

---

### **1. Clone the Repository**

Clone this repository to your local machine using Git:

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

## **Usage**

### **Upload Your CSV File**

The dashboard allows you to upload a CSV file containing your transaction data. The CSV should have the following columns:

* **Date**: The transaction date (in `YYYY-MM-DD` format)
* **Merchant**: The name of the merchant where the transaction occurred
* **Category**: The spending category (e.g., Groceries, Entertainment, Travel)
* **Amount**: The amount spent on the transaction (numeric)

### **Analyze Your Spending**

Once the file is uploaded, the dashboard will:

* Display the **total spend** from the uploaded data.
* **Break down** your spending by **category** and **month**.
* **Forecast** your spending for the next month based on current trends.
* Provide **personalized insights** on your spending habits.
