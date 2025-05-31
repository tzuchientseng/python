let monthlyData = {
    "monthly_data": {}
};

// 暫存資料按鈕
document.getElementById('saveButton').addEventListener('click', function(event) {
    const month = document.getElementById('month').value;
    const profit = document.getElementById('profit').value;
    const sales = document.getElementById('sales').value;

    if (month && profit && sales) {
        // 將資料存入 monthlyData
        monthlyData["monthly_data"][month] = {
            "profit": parseFloat(profit),
            "sales": parseFloat(sales)
        };

        // 更新表格顯示
        updateTable();

        // 清空輸入欄位
        document.getElementById('month').value = '';
        document.getElementById('profit').value = '';
        document.getElementById('sales').value = '';

        // 啟用計算按鈕
        document.getElementById('calculateButton1').disabled = false;
        document.getElementById('calculateButton2').disabled = false;
        document.getElementById('calculateButton3').disabled = false;
        document.getElementById('calculateButton4').disabled = false;
        document.getElementById('calculateButton5').disabled = false;
    } else {
        alert("請填寫完整資料！");
    }
});

// 更新表格函數
function updateTable() {
    const tableBody = document.querySelector('#dataTable tbody');
    tableBody.innerHTML = ''; // 清空表格

    // 從 monthlyData 動態生成表格內容
    Object.keys(monthlyData["monthly_data"]).forEach(month => {
        const profit = monthlyData["monthly_data"][month].profit;
        const sales = monthlyData["monthly_data"][month].sales;
        const revenue = profit * sales; // 計算營業額

        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${month}</td>
            <td>${profit}</td>
            <td>${sales}</td>
            <td>${revenue}</td> <!-- 營業額欄位 -->
        `;
        tableBody.appendChild(row);
    });
}

// 發送商品定價建議的API
document.getElementById('calculateButton1').addEventListener('click', function(event) {
    const postData = {
        "monthly_data": monthlyData["monthly_data"]
    };

    fetch('https://api.sunnytseng.com/calculate_max_revenue', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData)
    })
    .then(response => response.json())
    .then(data => {
        // 將結果顯示在前端
        document.getElementById('resultContainer').innerHTML = `
            <h3>商品定價建議</h3>
            <p><strong>最佳利潤:</strong> ${data.max_profit}</p>
            <p><strong>最佳營業額:</strong> ${data.max_revenue}</p>
            <p><strong>建議:</strong> ${data.suggestion}</p>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('resultContainer').innerHTML = `<p>資料解析失敗</p>`;
    });
});

// 發送銷售量95%信賴區間的API
document.getElementById('calculateButton2').addEventListener('click', function(event) {
    const salesData = Object.values(monthlyData["monthly_data"]).map(entry => entry.sales);
    const postData = {
        "data": salesData,
        "CI": 95
    };

    fetch('https://api.sunnytseng.com/CI', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData)
    })
    .then(response => response.json())
    .then(data => {
        // 將結果顯示在前端
        document.getElementById('resultContainer').innerHTML = `
            <h3>商品銷售量平均 95% 信賴區間結果</h3>
            <p><strong>下限:</strong> ${data.lower_bound}</p>
            <p><strong>上限:</strong> ${data.upper_bound}</p>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('resultContainer').innerHTML = `<p>資料解析失敗</p>`;
    });
});

// 發送銷售量98%信賴區間的API
document.getElementById('calculateButton3').addEventListener('click', function(event) {
    const salesData = Object.values(monthlyData["monthly_data"]).map(entry => entry.sales);
    const postData = {
        "data": salesData,
        "CI": 98
    };

    fetch('https://api.sunnytseng.com/CI', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData)
    })
    .then(response => response.json())
    .then(data => {
        // 將結果顯示在前端
        document.getElementById('resultContainer').innerHTML = `
            <h3>商品銷售量平均 98% 信賴區間結果</h3>
            <p><strong>下限:</strong> ${data.lower_bound}</p>
            <p><strong>上限:</strong> ${data.upper_bound}</p>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('resultContainer').innerHTML = `<p>資料解析失敗</p>`;
    });
});

// 發送銷售量變異數95%信賴區間的API
document.getElementById('calculateButton4').addEventListener('click', function(event) {
    const salesData = Object.values(monthlyData["monthly_data"]).map(entry => entry.sales);
    const postData = {
        "data": salesData,
        "CI": 95
    };

    fetch('https://api.sunnytseng.com/VarCI', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData)
    })
    .then(response => response.json())
    .then(data => {
        // 將結果顯示在前端
        document.getElementById('resultContainer').innerHTML = `
            <h3>商品銷售量變異數 95% 信賴區間結果</h3>
            <p><strong>下限:</strong> ${data.lower_bound}</p>
            <p><strong>上限:</strong> ${data.upper_bound}</p>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('resultContainer').innerHTML = `<p>資料解析失敗</p>`;
    });
});

// 發送營業額描述性統計的API
document.getElementById('calculateButton5').addEventListener('click', function(event) {
    const revenueData = Object.values(monthlyData["monthly_data"]).map(entry => entry.profit * entry.sales);
    const postData = {
        "data": revenueData // 符合 API 的格式
    };

    fetch('https://api.sunnytseng.com/Descriptive', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        document.getElementById('resultContainer').innerHTML = `
            <h3>營業額</h3>
            <p><strong>平均數:</strong> ${data.mean}</p>
            <p><strong>變異數:</strong> ${data.variance}</p>
            <p><strong>標準差:</strong> ${data.standard_deviation}</p>
            <p><strong>樣本變異數:</strong> ${data.sample_variance}</p>
            <p><strong>樣本標準差:</strong> ${data.sample_standard_deviation}</p>
            <p><strong>中位數:</strong> ${data.median}</p>
            <p><strong>眾數:</strong> ${data.mode}</p>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
        console.log(JSON.stringify(postData))
        document.getElementById('resultContainer').innerHTML = `<p>資料解析失敗</p>`;
    });

});

// 清除資料按鈕
document.getElementById('clearButton').addEventListener('click', function() {
    // 清空 monthlyData
    monthlyData = { "monthly_data": {} };

    // 清空表格內容
    document.querySelector('#dataTable tbody').innerHTML = '';

    // 清空結果顯示
    document.getElementById('maxRevenue').innerHTML = '';

    // 清空輸入欄位
    document.getElementById('month').value = '';
    document.getElementById('profit').value = '';
    document.getElementById('sales').value = '';

    // 禁用計算按鈕
    document.getElementById('calculateButton1').disabled = true;
    document.getElementById('calculateButton2').disabled = true;
    document.getElementById('calculateButton3').disabled = true;
    document.getElementById('calculateButton4').disabled = true;
    document.getElementById('calculateButton5').disabled = true;

    alert("資料已經清除！");
});
