from flask import Flask, render_template, request
import pickle

app=Flask(__name__)
tokenizer= pickle.load(open('models/cv.pkl', "rb"))
model=pickle.load(open('models/clf.pkl', "rb"))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text=request.form.get('email_content')
    tokenized_email=tokenizer.transform(email_text)
    predictions=model.transform(tokenized_email)
    predictions=1 if prediction==1 else -1
    return render_template('index.html', predictions=predictions, email_text=email_text)


if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)