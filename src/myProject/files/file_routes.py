from flask import Blueprint, request, jsonify, render_template, send_file, Response
import io
from src.myProject.files.file_db import upload_file, download_file

file_routes = Blueprint("file_routes", __name__)


@file_routes.route("/file", methods=["GET"])
def template():
    return render_template("files.html")


@file_routes.route("/upload", methods=["POST"])
def upload():
    try:
        upload_file(request.files["file"])
        return "File has been uploaded successfully"
    except Exception as e:
        print(e, "exception")
        return (
            jsonify(error=str(e)),
            400,
        )  # 400 is the HTTP status code for "Bad Request"


@file_routes.route("/download/<int:id>", methods=["GET"])
def download(id):
    try:
        file_data = download_file(id)
        file_content = file_data[2]
        response = Response(file_content, mimetype="application/octet-stream")
        response.headers.set("Content-Disposition", "attachment", filename=file_data[1])
        return response
    # with open(file_data[1], "wb") as f:
    #         f.write(file_data[2])
    #     return send_file(file_data[1], as_attachment=True) is for store the file in project folder
    
    #    return io.BytesIO(file_data) is for binary output
    except Exception as e:
        print(e, "exception")
        return (
            jsonify(error=str(e)),
            400,
        )  # 400 is the HTTP status code for "Bad Request"
