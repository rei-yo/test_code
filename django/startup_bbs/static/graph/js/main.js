
function displayChart(val, class_name) {
  const ctx = document.getElementById(class_name).getContext('2d');
  const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      // idをラベルにする
      labels: val.labels,
      datasets: [{
        label: 'Numbers',
        // data: val.map(n => n.values)
      //   valueを取り出してデータへ
        data: val.values,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      }
    }
  });
};


// ページが完全に読み込まれた後に実行
window.onload = function() {
  // httpリクエストをサーバーに送るための関数, get_numbersはdjangoでエンドポイントを設定
  fetch('api/get_values/')
    // promiseオブジェクトからjsonを取り出す
    .then(response => {
      if (!response.ok){
        console.error('エラー');
      }else{
        // console.log(response.json());
        return response.json();
      }
    }).then(data => {
      console.log(data)
      displayChart(data, 'myChart');
        })
    .catch(error => {
      console.log(error);
    });
};



  // 更新(api)ボタンがクリックされたときの処理
  document.getElementById('update-btn').onclick = function() {
      // 新しい数字を生成して、DBに保存する
      fetch('api/update_values/', {
      method: 'POST',
      })
      .then(response => response.json())
      .then(data => {
          // 更新された数字で棒グラフを再描画する
          displayChart(data, 'myChart');
      })
      .catch(error => {
        console.log(error);
      });
  };

// ajaxでの更新部分

  window.addEventListener("load" , function (){
    // submitイベントを検知。
    $("#ajax-form").on("submit", function(){ submit(); });
});

function submit(){
  // サーバーに送信するリクエストの設定
  $.ajax({
    'url': '{% url "" %}',
    'type': 'POST',
    'data': {
      // 左のvalueは
        'value': $('value').val()
    },
    'dataType': 'json'
  })
  // 通信成功時の処理
  .done(function(data){
    console.log(data);
    displayChart(data, 'myChart')
  })
  // 通信失敗時の処理
  .fail(function(response){
    console.log(response);
  })


}
