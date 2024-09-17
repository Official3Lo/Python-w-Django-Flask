from flask import Flask, render_template, request, flash
from forms import ContactForm #dont forget to remove 12. from forms.py file

app = Flask(
    __name__
)

app.secret_key = 'development key'

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validaate() == False:
            flash('All fields are required')
            return render_template('contact.html')
        else:
            return render_template('success.html')
    if request.method == 'GET':
        return render_template('contact.html', form = form)
    
if __name__ == '__main__':
    app.run(debug=True)

    