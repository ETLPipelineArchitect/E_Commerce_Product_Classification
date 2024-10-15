from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

s3_client = boto3.client('s3')

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['file']
    bucket_name = 'your-bucket-name'
    s3_client.upload_fileobj(file, bucket_name, file.filename)
    return jsonify({'message': 'Upload Successful', 'file_name': file.filename}), 200

if __name__ == '__main__':
    app.run(debug=True)
