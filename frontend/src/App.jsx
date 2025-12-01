import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = (e) => setFile(e.target.files[0]);

  const analyzeFile = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://localhost:8080/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setResult(data);

    } catch (err) {
      console.error("Error:", err);
    }
  };

  return (
    <div className="container">
      <h1>AI Spending Insight Dashboard</h1>

      {/* Upload + Button */}
      <div className="upload-row">
        <input type="file" onChange={handleUpload} />
        <button onClick={analyzeFile}>Analyze Spending</button>
      </div>

      {result && (
        <>
          {/* Overview Section */}
          <h2 className="section-title">Overview</h2>
          <div className="metric-grid">

            <div className="card">
              <h3>Total Spend</h3>
              <div className="metric-value">${result.total_spend.toFixed(2)}</div>
            </div>

            <div className="card">
              <h3>Forecast Next Month</h3>
              <div className="metric-value">
                ${result.forecast_next_month.toFixed(2)}
              </div>
            </div>

            <div className="card">
              <h3>Top Category</h3>
              <div className="metric-value">{result.top_category}</div>
            </div>

          </div>

          {/* Insight */}
          <h2 className="section-title">Insight</h2>
          <p className="insight-text">{result.insight_text}</p>

          {/* By Month */}
          <h2 className="section-title">By Month</h2>
          <div className="card">
            {Object.entries(result.by_month).map(([month, amount]) => (
              <div className="list-item" key={month}>
                <span className="list-label">{month}</span>
                <span className="list-value">${amount.toFixed(2)}</span>
              </div>
            ))}
          </div>

          {/* By Category */}
          <h2 className="section-title">By Category</h2>
          <div className="card">
            {Object.entries(result.by_category).map(([cat, amount]) => (
              <div className="list-item" key={cat}>
                <span className="list-label">{cat}</span>
                <span className="list-value">${amount.toFixed(2)}</span>
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
}

export default App;
