from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Load expenses from CSV
def load_expenses():
    expenses = []
    try:
        with open('data/expenses.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses

# Save expenses to CSV
def save_expenses(expenses):
    with open('data/expenses.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        writer.writerows(expenses)

@app.route('/')
def index():
    expenses = load_expenses()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    date = request.form.get('date')
    category = request.form.get('category')
    amount = request.form.get('amount')
    description = request.form.get('description')
    
    if not all([date, category, amount, description]):
        return redirect(url_for('index'))
    
    expenses = load_expenses()
    expenses.append({
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    })
    save_expenses(expenses)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
