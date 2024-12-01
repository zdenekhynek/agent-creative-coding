import { useState } from "react";

const Form = ({ onSubmit, isLoading }) => {
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    onSubmit(message);
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{ display: "flex", width: "100%", marginBottom: "20px" }}
    >
      <label style={{ flex: "auto" }}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          style={{
            backgroundColor: "transparent",
            border: 0,
            outline: 0,
            borderBottom: "1px solid gray",
            color: "gray",
            padding: "10px",
            width: "100%",
            boxSizing: "border-box",
          }}
          required
        />
      </label>
      <button
        type="submit"
        disabled={isLoading}
        style={{
          padding: "2px 5px",
          background: "gray",
          color: "white",
          border: "none",
          cursor: isLoading ? "not-allowed" : "pointer",
          opacity: isLoading ? 0.2 : 1,
        }}
      >
        Submit
      </button>
    </form>
  );
};

export default Form;
