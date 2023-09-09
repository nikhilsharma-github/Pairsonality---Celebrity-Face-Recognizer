# we are Going to create our python flask server from this file
# A very light python webserver "Python Flask" which we are using here.

# First, we are importing all the important libraries
from flask import Flask, request, jsonify
import util


# Running the main server
app = Flask(__name__)


# Writing the simple API for the browser Call
# It has methods GET and POST for the calls
@app.route('/classify_image',
           methods=['GET', 'POST'])

# This classify image function is called by the UI
def classify_image():
    # This image data is actually a base64 string
    image_data = request.form['image_data']

    # This function classify the image we have above and gives us the result in return
    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    # Returning the final response
    return response


# Running the main method
if __name__ == "__main__":
    print("Starting python flask server for celeb recoginition")
    util.load_saved_artifacts()
    app.run(port=5000)