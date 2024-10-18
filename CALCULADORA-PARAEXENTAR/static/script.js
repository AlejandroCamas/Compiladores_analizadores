function appendCharacter(character) {
    document.getElementById("expression").value += character;
}

function clearDisplay() {
    document.getElementById("expression").value = "";
    document.getElementById("result").innerHTML = "";
    document.querySelector("#tokenTable tbody").innerHTML = "";
}

function calculate() {
    const expression = document.getElementById("expression").value;
    
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expression: expression })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = data.result;
        displayTokens(data.tokens);
    });
}

function showHistory() {
    const expression = document.getElementById("expression").value;

    fetch('/history', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expression: expression })
    })
    .then(response => response.json())
    .then(data => {
        displayTokens(data.tokens);
    });
}

function displayTokens(tokens) {
    const tbody = document.querySelector("#tokenTable tbody");
    tbody.innerHTML = "";
    tokens.forEach(token => {
        const row = document.createElement("tr");
        row.innerHTML = `<td>${token.value}</td><td>${token.type}</td>`;
        tbody.appendChild(row);
    });
}
