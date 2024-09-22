// DOM elements
const todoContainer = document.getElementById('todo-container');
const mainTitle = document.getElementById('main-title');
const mainContent = document.getElementById('main-content');
const noteButton = document.getElementById('note');
const saveButton = document.getElementById('save-tasks');
const addTaskButton = document.getElementById('add-task');
const clearInProgressButton = document.getElementById('clear-in-progress');
let noteContainer = null;
let noteEditor = null;

document.addEventListener('DOMContentLoaded', function() {
    // Focus on "Add Task" button
    addTaskButton.focus();

    // Add event listener for Enter key
    document.addEventListener('keydown', enterKeyListener);

    // Add event listener for Tab key
    document.addEventListener('keydown', tabKeyListener);

    // Add event listener for Ctrl+S
    document.addEventListener('keydown', function(event) {
        if (event.ctrlKey && event.key === 's') {
            event.preventDefault(); // Prevent the browser's save dialog
            saveTasks();
        }
    });

    // Add event listener for double click
    // document.addEventListener('dblclick', disableTabListener);

    initializePage();
});

function initializePage() {
    // Event listeners
    saveButton.addEventListener('click', saveTasks);
    addTaskButton.addEventListener('click', addTask);
    clearInProgressButton.addEventListener('click', clearInProgress);
    noteButton.addEventListener('click', toggleNote);

    fetchTasks();
    initializeSortable();
}

function showTodoView() {
    todoContainer.style.display = 'block';
    mainTitle.textContent = 'To-Do List';
    if (noteContainer) noteContainer.style.display = 'none';
    noteButton.textContent = 'Notebook';
}

function fetchTasks() {
    fetch('/tasks', {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            renderTasks(JSON.parse(data.data[0].todo), 'todo-list');
            renderTasks(JSON.parse(data.data[0].in_progress), 'in-progress-list');
            updateNoteContent(data.data[0].note);
        } else {
            showErrorMessage('Error', 'Invalid data structure received from server');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showErrorMessage('Error', 'Error fetching tasks and note content');
    });
}

function renderTasks(tasks, listId) {
    const listElement = document.getElementById(listId);
    if (!listElement) {
        console.error(`Cannot find element with ID '${listId}'`);
        return;
    }
    listElement.innerHTML = '';
    tasks.forEach(task => {
        const newTask = createTaskElement(task, listId === 'in-progress-list');
        listElement.appendChild(newTask);
    });
}

function saveTasks() {
    const todoTasks = Array.from(document.getElementById('todo-list').children).map(li => li.firstChild.textContent.trim());
    const inProgressTasks = Array.from(document.getElementById('in-progress-list').children).map(li => li.firstChild.textContent.trim());
    const noteText = noteEditor ? noteEditor.getValue() : '';

    const data = {
        todo: JSON.stringify(todoTasks),
        in_progress: JSON.stringify(inProgressTasks),
        note: noteText
    };

    fetch('/save_tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showSuccessMessage('Save Successful', 'Your tasks and notes have been successfully saved');
        } else {
            showErrorMessage('Save Failed', 'Unable to save tasks and notes: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showErrorMessage('Error', 'An error occurred while saving tasks and notes');
    });
}

function addTask() {
    Swal.fire({
        title: 'Add Task',
        input: 'text',
        inputPlaceholder: 'Enter your task...',
        showCancelButton: true,
        confirmButtonText: 'Add',
        cancelButtonText: 'Cancel',
        confirmButtonColor: '#ff9800',
        cancelButtonColor: '#aaa',
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
                const newTask = createTaskElement(taskText, false);
                todoList.prepend(newTask);
            }
        }
    });
}

function createTaskElement(taskText, isCompleted) {
    const newTask = document.createElement('li');
    newTask.className = 'list-group-item d-flex justify-content-between align-items-center';
    newTask.textContent = taskText;

    newTask.addEventListener('dblclick', () => editTask(newTask));

    const button = document.createElement('button');
    button.className = isCompleted ? 'btn btn-sm btn-outline-danger' : 'btn btn-sm btn-outline-success';
    button.textContent = isCompleted ? 'Complete' : 'In Progress';
    button.addEventListener('click', () => isCompleted ? newTask.remove() : completeTask(newTask));
    newTask.appendChild(button);

    return newTask;
}

