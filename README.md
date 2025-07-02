# Instagram Login Clone (Educational Project)

This project replicates the Instagram login interface and demonstrates basic form handling using HTML, JavaScript, and a Flask backend. When users enter login details, the data is saved to an Excel file, and they are redirected to the official Instagram site.

> ⚠️ This project is created purely for **educational purposes**. It must **not** be used for unauthorized or unethical activities. Do not deploy or misuse this project.

---

## 🔧 Technologies Used

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python (Flask)
- **Data Storage:** Excel using `openpyxl`
- **Others:** `package.json` (for optional frontend package tracking)

---

## 📁 Project Structure

```

instagram-login-clone/
├── index.html          # Instagram-style login page
├── script.js           # Handles form submission
├── server.py           # Flask backend logic
├── login\_data.xlsx     # Stores login data (demo only)
├── package.json        # Optional (frontend packages)
└── README.md

````

---

## 🚀 How to Run

### Backend

```bash
# Step 1: Install required Python packages
pip install flask openpyxl

# Step 2: Run the backend server
python server.py
````

### Frontend

* Open `index.html` in any modern browser
* Submit login credentials
* You’ll be redirected to [Instagram](https://www.instagram.com)
* Submitted data is saved locally to `login_data.xlsx`

---

## 📸 Preview

*(Add screenshot here if available)*
![Preview](https://via.placeholder.com/700x400?text=Instagram+Login+Clone)

---

## 🎯 Learning Objectives

* Frontend form UI replication
* JavaScript form interaction
* Sending form data to Flask
* Writing to Excel from Python

---

## 🛑 Disclaimer

This project is intended **only for learning purposes**.
Never collect or store real user data without consent.
Avoid public deployment of this clone to prevent misuse.
The author is not responsible for any unethical usage.

---

## 👤 Author

**Ravi Sai Vinay M**
GitHub: [@Ravi123sv](https://github.com/Ravi123sv)

---

## 📘 License

This project is licensed under the [MIT License](LICENSE).

```
