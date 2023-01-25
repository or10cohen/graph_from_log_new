import json
import requests
import base64

# access_token = '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'
# test_file = 'test_file_1.png'

def upload_to_github(file_path, access_token):
    headers = {'Authorization': 'Token ' + access_token}
    file_name = file_path.split("/")[-1]
    url = 'https://api.github.com/repos/or10cohen/graph_from_log_new/contents/graphs/'+file_name

    # Open the file and read the content
    with open(file_path, 'rb') as f:
        file_content = f.read()
    # Encode the file content to base64
    encoded_file_content = base64.b64encode(file_content).decode()
    # Prepare the data for the PUT request
    data = json.dumps({
        'message': 'Upload '+file_name,
        'content': encoded_file_content
    })

    # Make the PUT request to upload the file
    response = requests.put(url, headers=headers, data=data)

    # Print the status code of the response
    print(response.status_code)

    if response.status_code == 201:
        print('File uploaded successfully')
    else:
        print('Upload failed with status code', response.status_code)

# upload_to_github(test_file, access_token)