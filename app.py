from flask import Flask, render_template, jsonify

app = Flask(__name__)

menu = [
    {"name": "Chicken Burger", "price": 129, "description": "Crispy chicken with fresh lettuce and house sauce.", "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=900&q=85"},
    {"name": "Beef Burger", "price": 159, "description": "Juicy beef patty with cheese and fresh vegetables.", "image": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=900&q=85"},
    {"name": "Creamy Carbonara", "price": 149, "description": "Creamy pasta finished with herbs and parmesan.", "image": "https://images.unsplash.com/photo-1612874742237-6526221588e3?auto=format&fit=crop&w=900&q=85"},
    {"name": "Classic Spaghetti", "price": 120, "description": "A comforting pasta favorite with tomato sauce.", "image": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=900&q=85"},
    {"name": "French Fries", "price": 79, "description": "Golden, crispy fries served hot.", "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=900&q=85"},
    {"name": "Iced Coffee", "price": 89, "description": "Chilled coffee for a refreshing break.", "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?auto=format&fit=crop&w=900&q=85"}
]

@app.route("/")
def home():
    return render_template("index.html", menu=menu)

@app.route("/api/menu")
def api_menu():
    return jsonify(menu)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
