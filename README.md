# Quiz Game Web App
A simple **interactive quiz game** built using **Python (Flask)** and **HTML**.
The app runs in a web browser and allows users to answer multiple-choice questions and view their final score.

## Features
- Step-by-step quiz with multiple-choice questions  
- Keeps track of your score  
- Stylish, vibrant, and mobile-friendly design  
- Works on any device with a browser  
- Simple and lightweight Flask backend  

## Technologies Used
**Backend:** Python 3 + Flask  
**Frontend:** HTML, CSS (with Gen Z gradients & styling)  
**Deployment:** Railway (cloud platform)  
**Session Management:** Flask sessions to store current question and score  

## Getting Started (Local Development)
## 1.Clone the repository
bash
git clone <your-repo-url>
cd <repo-folder>

## 2.Create a virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

## 3.Installation & Setup
**Install Python**
Download and install Python from:
https://www.python.org/downloads/
⚠️ Ensure you check **"Add Python to PATH"**

**Install Flask**
Open PowerShell and run:
bash
pip install flask

**Install dependencies**
pip install -r requirements.txt

## 4.Run the app locally
1.Navigate to your project folder:
bash
cd C:\projects\quiz-game
2.Start the Flask server:
bash
python app.py

## 5.Open in your browser
http://127.0.0.1:500/

## Deployment on Railway
1.Push your code to GitHub
2.Connect your repository to Railway
3.Ensure you have a Procfile with:
web: gunicorn app:app
4.Railway will automatically deploy your app
5.Use the generated public URL to share your quiz

## Styling
Vibrant gradients and fun fonts
Interactive buttons with hover effects
Mobile-friendly layout

## Project Structure
BrainBlast/
│
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
├── Procfile             # Railway deployment command
├── templates/
│   ├── quiz.html        # Main quiz interface
│   └── result.html      # Score page
└── static/              # Optional: CSS, images, JS (if any)

### Notes
* Both devices must be on the **same network**
* Allow access if Windows Firewall prompts you
* If it doesn’t work, check firewall settings

##  How It Works
* Questions are stored in a Python list
* Flask serves the page using `render_template()`
* User selects answers via an HTML form
* On submission:
  * Answers are checked
  * Score is calculated
  * Result is displayed
    
## Future Improvements
Add more questions dynamically from a database
Timer for each question
User authentication to save scores
Leaderboard to compare scores

## Author
Grace Maina

## License
This project is open-source and free to use.
