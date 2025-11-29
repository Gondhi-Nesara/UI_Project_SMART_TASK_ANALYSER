async function analyzeTasks() {
    const taskInput = document.getElementById("taskInput").value;
    let tasks;

    try {
        tasks = JSON.parse(taskInput);
    } catch {
        alert("Invalid JSON, please check format!");
        return;
    }

    const response = await fetch("http://127.0.0.1:8000/api/tasks/analyze/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(tasks),
    });

    const sortedTasks = await response.json();
    displayResults(sortedTasks);
}

async function getSuggestions() {
    const response = await fetch("http://127.0.0.1:8000/api/tasks/suggest/");
    const topTasks = await response.json();
    displayResults(topTasks);
}

function displayResults(tasks) {
    const results = document.getElementById("results");
    results.innerHTML = "";

    tasks.forEach((task) => {
        results.innerHTML += `
            <div class="task-card" style="border-left-color: black;">
                <h3>${task.title}</h3>
                <p>Due Date: ${task.due_date}</p>
                <p>Importance: ${task.importance}</p>
                <p>Effort (hrs): ${task.estimated_hours}</p>
            </div>
        `;
    });
}
