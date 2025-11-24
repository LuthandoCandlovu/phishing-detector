# PhishShield - Phishing URL Detection

A machine learning-based phishing URL detection system that analyzes URLs to identify potential phishing threats.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

PhishShield uses machine learning to analyze URLs and detect potential phishing attempts. The system examines multiple features including URL structure, domain characteristics, and page content to provide a risk assessment.

## Features

- **URL Analysis**: Examines URL structure and domain characteristics
- **Machine Learning Detection**: Uses trained models to identify phishing patterns
- **Feature Extraction**: Analyzes 75+ URL features
- **Command Line Interface**: Easy-to-use CLI for quick analysis
- **Python API**: Integrate detection into your applications

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

```bash
# Clone the repository
git clone https://github.com/LuthandoCandlovu/phishing-detector.git
cd phishing-detector

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Python API

```python
from phishshield import URLAnalyzer

# Initialize analyzer
analyzer = URLAnalyzer()

# Analyze a URL
result = analyzer.analyze("https://example.com")

print(f"Is Phishing: {result.is_phishing}")
print(f"Confidence: {result.confidence:.2%}")
print(f"Risk Score: {result.risk_score}/100")
```

### Command Line Interface

```bash
# Analyze a single URL
python main.py --url "https://example.com"

# Analyze from a file
python main.py --file urls.txt

# Output results as JSON
python main.py --url "https://example.com" --format json
```

## How It Works

PhishShield analyzes URLs through multiple stages:

1. **URL Parsing**: Extracts components (domain, path, parameters)
2. **Feature Extraction**: Calculates features like URL length, special characters, domain age
3. **ML Classification**: Applies trained models to predict phishing likelihood
4. **Risk Scoring**: Combines multiple signals into a final risk assessment

### Key Features Analyzed

- URL length and complexity
- Domain characteristics
- Presence of IP addresses
- Suspicious keywords
- HTTPS usage
- Domain registration age
- URL shorteners
- Special character patterns

## Project Structure

```
phishing-detector/
├── src/
│   ├── analyzer.py      # Main analysis logic
│   ├── features.py      # Feature extraction
│   └── models.py        # ML models
├── data/
│   ├── training/        # Training datasets
│   └── models/          # Saved models
├── tests/               # Unit tests
├── main.py             # CLI entry point
├── requirements.txt    # Dependencies
└── README.md
```

## Configuration

Create a `config.yml` file to customize behavior:

```yaml
analysis:
  timeout: 5
  max_redirects: 3
  
model:
  confidence_threshold: 0.8
  
logging:
  level: INFO
```

## Development

### Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Run with coverage
pytest --cov=src tests/
```

### Training Models

To retrain the detection models:

```bash
python scripts/train.py --data data/training/urls.csv
```

## Performance

Current model performance on test dataset:
- **Accuracy**: 94.5%
- **Precision**: 93.2%
- **Recall**: 95.1%
- **F1 Score**: 94.1%

*Note: Performance may vary based on dataset and URL types*

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code:
- Follows PEP 8 style guidelines
- Includes appropriate tests
- Updates documentation as needed

## Limitations

- Detection accuracy depends on training data quality
- May have false positives on legitimate but unusual URLs
- Requires periodic model updates to detect new phishing patterns
- Cannot analyze password-protected or dynamic content

## Roadmap

- [ ] Real-time URL monitoring
- [ ] Browser extension
- [ ] REST API service
- [ ] Enhanced feature extraction
- [ ] Support for additional languages

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Phishing datasets from [PhishTank](https://www.phishtank.com/)
- Machine learning libraries: scikit-learn, pandas, numpy
- Community contributors

## Support

- **Issues**: [GitHub Issues](https://github.com/LuthandoCandlovu/phishing-detector/issues)
- **Discussions**: [GitHub Discussions](https://github.com/LuthandoCandlovu/phishing-detector/discussions)

---

**Disclaimer**: This tool is for educational and research purposes. Always exercise caution when visiting unfamiliar URLs.
