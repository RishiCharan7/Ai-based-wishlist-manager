from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage for the wishlist
wishlist = []

# Function to handle bot responses
def bot_response(user_input):
    user_input = user_input.lower()
    
    if "add" in user_input:
        item = user_input.split("add")[-1].strip()
        if item:
            wishlist.append(item)
            return f"{item} has been added to your wishlist."
        return "Please specify an item to add."
    
    elif "remove" in user_input:
        item = user_input.split("remove")[-1].strip()
        if item in wishlist:
            wishlist.remove(item)
            return f"{item} has been removed from your wishlist."
        return f"{item} is not in your wishlist."
    
    elif "view" in user_input or "wishlist" in user_input:
        if wishlist:
            return "Your wishlist contains: " + ", ".join(wishlist) + "."
        return "Your wishlist is currently empty."
    
    elif "bye" in user_input:
        return "Goodbye! If you need anything else, just ask!"
    
    return "I'm sorry, I didn't understand that. You can say 'add', 'remove', or 'view' to manage your wishlist."

@app.route("/")
def home():
    return render_template("index.html", wishlist=wishlist)

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["user_input"]
    response = bot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
