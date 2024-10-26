from flask import Flask, request, jsonify
from flask_cors import CORS
# Import your recommendation script functions here
# from recommendation_script import generate_recommendations

app = Flask(__name__)
CORS(app)

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    store_id = request.args.get('store_id')
    try:
        # Replace this with your actual recommendation generation logic
        recommendations = generate_recommendations(store_id)
        return jsonify(recommendations)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if name == '__main__':
    app.run(debug=True, port=5000)
