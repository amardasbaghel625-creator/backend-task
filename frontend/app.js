const baseURL = "http://127.0.0.1:5000/accounts/1/tasks/10/comments";

function loadComments() {
    fetch(baseURL)
        .then(r => r.json())
        .then(data => {
            const list = document.getElementById("list");
            list.innerHTML = "";
            data.forEach(c => {
                const li = document.createElement("li");
                li.innerHTML = `${c.text}
                    <button onclick="editComment(${c.id})">Edit</button>
                    <button onclick="deleteComment(${c.id})">Delete</button>`;
                list.appendChild(li);
            });
        });
}

function addComment() {
    const text = document.getElementById("text").value;
    fetch(baseURL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    }).then(loadComments);
}

function editComment(id) {
    const text = prompt("New text:");
    fetch(`${baseURL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    }).then(loadComments);
}

function deleteComment(id) {
    fetch(`${baseURL}/${id}`, { method: "DELETE" })
        .then(loadComments);
}

loadComments();
