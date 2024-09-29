from flask import Flask, render_template, request, redirect, url_for, flash, session
import pandas as pd

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Load user data from CSV
users_df = pd.read_csv('C:\\Users\\emily\\OneDrive\\Documents\\nihaissexy\\login info.csv')

@app.route('/')
def home():
    return render_template('hl3.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the user exists in the DataFrame
    user = users_df[(users_df['username'] == username) & (users_df['password'] == password)]
    if not user.empty:
        # Successful login
        session['username'] = username
        session['role'] = user['role'].values[0]  # Store user role in session
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))  # Redirect to the dashboard page
    else:
        flash('Invalid username or password', 'danger')
        return redirect(url_for('home'))  # Redirect back to login

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'], role=session['role'])
    else:
        flash('Please log in first', 'warning')
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    flash('Logged out successfully!', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)