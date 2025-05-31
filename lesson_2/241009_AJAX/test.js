document.addEventListener("DOMContentLoaded", function() {
    // 使用 fetch API 來獲取資料
    fetch('https://raw.githubusercontent.com/wsmwason/taiwan-bank-code/master/data/taiwanBankCodeATM.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(info => {
            // 將資料插入到表格中
            document.getElementById('row').innerHTML = 
                "<tr>" +
                    "<td>" + info[0].code + "</td>" +
                    "<td>" + info[0].name + "</td>" +
                "</tr>";
        })
        .catch(error => {
            console.error('請求失敗:', error);
        });
});

$(document).ready(function() {
    // Update table with new row data
    // $("#row").html("<tr><td>123</td><td>ABC</td></tr>");
    $.ajax({
        url: 'https://raw.githubusercontent.com/wsmwason/taiwan-bank-code/master/data/taiwanBankCodeATM.json',
        type: "get",
        dataType:"json",
        success: function (info) {
            total_len = info.length;
            for(i=0; i<total_len; i++) {
                $("#row").html(
                    "<tr>" +
                        "<td>" + info[i].code + " </td>" +
                    "</tr>"
                )
                console.log(i);
                console.log(info[i].code);
                console.log(info[i].name);
            }
        },
        error: function (data) {
            console.log("請求失敗");
        }
    });
});

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    document.addEventListener("DOMContentLoaded", function() {
        // 使用 axios 來獲取資料
        axios.get('https://raw.githubusercontent.com/wsmwason/taiwan-bank-code/master/data/taiwanBankCodeATM.json')
            .then(response => {
                const info = response.data;
                // 將資料插入到表格中
                document.getElementById('row').innerHTML = 
                    "<tr>" +
                        "<td>" + info[0].code + "</td>" +
                        "<td>" + info[0].name + "</td>" +
                    "</tr>";
            })
            .catch(error => {
                console.error('請求失敗:', error);
            });
    });