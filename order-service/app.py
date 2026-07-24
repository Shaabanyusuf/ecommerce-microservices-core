import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

INVENTORY_SERVICE_URL = os.getenv("INVENTORY_SERVICE_URL", "http://localhost:5001")

@app.route("/order", methods=["POST"])
def create_order():
    data = request.get_json()
    if not data or "item_id" not in data or "quantity" not in data:
        return jsonify({"error": "Invalid payload, 'item_id' and 'quantity' are required"}), 400

    item_id = data["item_id"]
    quantity = data["quantity"]

    try:
        response = requests.get(f"{INVENTORY_SERVICE_URL}/inventory/{item_id}")
        if response.status_code == 404:
            return jsonify({"error": "Item not found in inventory"}), 404
        elif response.status_code != 200:
            return jsonify({"error": "Failed to communicate with inventory service"}), 502

        item_data = response.json()

        if item_data["stock"] < quantity:
            return jsonify({"error": "Insufficient stock available", "available_stock": item_data["stock"]}), 400

        total_price = item_data["price"] * quantity
        order_result = {
            "order_status": "SUCCESS",
            "item_id": item_id,
            "item_name": item_data["name"],
            "quantity": quantity,
            "total_price": total_price
        }
        return jsonify(order_result), 201

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Inventory service is unreachable", "details": str(e)}), 503

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "service": "order-service"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
