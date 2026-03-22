# Edge Deployment Plan

## Goal

Deploy the system on-device (mobile or edge) for real-time, private inference.

---

## Model Choice

* Logistic Regression
* TF-IDF features

Reason:

* Lightweight
* Fast inference
* Small memory footprint

---

## Deployment Strategy

### Option 1 — ONNX Conversion

* Convert sklearn model to ONNX
* Run using ONNX Runtime

### Option 2 — Direct Python Execution

* Use lightweight Python runtime
* Suitable for Android (via Chaquopy) or iOS (via wrappers)

---

## System Constraints

### Model Size

* < 50 MB

### Latency

* < 200 ms per inference

### Memory

* < 200 MB RAM usage

---

## Tradeoffs

| Factor      | Tradeoff                        |
| ----------- | ------------------------------- |
| Accuracy    | Slightly lower than deep models |
| Speed       | Very fast                       |
| Privacy     | High (on-device)                |
| Scalability | Limited model complexity        |

---

## Optimizations

* Reduce TF-IDF features (e.g., 3000 instead of 5000)
* Quantize model weights
* Cache vectorizer
* Use batch inference where possible

---

## Handling Edge Cases

### Short Text

* Use metadata-driven fallback

### Missing Data

* Impute + flag missingness

### Conflicting Signals

* Prioritize physiological features

---

## Future Improvements

* Replace TF-IDF with small embedding model
* Add lightweight neural model (distilled)
* Implement adaptive decision engine

---

## Conclusion

The system is highly suitable for edge deployment due to:

* Low computational requirements
* Fast inference
* Minimal dependencies
* Strong real-world robustness

---
