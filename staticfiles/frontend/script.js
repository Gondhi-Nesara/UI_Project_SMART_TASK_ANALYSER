async function analyzeTasks() {
  const input = document.getElementById("taskInput").value;
  let tasks;
  try {
    tasks = JSON.parse(input);
  } catch {
    alert("❌ Invalid JSON, fix it first!");
    return;
  }

  try {
    const response = await fetch("/api/tasks/analyze/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(tasks)
    });

    const data = await response.json();
    if (!response.ok) {
      alert("❌ Error from backend: " + (data.error || "Unknown error"));
    } else {
      displayResults(data);
    }
  } catch (err) {
    alert("❌ Could not connect to server!");
    console.error(err);
  }
}

async function getSuggestions() {
  try {
    const response = await fetch("/api/tasks/suggest/");
    const data = await response.json();
    if (!response.ok) {
      alert("❌ Failed to get suggestions!");
    } else {
      displayResults(data.top);
      console.log("🔍 Suggestions:", data.suggestions);
    }
  } catch (err) {
    alert("❌ Could not connect to server!");
    console.error(err);
  }
}

function displayResults(tasks) {
  const output = document.getElementById("results");
  output.innerHTML = "";
  tasks.forEach(task => {
    output.innerHTML += `
      <div class="task-card">
        <h3>${task.title}</h3>
        <p>${task.explanation}</p>
      </div>
    `;
  });
}

