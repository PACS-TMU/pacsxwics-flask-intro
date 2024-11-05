from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    #define our list of dictionaries where each dictionary represents a project (Image, Title, and Description)
    projects = [{"image": "/static/images/project_img.jpg", 
                 "title":"PROJECT TITLE", 
                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eros eros, imperdoet vitae mollis ut, sagittis et ante.",
                 "github": "https://github.com/"},
                {"image": "/static/images/project_img.jpg", 
                 "title":"PROJECT TITLE", 
                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eros eros, imperdoet vitae mollis ut, sagittis et ante.",
                 "github": "https://github.com/"},
                {"image": "/static/images/project_img.jpg", 
                 "title":"PROJECT TITLE", 
                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eros eros, imperdoet vitae mollis ut, sagittis et ante.",
                 "github": "https://github.com/"},
                {"image": "/static/images/project_img.jpg", 
                 "title":"PROJECT TITLE", 
                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eros eros, imperdoet vitae mollis ut, sagittis et ante.",
                 "github": "https://github.com/"}]
    
    return render_template('index.html', projects = projects)
@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
