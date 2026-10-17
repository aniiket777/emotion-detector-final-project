let RunSentimentAnalysis = () => {
    let inputElem = document.getElementById("textToAnalyze");
    let textToAnalyze = inputElem ? inputElem.value : "";
    let responseElem = document.getElementById("system_response");

    if (responseElem) {
        responseElem.innerHTML = "Analyzing emotion, please wait...";
    }

    let params = new URLSearchParams({ textToAnalyze: textToAnalyze });
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4) {
            if (this.status === 200 || this.status === 400 || this.status === 502) {
                if (responseElem) {
                    responseElem.innerHTML = xhttp.responseText;
                }
            } else if (this.status !== 0) {
                if (responseElem) {
                    responseElem.innerHTML = "Error " + this.status + ": " + (xhttp.responseText || "Unable to process request.");
                }
            } else if (responseElem) {
                responseElem.innerHTML = "Error: Unable to reach the server. Please check your connection.";
            }
        }
    };
    xhttp.open("GET", "/emotionDetector?" + params.toString(), true);
    xhttp.send();
};