function completeTask(task) {
    const inProgressList = document.getElementById('in-progress-list');
    inProgressList.prepend(task);
    const button = task.querySelector('button');
    button.className = 'btn btn-sm btn-outline-danger';
    button.textContent = 'Complete';
    button.onclick = () => task.remove();
}

function editTask(task) {
    const originalText = task.childNodes[0].textContent.trim();
    const input = document.createElement('input');
    input.type = 'text';
    input.className = 'form-control';
    input.value = originalText;
    task.innerHTML = '';
    task.appendChild(input);
    input.focus();

    input.addEventListener('blur', () => saveEdit(task, input.value));
    input.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            saveEdit(task, input.value);
        }
    });
}

function saveEdit(task, newValue) {
    const isCompleted = task.closest('#in-progress-list') !== null;
    task.innerHTML = '';
    task.textContent = newValue;
    const button = document.createElement('button');
    button.className = isCompleted ? 'btn btn-sm btn-outline-danger' : 'btn btn-sm btn-outline-success';
    button.textContent = isCompleted ? 'Complete' : 'In Progress';
    button.addEventListener('click', () => isCompleted ? task.remove() : completeTask(task));
    task.appendChild(button);
    task.addEventListener('dblclick', () => editTask(task));
}

function clearInProgress() {
    document.getElementById('in-progress-list').innerHTML = '';
}

function initializeSortable() {
    new Sortable(document.getElementById('todo-list'), {
        group: 'shared',
        animation: 150,
        ghostClass: 'blue-background-class',
        onEnd: function (evt) {
            // 如果是拖到 in-progress-list 中，不需要再手動執行 completeTask
            if (evt.to.id === 'in-progress-list') {
                const button = evt.item.querySelector('button');
                button.className = 'btn btn-sm btn-outline-danger';
                button.textContent = 'Complete';
                button.onclick = function () {
                    evt.item.remove();
                };
            }
        }
    });

    new Sortable(document.getElementById('in-progress-list'), {
        group: 'shared',
        animation: 150,
        ghostClass: 'blue-background-class',
        onEnd: function (evt) {
            // 如果是從 in-progress-list 移回 todo-list，恢復按鈕狀態
            if (evt.to.id === 'todo-list') {
                const button = evt.item.querySelector('button');
                button.className = 'btn btn-sm btn-outline-success';
                button.textContent = 'In Progress';
                button.onclick = function () {
                    const inProgressList = document.getElementById('in-progress-list');
                    inProgressList.prepend(evt.item);  // 將項目移到 in-progress-list
                };
            }
        }
    });
}
    
// // Not Completed item 只能移動到 In Progress最上層
// function initializeSortable() {
//     new Sortable(document.getElementById('todo-list'), {
//         group: 'shared',
//         animation: 150,
//         ghostClass: 'blue-background-class',
//         onEnd: function (evt) {
//             if (evt.to.id === 'in-progress-list') {
//                 completeTask(evt.item);
//             }
//         }
//     });

//     new Sortable(document.getElementById('in-progress-list'), {
//         group: 'shared',
//         animation: 150,
//         ghostClass: 'blue-background-class',
//         onEnd: function (evt) {
//             if (evt.to.id === 'todo-list') {
//                 const button = evt.item.querySelector('button');
//                 button.className = 'btn btn-sm btn-outline-success';
//                 button.textContent = 'In Progress';
//                 button.onclick = function () {
//                     completeTask(evt.item);
//                 };
//             }
//         }
//     });
// }

function enterKeyListener(event) {
    if (event.key === 'Enter' && (!noteEditor || !noteEditor.hasFocus())) {
        addTaskButton.click();
    }
}

function tabKeyListener(event) {
    if (event.key === 'Tab' && (!noteEditor || !noteEditor.hasFocus() && !isVimModeActive())) {
        event.preventDefault(); // Prevent default tab behavior
        toggleNote();
    }
}

function isVimModeActive() {
    return noteEditor && noteEditor.getOption('keyMap') === 'vim' && noteEditor.state.vim && noteEditor.state.vim.insertMode;
}

function disableTabListener() {
    document.removeEventListener('keydown', tabKeyListener);
    setTimeout(() => {
        document.addEventListener('keydown', tabKeyListener);
    }, 1000); // Re-enable after 1 second
}

