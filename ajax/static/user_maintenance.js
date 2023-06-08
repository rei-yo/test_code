document.addEventListener('DOMContentLoaded', function() {

    // サーバから認証されたユーザの情報を取得
    // getSessionUser(function(resJson) {
        // console.log("=== resJson ===");
        // console.log(resJson);

        // ヘッダの初期化
        // initializeHeader(resJson.user);
        // 検索処理の初期化
        initializeSearch();
        // 登録ダイアログの初期化
        // initializeRegisterDialog();
        // 編集ダイアログの初期化
        // initializeEditDialog();
    // });
});

function initializeSearch() {
    getSearchButton().addEventListener('click', function() {
        search();
    });
}


function search() {
    // clearMessage();
    // clearSearchResult();

    reqData = {
        mieruka_user_id: getUserId().value,
        group_id:getGroupId().value,
        user_name: getName().value,
        email: getEmail().value,
        create_datetime_from: getCreateDatetimeFrom().value,
        create_datetime_to: getCreateDatetimeTo().value,
        update_datetime_from: getUpdateDatetimeFrom().value,
        update_datetime_to: getUpdateDatetimeTo().value,
        delete_flg: getSearchConditionForBoolean('delete_flg')
    };
    // json形式へ変換（辞書型のデコード）
    reqJson = JSON.stringify(reqData); 
    post("/search", reqJson, function(resJson) {
        if (resJson.records.length == 0) {
            getMessageField().innerHTML = "該当のデータがありません。";
        } else {
            // thead
            var row = getSea
            rchResultTableHead().insertRow();
            row.appendChild(createTH('ID'));
            row.appendChild(createTH('GROUP_ID'));
            row.appendChild(createTH('USER_NAME', 'col_std'));
            row.appendChild(createTH('EMAIL', 'col_wide'));
            row.appendChild(createTH('CREATE_DATETIME', 'col_std'));
            row.appendChild(createTH('UPDATE_DATETIME', 'col_std'));
            row.appendChild(createTH('DELETE_FLG'));

            // tbody
            for (record of resJson.records) {
                row = getSearchResultTableBody().insertRow();
                row.appendChild(createTD(record.mieruka_user_id, "right"));
                row.appendChild(createTD(record.group_id, "right"));
                row.appendChild(createTD(record.user_name, "left"));
                row.appendChild(createTD(record.email, "left"));
                row.appendChild(createTD(record.create_datetime, "center"));
                row.appendChild(createTD(record.update_datetime, "center"));
                row.appendChild(createTD(record.delete_flg == "1" ? "✓" : "-", "center"));

                // row.onclick = function() {
                //     // 最新のユーザ情報をサーバから取得する
                //     id = this.cells[0].innerText;
                //     find_by_id(id);
                // };
            }
        }
    });
}





function getSearchButton() {
    return document.getElementById('search_button');
}

// 検索結果テーブルのtheadの取得
function getSearchResultTableHead() {
    return document.getElementById("search_result_table_head");
}

// 検索結果テーブルのtbodyの取得
function getSearchResultTableBody() {
    return document.getElementById("search_result_table_body");
}

// mieruka_user_idの取得
function getUserId() {
    return document.getElementById('mieruka_user_id');
}

//group_idの取得
function getGroupId() {
    return document.getElementById('group_id');
}

// 名前の取得
function getName() {
    return document.getElementById('user_name');
}

// Eメールの取得
function getEmail() {
    return document.getElementById('email');
}

// 作成日時Fromの取得
function getCreateDatetimeFrom() {
    return document.getElementById('create_datetime_from');
}

// 作成日時Toの取得
function getCreateDatetimeTo() {
    return document.getElementById('create_datetime_to');
}

// 更新日時Fromの取得
function getUpdateDatetimeFrom() {
    return document.getElementById('update_datetime_from');
}

// 更新日時Toの取得
function getUpdateDatetimeTo() {
    return document.getElementById('update_datetime_to');
}

// 削除フラグの取得
function getDeleteFlg() {
    return document.getElementsByName('delete_flg');
}

function getSearchConditionForBoolean(name) {
    elements = document.getElementsByName(name);
    // 1: True値を検索, 2: False値を検索, "": 両方を検索
    for (i = 0; i < 3; i++) {
        if (elements.item(i).checked) {
            return elements.item(i).value;
        }
    }
}

// THの作成
function createTH(value, clsname=null) {
    th = document.createElement('th');
    th.innerHTML = value;
    if (clsname != null) {
        th.classList.add(clsname);
    }
    return th;
}

function createTD(value, clsname=null) {
    td = document.createElement('td');
    td.innerHTML = value;
    if (clsname != null) {
        td.classList.add(clsname);
    }
    return td;
}