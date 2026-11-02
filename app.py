"""Minimal Flask web app for the food ordering application."""
from flask import Flask, flash, redirect, render_template, request, session, url_for

from cart import Cart
from ordering import MENU

app = Flask(__name__)
app.secret_key = "dev-secret-change-me"

USERS = {"admin": "admin123"}


def get_cart():
    return Cart(session.get("cart", {}))


def save_cart(cart):
    session["cart"] = cart.items


@app.before_request
def require_login():
    if request.endpoint not in ("login", "health", "index", "static") and "user" not in session:
        return redirect(url_for("login"))


@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if USERS.get(username) == password:
            session["user"] = username
            return redirect(url_for("menu"))
        error = "Invalid username or password"
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/menu")
def menu():
    cart = get_cart()
    return render_template(
        "menu.html", user=session["user"], menu=MENU, cart_count=sum(cart.items.values())
    )


@app.route("/cart")
def view_cart():
    cart = get_cart()
    return render_template(
        "cart.html", cart=cart, menu=MENU, subtotal=cart.subtotal(), total=cart.total(10)
    )


@app.route("/cart/add", methods=["POST"])
def add_to_cart():
    cart = get_cart()
    try:
        cart.add_item(request.form["item"], int(request.form.get("qty", 1)))
        save_cart(cart)
        flash(f"Added {request.form['item']} to cart")
    except (ValueError, KeyError) as e:
        flash(str(e))
    return redirect(url_for("menu"))


@app.route("/cart/update", methods=["POST"])
def update_cart():
    cart = get_cart()
    try:
        cart.update_quantity(request.form["item"], int(request.form["qty"]))
        save_cart(cart)
    except (ValueError, KeyError) as e:
        flash(str(e))
    return redirect(url_for("view_cart"))


@app.route("/cart/remove", methods=["POST"])
def remove_from_cart():
    cart = get_cart()
    cart.remove_item(request.form.get("item"))
    save_cart(cart)
    return redirect(url_for("view_cart"))


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
