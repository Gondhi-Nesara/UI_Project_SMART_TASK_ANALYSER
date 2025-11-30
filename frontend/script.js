const resultsBox = document.getElementById("results");

async function analyzeTasks() {
  const input = document.getElementById("taskInput").value;
  let tasks;

  try {
    tasks = JSON.parse(input);
  } catch {
    alert("❌ Invalid JSON!");
    return;
  }

  resultsBox.innerHTML = "⏳ Analyzing...";

  try {
    const res = await fetch("/api/tasks/analyze/", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(tasks),
    });

    const data = await res.json();
    if (!res.ok) {
      alert("Backend Error");
      resultsBox.innerHTML = "";
      return;
    }
    displayResults(data);
  } catch {
    alert("Server not running!");
    resultsBox.innerHTML = "";
  }
}

async function getSuggestions() {
  resultsBox.innerHTML = "⏳ Loading suggestions...";

  try {
    const res = await fetch("/api/tasks/suggest/");
    const data = await res.json();
    if (!res.ok) {
      alert("Failed to get suggestions");
      resultsBox.innerHTML = "";
      return;
    }
    displayResults(data.top || []);
  } catch {
    alert("Server not running!");
    resultsBox.innerHTML = "";
  }
}

function displayResults(tasks) {
  resultsBox.innerHTML = "";
  tasks.forEach(t => {
    resultsBox.innerHTML += `
      <div class="task-card">
        <h3>${t.title}</h3>
        <p>📅 Due: ${t.due_date}</p>
        <p>⭐ Importance: ${t.importance}</p>
        <p>⏱ Effort: ${t.estimated_hours} hrs</p>
        <p>🧮 Score: <b>${t.score}</b></p>
        
      </div>
    `;
  });
}
