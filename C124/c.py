from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'title': 'breakefast',
        'description': 'noodle',
        'done': 'True'
    },
    {
        'id': 2,
        'title': 'game',
        'description': 'overwatch',
        'done': 'True'
    }
]


@app.route('/myName')
def showMyName():
    return '{name:Minho}'


@app.route('/adddata', methods=['POST'])
def addTask():
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'Please enter the tasks'
        })
    task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json['description'],
        'done': request.json['done']
    }
    tasks.append(task)
    return jsonify({
        'status': 'succes',
        'message': 'Ptasks enter succesfuly'
    })
@app.route('/getTask')
def getTask():
    return jsonify({
        'data':tasks
    })

if(__name__ == '__main__'):
    app.run(debug=True)
