import React, { useState } from "react";

import axios from "axios";
import P5Renderer from "./P5Renderer";
import Form from "./Form";

import "./App.css";

const App = () => {
  const [code, setCode] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFormSubmit = async (message) => {
    setIsLoading(true);
    setError("");
    try {
      const response = await axios.post("http://127.0.0.1:8000/generate-p5", {
        message,
      }); // Replace with your API URL
      setCode(response.data.code); // Ensure API response contains `code` field
    } catch (err) {
      const code =
        "window.__P5_SKETCH__ = function(p) { p.setup = function() { p.createCanvas(400, 400); p.background(220); }; };";
      setCode(code);
      //setError("Failed to fetch the sketch.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <div style={{ position: "absolute", bottom: 10, left: 10, right: 10 }}>
        <Form onSubmit={handleFormSubmit} isLoading={isLoading} />
      </div>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {code && <P5Renderer code={code} />}
    </div>
  );
};

export default App;
