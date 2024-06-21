from flask import Flask, request, render_template
import csv

app = Flask(__name__)

def read_links_from_csv(file_path):
    links = []
    with open(file_path, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            links.append(row)
    return links

def filter_links_by_keyword(links, keyword):
    return [link for link in links if keyword.lower() in link['name'].lower()]

@app.route('/search', methods=['GET', 'POST'])
def search_links():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        file_choice = request.form.get('file_choice')
        
        file_paths = {
            'file1': r'C:\Users\T0294547\Chatbot2\MSDP.csv',
            'file2': r'C:\Users\T0294547\Chatbot2\VPN.csv',
            'file3': r'C:\Users\T0294547\Chatbot2\DC.csv'
        }
        
        selected_file = file_paths.get(file_choice)
        if not selected_file:
            return render_template('index.html', links=[], keyword=keyword, error="Invalid file choice")
        
        links = read_links_from_csv(selected_file)
        filtered_links = filter_links_by_keyword(links, keyword)
        return render_template('index.html', links=filtered_links, keyword=keyword, error="")
    return render_template('index.html', links=[], keyword='', error='')

@app.route('/')
def index():
    return render_template('index.html', links=[], keyword='', error='')

if __name__ == '__main__':
    app.run(debug=True , port=4000)
