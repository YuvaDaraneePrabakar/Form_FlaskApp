from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


temp_data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Store the data in temporary storage
        temp_data.append({'name': name, 'email': email, 'message': message})

        # Redirect to the thank you page
        return redirect(url_for('thank_you'))

    return render_template('index.html')

@app.route('/thank_you')
def thank_you():
    # Retrieve the last submitted data from temporary storage
    last_entry = temp_data[-1] if temp_data else None

    return render_template('thank_you.html', last_entry=last_entry)

if __name__ == '__main__':
    app.run(debug=True)
