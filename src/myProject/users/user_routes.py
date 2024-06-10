from flask import Blueprint, jsonify, request, render_template
from src.myProject.users.user_db import (
    get_users,
    add_user,
    get_user_by_id,
    delete_user,
    update_user,
)

user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/user", methods=["GET"])
def template():
    return render_template("user.html")


@user_routes.route("/users", methods=["GET", "POST"])
def get_user():
    print("get_user", request.method)
    if request.method == "GET":
        rows = get_users()
        data = []
        for row in rows:
            result = {"id": row[0], "name": row[1], "email": row[2], "age": row[3]}
            data.append(result)
        return jsonify(data)
    elif request.method == "POST":
        try:
            add_user(request)
            return jsonify({"message": "User saved successfully"}), 200
        except Exception as e:
            print(e, "exception")
            return (
                jsonify(error=str(e)),
                400,
            )  # 400 is the HTTP status code for "Bad Request"
    else:
        return jsonify({"message": "Method Not Allowed"}), 405


@user_routes.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def get_userbyid(id):
    if request.method == "GET":
        row = get_user_by_id(id)
        data = {
            "id": row["id"],
            "name": row["name"],
            "age": row["age"],
            "email": row["email"],
            # add more keys as needed
        }
        return jsonify(data)
    elif request.method == "PUT":
        try:
            update_user(id, request)
            return jsonify({"message": "User updated successfully"}), 200
        except Exception as e:
            print(e, "exception")
            return (
                jsonify(error=str(e)),
                400,
            )  # 400 is the HTTP status code for "Bad Request"
    elif request.method == "DELETE":
        try:
            delete_user(id)
            return jsonify({"message": "User deleted successfully"}), 200
        except Exception as e:
            print(e, "exception")
            return jsonify(error=str(e)), 400
    else:
        return jsonify({"message": "Method Not Allowed"}), 405
