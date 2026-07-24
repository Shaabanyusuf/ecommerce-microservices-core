from from flask import Flask, jsonify, request

app = Flask(__name__)

inventory_db = {
    "item_1": {"name": "Mechanical Keyboard", "stock": 15, "price": 75},
    "item_2": {"name": "Gaming Mouse", "stock": 30, "price": 45},
    "item_3": {"name": "Type-C Hub", "stock": 50, "price": 25}
}

@app.route("/inventory/<item_id>", methods=["GET"])
def get_inventory(item_id):
    item = inventory_db.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"item_id": item_id, **item}), 200

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "service": "inventory-service"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)




from
