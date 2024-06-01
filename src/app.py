from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

processed_data = None

# Function to process data
def process_data(data):
    # Dummy data processing logic, just reversing the input string
    processed_data = data[::-1]
    return processed_data

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )
@app.route("/process_data", methods=["POST"])
def process_data_endpoint():
    global processed_data
    # Assuming input data is passed as JSON in the request body
    data = request.json.get("data")
    if data is None:
        return jsonify(error="No data provided"), 400

    processed_data = process_data(data)
    return jsonify(input_data=data, processed_data=processed_data)

@app.route("/display")
def display_processed_data():
    global processed_data
    if processed_data is None:
        return jsonify(error="No processed data available"), 404

    return jsonify(processed_data=processed_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
