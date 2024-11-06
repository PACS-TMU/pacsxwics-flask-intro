from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    #define our list of dictionaries where each dictionary represents a project (Image, Title, and Description)
    projects = [{"image": "/static/images/project_1_img.jpg", 
                 "title":"PROJECT TITLE 1", 
                 "description": "Yuji Itadori is the main protagonist of the Jujutsu Kaisen series. He is the son of Jin Itadori and Kaori Itadori, and the grandson of Wasuke Itadori.",
                 "github": "https://github.com/"},
                {"image": "/static/images/project_2_img.jpg", 
                 "title":"PROJECT TITLE 2", 
                 "description": "Megumi is a Jujutsu sorcerer utilizing the Ten Shadows Technique to fight against Curse Demons. Past his cold exterior, Megumi wishes to protect people he values.",
                 "github": "https://github.com/"},
                {"image": "/static/images/project_3_img.jpg", 
                 "title":"PROJECT TITLE 3", 
                 "description": "Nobara Kugisaki is a first-year student at Tokyo Jujutsu High, an academy that trains students to fight Cursed Spirits using Cursed Techniques.",
                 "github": "https://github.com/"},
                {"image": "/static/images/project_4_img.jpg", 
                 "title":"PROJECT TITLE 4", 
                 "description": "Suguru Geto is an antagonist in both the Jujutsu Kaisen series. He was originally a student of Masamichi Yaga's alongside Satoru Gojo and Shoko Ieiri at Tokyo Jujutsu High.",
                 "github": "https://github.com/"}]
    
    return render_template('index.html', projects = projects)
@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
