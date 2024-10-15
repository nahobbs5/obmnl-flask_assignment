# Import libraries
from flask import Flask , request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)


# Create operation
@app.route("/add", methods = ['GET', 'POST'])
def add_transaction():

    if request.method == "POST":
         # Create a new transaction object using form field values
         transaction = {
              'id': len(transactions)+1,
              'date': request.form['date'],
              'amount': float(request.form['amount'])
         }
         # Apend new transaction to transactions list
         transactions.append(transaction)

         #redirect to transactions list page after adding new transaction
         return redirect(url_for("get_transactions"))

    # if request method is GET, render the form template to display the add transaction form
    return render_template("form.html")


# Update operation
@app.route("/edit/<int:transaction_id>", methods = ['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == "POST":
        #Extract updated values from form fields
        date = request.form['date'] #get "date" field value from form
        amount = float(request.form['amount']) #get the 'amount' field value from the form and convert to float


        #find transaction with matching ID and update values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date #update date field
                transaction['amount'] = amount #update amount field
                break
        
        #Redirect to transactions list page after updating transaction
        return redirct(url_for("get_transactions"))

    #if request method is GET, find transaction with matching ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            #Render edit form template and pass transaction to be edited
            return render_template("edit.html", transaction = transaction)

    #if the transaction with specified ID is not found, handle this case
    return {"Message: " "Transaction not found"}, 404

# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break

    #redirect to transactions page after deletion
    return redirct(url_for("get_transactions"))


# Run the Flask app
if __name__ == "__main__":
    app.run(debug = True)
    