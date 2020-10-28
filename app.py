from flask import Flask,render_template,request,jsonify
import numpy as np
import joblib
import config
app = Flask(__name__)
#model = pickle.load(open('model.pkl','rb'))

model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')


   




@app.route('/football', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        #operation=request.form['operation']
        potential=int(request.form['potential'])
        finishing=int(request.form['finishing'])
        stamina=int(request.form['stamina'])
        positioning=int(request.form['positioning'])
        strength=int(request.form['strength'])
        








        int_features = []
        int_features.append(potential)
        int_features.append(finishing)
        int_features.append(stamina)
        int_features.append(positioning)
        int_features.append(strength)
        

        

        final_features = [np.array(int_features)]

        print(final_features)

        



        prediction = model.predict(final_features)

        print(prediction)

        prediction = np.round(prediction[0])

        print(type(prediction))

        prediction = prediction.astype(int)

        print(type(prediction))

        


        # not_cheating = prediction[0][0]
        # cheating = prediction[0][1]

        # if not_cheating > cheating:
        #     verdict = int(not_cheating*100)
        #     predict = 'not cheating'
        # else:
        #     verdict = int(cheating*100)   
        #     predict = 'cheating' 

        # prediction = [verdict, predict]   



        

        
        return render_template('results.html',result=prediction)  


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=config.PORT, debug=config.DEBUG_MODE)           