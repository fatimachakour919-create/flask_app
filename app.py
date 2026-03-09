from flask import Flask


app =Flask(_name_)

@app.route("/")
def home():
    return "hello devops - docker ci pipeline"

if _name=="main_":
    app.run(host="0.0.0.0", port=5000)