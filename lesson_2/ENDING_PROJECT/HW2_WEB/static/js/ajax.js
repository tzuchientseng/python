// 初始化一個空的 monthlyData 字典
let monthlyData = {
    "monthly_data": {}
};

// 暫存資料按鈕
document.getElementById('saveButton').addEventListener('click', function(event) {
    const month = document.getElementById('month').value;
    const profit = document.getElementById('profit').value;
    const sales = document.getElementById('sales').value;

    // 檢查月分是否已經存在於字典中，否則添加新資料
    if (month && profit && sales) {
        monthlyData["monthly_data"][month] = {
            "profit": parseFloat(profit),
            "sales": parseFloat(sales)
        };

        // 將當前字典結果顯示在頁面上
        document.getElementById('result').innerHTML = `
            <p>暫存資料:</p>
            <pre>${JSON.stringify(monthlyData, null, 2)}</pre>
        `;
    } else {
        alert("請填寫完整資料！");
    }
});

// 計算並送出資料按鈕
document.getElementById('calculateButton').addEventListener('click', function(event) {
    if (Object.keys(monthlyData["monthly_data"]).length === 0) {
        alert("請先暫存資料再送出！");
        return;
    }

    // 發送 AJAX 請求
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "https://api.sunnytseng.com/calculate_max_revenue", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    // 當收到回應後的處理
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            document.getElementById('result').innerHTML += `<p>Max Revenue: ${JSON.stringify(response)}</p>`;
        } else if (xhr.readyState === 4) {
            console.error('Error:', xhr.statusText);
        }
    };

    // 發送資料
    xhr.send(JSON.stringify(monthlyData));
});

// 清除資料按鈕
document.getElementById('clearButton').addEventListener('click', function() {
    monthlyData = { "monthly_data": {} }; // 清空字典
    document.getElementById('result').innerHTML = ''; // 清空顯示內容
    document.getElementById('month').value = ''; // 清空輸入欄位
    document.getElementById('profit').value = '';
    document.getElementById('sales').value = '';
});
