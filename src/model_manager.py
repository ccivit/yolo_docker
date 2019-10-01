import os

def download_url(file_url,dest_filename):
    os.system('''curl "''' + file_url + '''" -o ''' + dest_filename)

def model_exists(file_path):
    return os.path.isfile(file_path)
 
def find_github_model_url(config):
    # code based on:
    # https://stackoverflow.com/questions/25923939/how-do-i-download-binary-files-of-a-github-release
    delete_temp_files = True
    
    import json,time
    author = config['repo_author']
    repo = config['repo']
    try:
        github_token = config['token']
        token_available = True
    except:
        print('No token provided, trying without token...')
        token_available = False
    
    print('Finding asset location from latest',repo)
    if token_available:
        curl_command = 'curl -H "Authorization: token "''' + github_token + ' \
            https://api.github.com/repos/' + author + '/' + repo + '/releases/latest'
    else:
        curl_command = 'curl -H \
            https://api.github.com/repos/' + author + '/' + repo + '/releases/latest'  
        
    temp_json_file = 'temp.json' 
    temp_config_file = 'temp.txt' 
    os.system(curl_command + ' > ' + temp_json_file) 
    json_file = json.loads(open(temp_json_file).read())
    
    try:
        asset_url = json_file['assets'][0]['url'] 
        print('Asset ID: ',json_file['assets'][0]['name']
        print('Asset found')
        print(asset_url)
        print('Determining AWS url...')
        curl_command2='''curl -H "Authorization: token ''' + github_token + '''" \
             -H "Accept:application/octet-stream" \
             -i ''' + asset_url 
 
        os.system(curl_command2 + ' > ' + temp_config_file) 

        with open(temp_config_file) as f:
            content = f.readlines() 
            content = [x.strip() for x in content] 
            for line in content:
                if line[0:9] == 'location:':
                    file_url = line[10:]
        if delete_temp_files == True:
            os.remove(temp_json_file)
            os.remove(temp_config_file)
        return file_url
    except:
        print('Asset not found. Check github credentials')
        return 1
    


def check_and_download(model_path):
    import os, yaml
    model_name = os.path.basename(model_path)
    
    if model_exists(model_path):
        print('Model found at',model_path)
    else:
        with open('src/models.yml') as ymlfile:
            config = yaml.load(ymlfile, Loader=yaml.BaseLoader)#yaml.load(input, Loader=yaml.FullLoader
        print('Model not found. Trying to download from repo...')
        model_url = find_github_model_url(config[model_name])
        print('Downloading model from AWS...')
        try:
            download_url(model_url,model_path)
            print(model_name,'was downloaded sucessfully.')
        except:
            print('ERROR: Model could not be downloaded.')
            return 1
    return 0
              
if __name__ == '__main__':
    print('Checking if models are found locally...')
    check_and_download('bin/yolov3.weights')
              
