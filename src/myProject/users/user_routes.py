from flask import Blueprint, jsonify, request, render_template, send_file
import pandas as pd
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


@user_routes.route("/users/reports", methods=["GET"])
def get_reports():
    data = get_users()
    column_names = ["Id", "Name", "Email", "Age"]
    df = pd.DataFrame(data, columns=column_names)
    df.index = df.index + 1
    df.insert(0, "Serio.No", df.index)
    report_file_path = "report.csv"
    df.to_csv(report_file_path, index=False)
    return send_file(report_file_path, as_attachment=True)
