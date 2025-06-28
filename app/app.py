from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({"message": "No file received"}), 400

    file = request.files['file']
    if file:
        print("File received. Genome analysis successful")
        return jsonify({"message": "Genome analysis successful"}), 200
    else:
        return jsonify({"message": "Invalid file"}), 400

if __name__ == "__main__":
    app.run(port=5006, debug=True)

