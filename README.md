# SQLD Result Checker

[![Flask](https://img.shields.io/badge/Flask-2.2.2-blue)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow)](https://www.python.org/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.0.0-06B6D4)](https://tailwindcss.com/)

A modern web application that allows users to check their SQL Developer (SQLD) certification exam results from the Korea Data Agency portal.

## Features

- **Secure Authentication**: Login to the official Data Quality portal
- **Real-time Results**: Fetch and display the latest SQLD exam results
- **Beautiful UI**: Clean, responsive interface built with TailwindCSS
- **Detailed Scores**: View comprehensive breakdown of exam scores by subject

## Requirements

- Python 3.8+
- Flask 2.2.2
- TailwindCSS 3.0.0
- PostCSS 8.0.0
- Autoprefixer 10.0.0

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/sqld-result-checker.git
   cd sqld-result-checker
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Install Node.js dependencies
   ```bash
   npm install
   ```

5. Build TailwindCSS
   ```bash
   npx tailwindcss -i ./static/src/main.css -o ./static/dist/main.css
   ```

## Usage

1. Start the Flask development server
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000`

3. Log in with your Data Quality portal credentials

4. View your SQLD exam results

## Project Structure

```
sqld-result-checker/
├── app.py                  # Main Flask application
├── static/                 # Static files
│   └── css/style.css       # Source CSS 
├── templates/              # HTML templates
│   ├── index.html          # Login page
│   └── results.html        # Results display page
├── requirements.txt        # Python dependencies
├── package.json            # Node.js dependencies
├── tailwind.config.js      # TailwindCSS configuration
├── postcss.config.js       # PostCSS configuration
└── README.md               # Project documentation
```

## How It Works

The application securely authenticates with the Korea Data Agency portal and fetches exam results using their API. The process involves:

1. User authentication via login form
2. Session management with cookies
3. API requests to fetch exam results
4. Rendering results with detailed score breakdown

## Security Considerations

- User credentials are never stored
- Session cookies are managed securely
- HTTPS is recommended for production deployment
- Environment variables should be used for secrets in production

## Customization

You can customize the appearance by modifying the TailwindCSS configuration:

```bash
# Rebuild CSS after making changes
npx tailwindcss -i ./static/src/main.css -o ./static/dist/main.css --watch
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgements

- [Korea Data Agency](https://www.dataq.or.kr/) for providing the SQLD certification
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [TailwindCSS](https://tailwindcss.com/) for the UI components
