// Ajaxレスポンスが、1つでも未認証の場合には、1回だけ処理するためのフラグ
let unauthorized_flg = false;

// Ajax通信
function post(url, reqJson, callback) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if (xhr.status == 200) {
                var response = xhr.responseText;
                console.log(response);
                let resJson = eval("(" + response + ")");
                    callback(resJson);
                } else {
                    callback(resJson);
                }
            } else {
                console.log("Ajax failed.(HTTP status: " + xhr.status + ")");
                alert("Unexpected error occurred.(HTTP status:" + xhr.status + ")");
            }
        };
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.send(reqJson);
}