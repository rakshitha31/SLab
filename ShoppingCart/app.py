from flask import Flask, request, render_template, url_for, session, redirect

app = Flask(__name__)

items = [
    { "name": "Xbox One S" },
    { "name": "PS4 Pro" },
    { "name": "PS4 Slim" }
]

@app.route("/", methods=["GET"])
def index():
    if session.get(items[0]["name"]) or session.get(items[1]["name"]) or session.get(items[2]["name"]):
        store = [
            { items[0]["name"]: session[items[0]["name"]] },
            { items[1]["name"]: session[items[1]["name"]] },
            { items[2]["name"]: session[items[2]["name"]] }
        ]
    else:
        store = []
    data = [
        { "items": items },
        { "store": store }
    ]
    print (data)
    return render_template("index.html", data=data)

@app.route("/submit", methods=["POST"])
def submit():
    select = request.form.get("opt")
    quantity = request.form.get("quan")

    if select not in session:
        session[select] = int (quantity)
    else:
        session[select] += int(quantity)
    return redirect(url_for('index'))

@app.route("/cart", methods=["POST"])
def cart():
    cart = [
        { items[0]["name"]: session[items[0]["name"]] },
        { items[1]["name"]: session[items[1]["name"]] },
        { items[2]["name"]: session[items[2]["name"]] }
    ]
    msg = { "status" : 1, "cart": cart }
    return render_template("cart.html", msg=msg)
    

# Always keep debug=True to debug Internal Server Error and other verbose logging
if __name__ == "__main__":
    app.secret_key = "yolo"
    app.run(host='localhost', port=8080, debug=True)