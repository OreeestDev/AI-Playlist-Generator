# Dunci-Orest Music Flow

A web application for music discovery and recommendations, powered by a Python backend and a React frontend.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Music recommendations using Deezer API
- Interactive web interface built with React
- Data parsing and prompt management
- Easy to extend and customize

---

## Project Structure

```
project-root/
│
├── backend/
│   ├── main.py
│   ├── prompts.py
│   ├── deezer.py
│   ├── parsing.py
│   ├── data/
│   │   ├── response_data.json
│   │   └── testik.json
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── README.md
└── .gitignore
```

---

## Getting Started

### Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server:**
   ```bash
   python main.py
   ```

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the React development server:**
   ```bash
   npm start
   ```

---

## Usage

- Access the frontend at [http://localhost:3000](http://localhost:3000)
- The frontend communicates with the backend API for music recommendations and data.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

---

## License

This project is licensed under the MIT License.