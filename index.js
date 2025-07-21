function submit() {
    const submit = document.querySelector("#submit");
    submit.addEventListener("click", async () => {
        const formInfo = document.querySelector("#token_collector");
        const formData = new FormData(formInfo);

        const response = await fetch("127.0.0.1:8000/post", {
            method: "POST",
            body: formData.getAll("API_access_token"),
        });
    });
}

function submit2() {
    const submit = document.querySelector("#submit2");
    submit.addEventListener("click", async () => {
        const formInfo = document.querySelector("#token_finder");
        const formData = new FormData(formInfo);
        var data = {};
        for (const [key, value] of formData) {
            data[key] = value;
        }
        var json = JSON.stringify(data);
        const response = await fetch("127.0.0.1:8000/post", {
            method: "POST",
            body: json,
        });
    });
}

