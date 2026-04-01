import requests

def test_api():
    url = "http://localhost:5001/api/graph/ontology/generate"
    # The API expects:
    # files: uploaded files
    # simulation_requirement: str
    with open('pytest.txt', 'w') as f:
        f.write("This is a dummy text file for testing.")

    files = {'files': open('pytest.txt', 'rb')}
    data = {
        'simulation_requirement': 'Testing the ontology generation API',
        'project_name': 'Test Project'
    }

    print("Sending request...")
    response = requests.post(url, files=files, data=data)
    print("Status code:", response.status_code)
    try:
        json_data = response.json()
        print("Response JSON:", json_data)
        if 'traceback' in json_data:
            print("Traceback:")
            print(json_data['traceback'])
    except Exception as e:
        print("Failed to parse JSON:", response.text)

if __name__ == "__main__":
    test_api()
