async function fetchResults() {
    const res = await fetch('/api/results');
    const data = await res.json();
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = data.map(r => `
        <div class="${r.status}">
            ${r.ip}:${r.port} (${r.service}) → ${r.status} 
        </div>
    `).join('');
}

async function scan() {
    const ip = document.getElementById('ip').value;
    if(!ip) return alert("Enter IP");
    await fetch('/api/scan', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ip})
    });
    fetchResults();
}

fetchResults();
setInterval(fetchResults, 5000);
