function sendCode() {
    const code = document.getElementById('code').value;
    fetch('/tokenize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
        const output = document.getElementById('result');
        if (data.tokens) {
            let table = `
                <h3>Lexical Tokens</h3>
                <table border="1" cellpadding="8" cellspacing="0">
                    <tr style="background-color: #f2f2f2;">
                        <th>Token Type</th>
                        <th>Lexeme</th>
                    </tr>
            `;
            data.tokens.forEach(token => {
                table += `<tr><td>${token[0]}</td><td>${token[1]}</td></tr>`;
            });
            table += "</table>";
            output.innerHTML = table;
        } else {
            output.innerHTML = `<span style="color: red;">Error: ${data.error}</span>`;
        }
    });
}
function resetFields() {
    document.getElementById('code').value = "";
    document.getElementById('result').innerHTML = "";
}



document.addEventListener("DOMContentLoaded", function() {
    const accordions = document.getElementsByClassName("accordion");

    for (let i = 0; i < accordions.length; i++) {
        accordions[i].addEventListener("click", function () {
            this.classList.toggle("active");
            const panel = this.nextElementSibling;

            // Toggle panel display
            if (panel.style.display === "block") {
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }

            // Toggle icon
            const icon = this.querySelector(".icon");
            if (icon) {
                icon.textContent = this.classList.contains("active") ? "▲" : "▼";
            }
        });
    }
});