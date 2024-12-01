import React, { useEffect, useRef } from "react";

const P5Renderer = ({ code }) => {
  const sketchRef = useRef();

  useEffect(() => {
    if (!code) return;

    let p5Instance;

    const executeSketch = () => {
      const script = document.createElement("script");
      script.type = "text/javascript";

      const cleanedCode = code.replace(/^```javascript\n|```$/g, "");
      script.textContent = cleanedCode;
      document.body.appendChild(script);

      const sketch = window.__P5_SKETCH__; // A global variable expected from API code
      if (sketch) {
        const p5 = require("p5");
        p5Instance = new p5(sketch, sketchRef.current);
      }

      return () => {
        if (p5Instance) {
          p5Instance.remove();
          p5Instance = null;
        }
        document.body.removeChild(script);
      };
    };
    try {
      const cleanup = executeSketch();
      return cleanup;
    } catch (err) {
      console.error(err);
    }
  }, [code]);

  return <div ref={sketchRef}></div>;
};

export default P5Renderer;
