const like_btn = document.querySelector('like_button');
like_btn.classList.toggle('like')

like_btn.addEventListener('click', )

function submit(){
  // サーバーに送信するリクエストの設定

  $.ajax({
    // javascript内でDTLを書いてもダメ。urlをしっかり書く or html内仁鶴
    'url': '/like/',
    'type': 'POST',
    'data': {
      // 左のvalueは
        'value': $('#ajax-value').val()
    },
    'dataType': 'json'
  })
  // 通信成功時の処理
  .done(function(data){
    like_btn.classList.toggle('like')
  })
  // 通信失敗時の処理
  .fail(function(response){
    console.log(response);
  })
}



myChart = null;

function displayChart(val, class_name) {
  const ctx = document.getElementById(class_name).getContext('2d');

  if (myChart){
    console.log('destroy');
    myChart.destroy();
  }
  myChart = new Chart(ctx, {
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


// ページが完全に読み込まれた後に実行,, window onloadは後続にwindow.onloadを書くと上書きされてしまう。
// window.onload = function() {
  // httpリクエストをサーバーに送るための関数, get_numbersはdjangoでエンドポイントを設定
 function get_values() {
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

window.addEventListener("load", get_values());

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
    $("#ajax-button").on("click", function(){ submit(); });
});

function submit(){
  // サーバーに送信するリクエストの設定

  $.ajax({
    // javascript内でDTLを書いてもダメ。urlをしっかり書く or html内仁鶴
    'url': '/graph/',
    'type': 'POST',
    'data': {
      // 左のvalueは
        'value': $('#ajax-value').val()
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
  }).always( function(){;

  setTimeout(submit, 5000);
  })
}


let chart_data = {
  e : 5,
  b : 8,
  a : 9,
  d : 6,
  c : 7,

}

let sorted_data = Object.entries(chart_data)
                .sort((a, b) => b[1] - a[1]);

let label_name = [];
let chart_sorted_data = [];

for(let data of sorted_data){
label_name.push(data[0]);
chart_sorted_data.push(data[1]);
}


function CircleGraph (label_name, chart_sorted_data) {
let context = document.querySelector("#circle_graph").getContext('2d');

my_circle_Chart = new Chart(context, {
  type: 'pie',
  data: {
    labels: label_name,
    datasets: [{
      data: chart_sorted_data
    }]
  },
  options: {
    responsive: false,
  }
});
}

window.addEventListener("load" , CircleGraph(label_name, chart_sorted_data))