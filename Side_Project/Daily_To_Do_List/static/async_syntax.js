document.addEventListener('DOMContentLoaded', async function() {
    // Focus on "Add Task" button
    const addTaskButton = document.getElementById('add-task');
    addTaskButton.focus();

    // Add event listener for Enter key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            addTaskButton.click();
        }
    });

    // 從後端獲取現有的待辦事項和已完成事項
    try {
        const response = await fetch('http://127.0.0.1:5000/get-tasks');
        const data = await response.json();

        const todoList = document.getElementById('todo-list');
        const completedList = document.getElementById('completed-list');

        // 添加待辦事項到列表中
        data.todos.forEach(taskText => {
            const newTask = document.createElement('li');
            newTask.className = 'list-group-item d-flex justify-content-between align-items-center';
            newTask.textContent = taskText;

            const completeButton = document.createElement('button');
            completeButton.className = 'btn btn-sm btn-outline-success';
            completeButton.textContent = 'Complete';
            completeButton.addEventListener('click', function () {
                completeTask(newTask);
            });

            newTask.appendChild(completeButton);
            todoList.appendChild(newTask);
        });

        // 添加已完成事項到列表中
        data.completed.forEach(taskText => {
            const newTask = document.createElement('li');
            newTask.className = 'list-group-item d-flex justify-content-between align-items-center';
            newTask.textContent = taskText;

            const cancelButton = document.createElement('button');
            cancelButton.className = 'btn btn-sm btn-outline-danger';
            cancelButton.textContent = 'Cancel';
            cancelButton.addEventListener('click', function () {
                cancelTask(newTask);
            });

            newTask.appendChild(cancelButton);
            completedList.appendChild(newTask);
        });
    } catch (error) {
        console.error('Error fetching tasks:', error);
    }
});

document.getElementById('add-task').addEventListener('click', async function () {
    const result = await Swal.fire({
        title: 'Add a new task',
        input: 'text',
        inputPlaceholder: 'Enter your task...',
        showCancelButton: true,
        confirmButtonText: 'Add',
        cancelButtonText: 'Cancel',
        confirmButtonColor: '#ff9800',  // 橘色確認按鈕
        cancelButtonColor: '#aaa',  // 灰色取消按鈕
        inputValidator: (value) => {
            if (!value) {
                return 'Task cannot be empty!';
            }
        }
    });

    if (result.isConfirmed) {
        const taskText = result.value.trim();
        if (taskText) {
            const todoList = document.getElementById('todo-list');
            const newTask = document.createElement('li');
            newTask.className = 'list-group-item d-flex justify-content-between align-items-center';
            newTask.textContent = taskText;

            const completeButton = document.createElement('button');
            completeButton.className = 'btn btn-sm btn-outline-success';
            completeButton.textContent = 'Complete';
            completeButton.addEventListener('click', function () {
                completeTask(newTask);
            });

            newTask.appendChild(completeButton);
            todoList.prepend(newTask);
        }
    }
});

function completeTask(task) {
    const completedList = document.getElementById('completed-list');
    completedList.prepend(task);
    task.querySelector('button').remove();

    // 添加取消按鈕
    const cancelButton = document.createElement('button');
    cancelButton.className = 'btn btn-sm btn-outline-danger';
    cancelButton.textContent = 'Cancel';
    cancelButton.addEventListener('click', function () {
        cancelTask(task);
    });
    task.appendChild(cancelButton);
}

function cancelTask(task) {
    const todoList = document.getElementById('todo-list');
    task.querySelector('button').remove(); // 移除取消按鈕
    const completeButton = document.createElement('button');
    completeButton.className = 'btn btn-sm btn-outline-success';
    completeButton.textContent = 'Complete';
    completeButton.addEventListener('click', function () {
        completeTask(task);
    });
    task.appendChild(completeButton);
    todoList.prepend(task); // 將任務移回待辦事項
}

// 清空已完成事項列表
document.getElementById('clear-completed').addEventListener('click', function () {
    const completedList = document.getElementById('completed-list');
    completedList.innerHTML = ''; // 清空列表中的所有項目
});

