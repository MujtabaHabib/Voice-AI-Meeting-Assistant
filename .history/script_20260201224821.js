<script>
async function send() {
    const fileInput = document.getElementById("audioFile")
    const file = fileInput.files[0]

    if (!file){
        alert("Please select an audio file first.")
        return
    }
    document.getElementById("fileName").innerText = "Selected: " + file.Name

    const form = new FormData()
        form.append("file",file)

        document.getElementById("transcript").innerText = "processing..."
        document.getElementById("summary").innerText = "AI is thinking.."

    const res = await fetch("http://127.0.0.1:8000/voice-agent",{
        method : "POST",
        body : form
    })

    const data = await res.json()

    document.getElementById("transcript").innerText = data.transcript
    document.getElementById("summary").innerText = data.summary
}
</script>