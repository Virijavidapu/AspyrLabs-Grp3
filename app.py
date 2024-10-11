from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to convert number to string
@app.route('/<int:number>', methods= ['GET','POST'])
def number_to_string(number):
    number_str = str(number)

        # Return the result as a dictionary
    return jsonify({"number_as_string": number_str})

    
    

if __name__ == '__main__':
    app.run(debug=True)
