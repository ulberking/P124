from flask import Flask,jsonify,request
app=Flask(__name__)
@app.route('/myCity')
def myCity():
    return 'Chateauguay'
if(__name__=='__main__'):
    app.run(debug=True)