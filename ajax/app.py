import json
import logging
from datetime import timedelta
from flask import Flask, redirect, render_template, request, session, url_for, flash
from logic.user_logic import UserEntityLogic
# from util.logger_factory import LoggerFactory
# from util.config import Config


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """index画面を表示します。
    Args:
        -
    Returns:
        index.html
    """

    return render_template("index.html")


@app.route("/find_by_email", methods=["POST"])
def find_by_email():
    """指定されたEメールに該当するユーザ情報を返却します。
    Args:
        リクエストJSONに以下が含まれます。
        - email: Eメールアドレス
    Returns:
        以下をJSON形式で返却します。
        成功の場合：
        - status: success
        - user: ユーザ情報
        失敗の場合：
        - status: unknown user
        - message: エラーメッセージ
    """
    # logger.info("find_by_email() called.")

    req_json = request.get_json()
    # if logger.isEnabledFor(logging.DEBUG):
        # logger.debug(f"=== request json ===\n{req_json}")

    email = req_json["email"]
    entity = UserEntityLogic().find_by_email(email)
    # logger.info(f"entity: {entity}")

    if entity != None:
        session.permanent = True
        # session[WEB_SESSION_KEY_USER] = create_session_user(entity)
        # logger.info(f"session: ({session[WEB_SESSION_KEY_USER]})")

        res_dict = {
            "status": "success",
            # "user": session[WEB_SESSION_KEY_USER],
        }
    else:
        res_dict = {
            "status": "unknown user",
            "message": f"Unknown user.<br/>({email})",
        }
    return encodeJSON(res_dict)




def encodeJSON(res_dict):
    """指定されたdict形式のデータをJSONにして返却します。
    Args:
        res_dict: レスポンスするdict形式のデータ
    Returns:
        JSONデータ
    """
    res_json = json.dumps(res_dict)

    # if logger.isEnabledFor(logging.DEBUG):
        # logger.debug("=== response json ===\n" + res_json)

    return res_json



@app.route("/search", methods=["POST"])
def search():
    """ユーザの検索処理を行います。
    Args:
        リクエストJSONに以下が含まれます。
        - name: 名前
        - email: Eメールアドレス
        - create_datetime_from: 作成日時From
        - create_datetime_to: 作成日時To
        - update_datetime_from: 更新日時From
        - update_datetime_to: 更新日時To
        - delete_flg: 削除フラグ
    Returns:
        以下をJSON形式で返却します。
        - status: success
        - records: ユーザ情報のリスト
    """
        
    # logger.info("search() called.")

    print("serch_called")
    req_json = request.get_json()
    
    # if logger.isEnabledFor(logging.DEBUG):
    #     logger.debug(f"=== request json ===\n{req_json}")

    mieruka_user_id = req_json["mieruka_user_id"]
    group_id = req_json["group_id"]
    user_name = req_json["user_name"]
    email = req_json["email"]
    create_datetime_from = req_json["create_datetime_from"]
    create_datetime_to = req_json["create_datetime_to"]
    update_datetime_from = req_json["update_datetime_from"]
    update_datetime_to = req_json["update_datetime_to"]
    delete_flg = req_json["delete_flg"]
    
    entity_list = UserEntityLogic().search(
        mieruka_user_id,
        group_id,
        user_name,
        email,
        create_datetime_from,
        create_datetime_to,
        update_datetime_from,
        update_datetime_to,
        delete_flg,
    )

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)