// 清除資料庫
document.getElementById('clear-data').addEventListener('click', async function () {
    const result = await Swal.fire({
        title: 'Are you sure?',
        text: "This will delete all tasks!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Yes, delete it!'
    });

    if (result.isConfirmed) {
        try {
            const response = await fetch('http://127.0.0.1:5000/clear-tasks', {  // 更改為正確的伺服器地址和端口
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const data = await response.json();
            await Swal.fire({
                icon: 'success',
                title: 'Data cleared',
                text: 'All tasks have been deleted!'
            });
            location.reload();  // 刷新頁面
        } catch (error) {
            await Swal.fire({
                icon: 'error',
                title: 'Failed to clear data',
                text: 'Unable to clear tasks, please try again later.'
            });
        }
    }
});

// 啟用 SortableJS 並設置為同一組 group，以支援跨容器拖曳
new Sortable(document.getElementById('todo-list'), {
    group: 'shared', // 設定為同一個 group，允許這兩個列表之間進行拖曳
    animation: 150,  // 拖曳動畫時間，單位為毫秒
    ghostClass: 'blue-background-class', // 拖曳時，所拖曳項目的佔位符背景色
    onEnd: function (evt) {  // 當拖曳操作結束時觸發的事件回調
        if (evt.to.id === 'completed-list') {  // 檢查項目是否被移動到 "已完成事項" 列表中
            const task = evt.item;  // 獲取被拖曳的項目
            task.querySelector('button').remove(); // 移除該項目中的 "完成" 按鈕
            const cancelButton = document.createElement('button'); // 創建一個新的 "取消" 按鈕
            cancelButton.className = 'btn btn-sm btn-outline-danger'; // 設定 "取消" 按鈕的樣式
            cancelButton.textContent = 'Cancel';  // 設定按鈕文字為 "取消"
            cancelButton.addEventListener('click', function () {  // 為 "取消" 按鈕添加點擊事件
                cancelTask(task);  // 點擊 "取消" 按鈕時，呼叫 `cancelTask` 函數將任務移回 "待辦事項" 列表
            });
            task.appendChild(cancelButton);  // 將 "取消" 按鈕添加到被拖曳的項目中
        }
    }
});

new Sortable(document.getElementById('completed-list'), {
    group: 'shared', // 設定為同一個 group，允許這兩個列表之間進行拖曳
    animation: 150,  // 拖曳動畫時間，單位為毫秒
    ghostClass: 'blue-background-class', // 拖曳時，所拖曳項目的佔位符背景色
    onEnd: function (evt) {  // 當拖曳操作結束時觸發的事件回調
        if (evt.to.id === 'todo-list') {  // 檢查項目是否被移動到 "待辦事項" 列表中
            const task = evt.item;  // 獲取被拖曳的項目
            task.querySelector('button').remove(); // 移除該項目中的 "取消" 按鈕
            const completeButton = document.createElement('button'); // 創建一個新的 "完成" 按鈕
            completeButton.className = 'btn btn-sm btn-outline-success'; // 設定 "完成" 按鈕的樣式
            completeButton.textContent = 'Complete';  // 設定按鈕文字為 "完成"
            completeButton.addEventListener('click', function () {  // 為 "完成" 按鈕添加點擊事件
                completeTask(task);  // 點擊 "完成" 按鈕時，呼叫 `completeTask` 函數將任務移到 "已完成事項" 列表
            });
            task.appendChild(completeButton);  // 將 "完成" 按鈕添加到被拖曳的項目中
        }
    }
});

document.getElementById('save-tasks').addEventListener('click', async function () {
    // 收集待辦事項
    const todoItems = [];
    document.querySelectorAll('#todo-list li').forEach(function (li) {
        todoItems.push(li.textContent.replace('Complete', '').trim());  // 去掉按鈕文字
    });

    // 收集已完成事項
    const completedItems = [];
    document.querySelectorAll('#completed-list li').forEach(function (li) {
        completedItems.push(li.textContent.replace('Cancel', '').trim());  // 去掉按鈕文字
    });

    // 準備要發送的數據
    const data = {
        todos: todoItems,
        completed: completedItems
    };

    try {
        // 發送 POST 請求到後端
        const response = await fetch('http://127.0.0.1:5000/save-tasks', {  // 更改為正確的伺服器地址和端口
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        await Swal.fire({
            icon: 'success',
            title: 'Save successful',
            text: 'Your tasks have been saved successfully!'
        });
    } catch (error) {
        await Swal.fire({
            icon: 'error',
            title: 'Save failed',
            text: 'Unable to save your tasks, please try again later.'
        });
    }
});
/*
document.addEventListener('DOMContentLoaded', function() {
    // Focus on "Add Task" button
    const addTaskButton = document.getElementById('add-task');
    addTaskButton.focus();

    // Add event listener for Enter key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            addTaskButton.click();
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const addTaskButton = document.getElementById('add-task');
    addTaskButton.focus();

    // 從後端獲取現有的待辦事項和已完成事項
    fetch('http://127.0.0.1:5000/get-tasks')
        .then(response => response.json())
        .then(data => {
            const todoList = document.getElementById('todo-list');
            const completedList = document.getElementById('completed-list');

            // 添加待辦事項到列表中
            data.todos.forEach(taskText => {
                const newTask = document.createElement('li');
                newTask.className = 'list-group-item d-flex justify-content-between align-items-center';
                newTask.textContent = taskText;

                const completeButton = document.createElement('button');
                completeButton.className = 'btn btn-sm btn-outline-success';
                completeButton.textContent = 'Complete';
                completeButton.addEventListener('click', function () {
                    completeTask(newTask);
                });

                newTask.appendChild(completeButton);
                todoList.appendChild(newTask);
            });

            // 添加已完成事項到列表中
            data.completed.forEach(taskText => {
                const newTask = document.createElement('li');
                newTask.className = 'list-group-item d-flex justify-content-between align-items-center';
                newTask.textContent = taskText;

                const cancelButton = document.createElement('button');
                cancelButton.className = 'btn btn-sm btn-outline-danger';
                cancelButton.textContent = 'Cancel';
                cancelButton.addEventListener('click', function () {
                    cancelTask(newTask);
                });

                newTask.appendChild(cancelButton);
                completedList.appendChild(newTask);
            });
        })
        .catch(error => {
            console.error('Error fetching tasks:', error);
        });
});

// document.getElementById('add-task').addEventListener('click', function () {
//     const taskInput = document.getElementById('new-task');
//     const taskText = taskInput.value.trim();
//     if (taskText) {
//         const todoList = document.getElementById('todo-list');
//         const newTask = document.createElement('li');
//         newTask.className = 'list-group-item d-flex justify-content-between align-items-center';
//         newTask.textContent = taskText;

//         const completeButton = document.createElement('button');
//         completeButton.className = 'btn btn-sm btn-outline-success';
//         completeButton.textContent = '完成';
//         completeButton.addEventListener('click', function () {
//             completeTask(newTask);
//         });

//         newTask.appendChild(completeButton);
//         todoList.prepend(newTask);
//         taskInput.value = '';
//     }
// });
document.getElementById('add-task').addEventListener('click', function () {
    Swal.fire({
        title: 'Add a new task',
        input: 'text',
        inputPlaceholder: 'Enter your task...',
        showCancelButton: true,
        confirmButtonText: 'Add',
        cancelButtonText: 'Cancel',
        confirmButtonColor: '#ff9800',  // 橘色確認按鈕
        cancelButtonColor: '#aaa',  // 灰色取消按鈕
        inputValidator: (value) => {
            if (!value) {
                return 'Task cannot be empty!';
            }
        }
    }).then((result) => {
        if (result.isConfirmed) {
            const taskText = result.value.trim();
            if (taskText) {
                const todoList = document.getElementById('todo-list');
                const newTask = document.createElement('li');
                newTask.className = 'list-group-item d-flex justify-content-between align-items-center';
                newTask.textContent = taskText;

                const completeButton = document.createElement('button');
                completeButton.className = 'btn btn-sm btn-outline-success';
                completeButton.textContent = 'Complete';
                completeButton.addEventListener('click', function () {
                    completeTask(newTask);
                });

                newTask.appendChild(completeButton);
                todoList.prepend(newTask);
            }
        }
    });
});

function completeTask(task) {
    const completedList = document.getElementById('completed-list');
    completedList.prepend(task);
    task.querySelector('button').remove();

    // 添加取消按鈕
    const cancelButton = document.createElement('button');
    cancelButton.className = 'btn btn-sm btn-outline-danger';
    cancelButton.textContent = 'Cancel';
    cancelButton.addEventListener('click', function () {
        cancelTask(task);
    });
    task.appendChild(cancelButton);
}

function cancelTask(task) {
    const todoList = document.getElementById('todo-list');
    task.querySelector('button').remove(); // 移除取消按鈕
    const completeButton = document.createElement('button');
    completeButton.className = 'btn btn-sm btn-outline-success';
    completeButton.textContent = 'Complete';
    completeButton.addEventListener('click', function () {
        completeTask(task);
    });
    task.appendChild(completeButton);
    todoList.prepend(task); // 將任務移回待辦事項
}

// 清空已完成事項列表
document.getElementById('clear-completed').addEventListener('click', function () {
    const completedList = document.getElementById('completed-list');
    completedList.innerHTML = ''; // 清空列表中的所有項目
});

// 清除資料庫
document.getElementById('clear-data').addEventListener('click', function () {
    Swal.fire({
        title: 'Are you sure?',
        text: "This will delete all tasks!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            fetch('http://127.0.0.1:5000/clear-tasks', {  // 更改為正確的伺服器地址和端口
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(response => response.json())
            .then(data => {
                Swal.fire({
                    icon: 'success',
                    title: 'Data cleared',
                    text: 'All tasks have been deleted!'
                }).then(() => {
                    location.reload();  // 刷新頁面
                });
            }).catch(error => {
                Swal.fire({
                    icon: 'error',
                    title: 'Failed to clear data',
                    text: 'Unable to clear tasks, please try again later.'
                });
            });
        }
    });
});

// 啟用 SortableJS 並設置為同一組 group，以支援跨容器拖曳
new Sortable(document.getElementById('todo-list'), {
    group: 'shared', // 設定為同一個 group，允許這兩個列表之間進行拖曳
    animation: 150,  // 拖曳動畫時間，單位為毫秒
    ghostClass: 'blue-background-class', // 拖曳時，所拖曳項目的佔位符背景色
    onEnd: function (evt) {  // 當拖曳操作結束時觸發的事件回調
        if (evt.to.id === 'completed-list') {  // 檢查項目是否被移動到 "已完成事項" 列表中
            const task = evt.item;  // 獲取被拖曳的項目
            task.querySelector('button').remove(); // 移除該項目中的 "完成" 按鈕
            const cancelButton = document.createElement('button'); // 創建一個新的 "取消" 按鈕
            cancelButton.className = 'btn btn-sm btn-outline-danger'; // 設定 "取消" 按鈕的樣式
            cancelButton.textContent = 'Cancel';  // 設定按鈕文字為 "取消"
            cancelButton.addEventListener('click', function () {  // 為 "取消" 按鈕添加點擊事件
                cancelTask(task);  // 點擊 "取消" 按鈕時，呼叫 `cancelTask` 函數將任務移回 "待辦事項" 列表
            });
            task.appendChild(cancelButton);  // 將 "取消" 按鈕添加到被拖曳的項目中
        }
    }
});

new Sortable(document.getElementById('completed-list'), {
    group: 'shared', // 設定為同一個 group，允許這兩個列表之間進行拖曳
    animation: 150,  // 拖曳動畫時間，單位為毫秒
    ghostClass: 'blue-background-class', // 拖曳時，所拖曳項目的佔位符背景色
    onEnd: function (evt) {  // 當拖曳操作結束時觸發的事件回調
        if (evt.to.id === 'todo-list') {  // 檢查項目是否被移動到 "待辦事項" 列表中
            const task = evt.item;  // 獲取被拖曳的項目
            task.querySelector('button').remove(); // 移除該項目中的 "取消" 按鈕
            const completeButton = document.createElement('button'); // 創建一個新的 "完成" 按鈕
            completeButton.className = 'btn btn-sm btn-outline-success'; // 設定 "完成" 按鈕的樣式
            completeButton.textContent = 'Complete';  // 設定按鈕文字為 "完成"
            completeButton.addEventListener('click', function () {  // 為 "完成" 按鈕添加點擊事件
                completeTask(task);  // 點擊 "完成" 按鈕時，呼叫 `completeTask` 函數將任務移到 "已完成事項" 列表
            });
            task.appendChild(completeButton);  // 將 "完成" 按鈕添加到被拖曳的項目中
        }
    }
});

document.getElementById('save-tasks').addEventListener('click', function () {
    // 收集待辦事項
    const todoItems = [];
    document.querySelectorAll('#todo-list li').forEach(function (li) {
        todoItems.push(li.textContent.replace('Complete', '').trim());  // 去掉按鈕文字
    });

    // 收集已完成事項
    const completedItems = [];
    document.querySelectorAll('#completed-list li').forEach(function (li) {
        completedItems.push(li.textContent.replace('Cancel', '').trim());  // 去掉按鈕文字
    });

    // 準備要發送的數據
    const data = {
        todos: todoItems,
        completed: completedItems
    };

    // 發送 POST 請求到後端
    fetch('http://127.0.0.1:5000/save-tasks', {  // 更改為正確的伺服器地址和端口
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => response.json())
    .then(data => {
        Swal.fire({
            icon: 'success',
            title: 'Save successful',
            text: 'Your tasks have been saved successfully!'
        });
    }).catch(error => {
        Swal.fire({
            icon: 'error',
            title: 'Save failed',
            text: 'Unable to save your tasks, please try again later.'
        });
    });
});
*/
