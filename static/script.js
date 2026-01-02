function analyzeSentiment() {
    const text = document.getElementById("textInput").value;

    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("positive").innerText = data.positive;
        document.getElementById("neutral").innerText = data.neutral;
        document.getElementById("negative").innerText = data.negative;
        document.getElementById("rating").innerText = data.rating;
        document.getElementById("result").classList.remove("hidden");
    });
}
