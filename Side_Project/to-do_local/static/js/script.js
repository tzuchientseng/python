// DOM elements
const todoContainer = document.getElementById('todo-container');
const mainTitle = document.getElementById('main-title');
const mainContent = document.getElementById('main-content');
const noteButton = document.getElementById('note');
const saveButton = document.getElementById('save-tasks');
const addTaskButton = document.getElementById('add-task');
const clearInProgressButton = document.getElementById('clear-in-progress');
let noteContainer = null;
let noteTextarea = null;

document.addEventListener('DOMContentLoaded', function() {
    // Focus on "Add Task" button
    addTaskButton.focus();

    // Add event listener for Enter key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            addTaskButton.click();
        }
    });

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
    const noteText = noteContainer ? noteContainer.querySelector('textarea').value : '';

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
            if (evt.to.id === 'in-progress-list') {
                completeTask(evt.item);
            }
        }
    });

    new Sortable(document.getElementById('in-progress-list'), {
        group: 'shared',
        animation: 150,
        ghostClass: 'blue-background-class',
        onEnd: function (evt) {
            if (evt.to.id === 'todo-list') {
                const button = evt.item.querySelector('button');
                button.className = 'btn btn-sm btn-outline-success';
                button.textContent = 'In Progress';
                button.onclick = () => completeTask(evt.item);
            }
        }
    });
}

function toggleNote() {
    if (todoContainer.style.display !== 'none') {
        todoContainer.style.display = 'none';
        mainTitle.textContent = 'Notebook';
        if (!noteContainer) {
            createNoteContainer();
        } else {
            noteContainer.style.display = 'block';
        }
        noteButton.textContent = 'To-Do List';
    } else {
        showTodoView();
    }
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
    noteTextarea = document.createElement('textarea');
    noteTextarea.className = 'form-control';
    noteTextarea.rows = 10;
    noteBody.appendChild(noteTextarea);
    noteCard.appendChild(noteHeader);
    noteCard.appendChild(noteBody);
    noteContainer.appendChild(noteCard);
    mainContent.appendChild(noteContainer);
}

function updateNoteContent(noteText) {
    if (!noteContainer) {
        createNoteContainer();
    }
    if (noteTextarea) {
        noteTextarea.value = noteText || '';
    }
    noteContainer.style.display = 'none';
}

function clearTasks() {
    document.getElementById('todo-list').innerHTML = '';
    document.getElementById('in-progress-list').innerHTML = '';
    if (noteContainer) {
        noteContainer.querySelector('textarea').value = '';
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