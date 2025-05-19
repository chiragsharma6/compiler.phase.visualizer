from flask import Flask, render_template, request, jsonify
# from parser import generate_parse_tree


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lexical')
def lexical():
    return render_template('lexical.html')

@app.route('/syntax')
def syntax():
    return render_template('syntax.html')

@app.route('/semantic')
def semantic():
    return render_template('semantic.html')

@app.route('/intermediate')
def intermediate():
    return render_template('intermediate.html')

@app.route('/optimization')
def optimization():
    return render_template('optimization.html')

@app.route('/generation')
def generation():
    return render_template('generation.html')



from lexer import lex  # Import your lexer

@app.route('/tokenize', methods=['POST'])
def tokenize():
    code = request.json['code']
    try:
        tokens = lex(code)
        return jsonify(tokens=tokens)
    except Exception as e:
        return jsonify(error=str(e)), 400
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
# @app.route('/parse', methods=['POST'])
# def parse():
#     data = request.get_json()
#     expr = data.get('expression', '')
#     try:
#         tree = generate_parse_tree(expr)
#         return jsonify(tree)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)