function toggleNote() {
    if (todoContainer.style.display !== 'none') {
        // Switch to Notebook and remove the listener for the Enter key
        document.removeEventListener('keydown', enterKeyListener);
        todoContainer.style.display = 'none';
        mainTitle.textContent = 'Notebook';
        if (!noteContainer) {
            createNoteContainer();
        } else {
            noteContainer.style.display = 'block';
        }
        noteButton.textContent = 'To-Do List';
    } else {
        // Switch back to the To-Do List and re-add the listener for the Enter key
        document.addEventListener('keydown', enterKeyListener);
        showTodoView();
    }
    // Ensure tabKeyListener is always active
    document.addEventListener('keydown', tabKeyListener);
}

function createNoteContainer() {
    noteContainer = document.createElement('div');
    noteContainer.id = 'note-container';
    noteContainer.className = 'container mt-3';
    const noteCard = document.createElement('div');
    noteCard.className = 'card flex-grow-1';
    const noteHeader = document.createElement('div');
    noteHeader.className = 'card-header bg-secondary text-white';
    noteHeader.textContent = 'Notebook';
    const noteBody = document.createElement('div');
    noteBody.className = 'card-body';
    const editorContainer = document.createElement('div');
    editorContainer.id = 'editor';
    noteBody.appendChild(editorContainer);
    noteCard.appendChild(noteHeader);
    noteCard.appendChild(noteBody);
    noteContainer.appendChild(noteCard);
    mainContent.appendChild(noteContainer);

    // Initialize CodeMirror with Vim mode and custom settings
    noteEditor = CodeMirror(editorContainer, {
        lineNumbers: true,
        theme: 'monokai',
        mode: 'markdown',
        keyMap: 'vim',
        extraKeys: {
            "Ctrl-S": function(cm) { saveTasks(); },
            "Ctrl-N": function(cm) { cm.setOption('highlightSelectionMatches', false); },
            "Ctrl-C": function(cm) { // Add Ctrl-C for copying text
            const selectedText = cm.getSelection();
            if (selectedText) {
                navigator.clipboard.writeText(selectedText)
                    .then(() => console.log('文本已成功複製到剪貼簿'))
                    .catch(err => console.error('無法複製到剪貼簿:', err));
            }
            }
        }
    });

    // Custom Vim key mappings
    CodeMirror.Vim.map('jk', '<Esc>', 'insert');
    // Start in insert mode
    CodeMirror.Vim.handleKey(noteEditor, 'i');

    // CodeMirror.Vim.map('t', 'ggVG', 'normal');
    // Override yank operation
    // const originalYankFunction = CodeMirror.Vim.getRegisterController().getRegister('yank').set;
    // CodeMirror.Vim.getRegisterController().getRegister('yank').set = function(text, linewise, blockwise) {
    //     originalYankFunction.call(this, text, linewise, blockwise);
    //     navigator.clipboard.writeText(text).catch(err => console.error('Failed to copy to clipboard:', err));
    // };
    // Override paste operation
    // CodeMirror.Vim.map('*p', ':pasteFromSystem<CR>', 'normal');
    // CodeMirror.Vim.map('*P', ':pasteFromSystem<CR>', 'normal');
    // CodeMirror.Vim.defineEx('pasteFromSystem', '', (cm) => {
    //     navigator.clipboard.readText().then(text => {
    //         const cursor = cm.getCursor();
    //         cm.replaceRange(text, cursor);
    //     }).catch(err => console.error('Failed to paste from clipboard:', err));
    // });
}

function updateNoteContent(noteText) {
    if (!noteContainer) {
        createNoteContainer();
    }
    if (noteEditor) {
        noteEditor.setValue(noteText || '');
    }
    noteContainer.style.display = 'none';
}

function clearTasks() {
    document.getElementById('todo-list').innerHTML = '';
    document.getElementById('in-progress-list').innerHTML = '';
    if (noteEditor) {
        noteEditor.setValue('');
    }
}

function showSuccessMessage(title, text) {
    Swal.fire({
        icon: 'success',
        title: title,
        text: text,
        confirmButtonText: 'OK',
        confirmButtonColor: '#ff9800'
    });
}

function showErrorMessage(title, text) {
    Swal.fire({
        icon: 'error',
        title: title,
        text: text,
        confirmButtonText: 'OK',
        confirmButtonColor: '#ff9800'
    });
}
