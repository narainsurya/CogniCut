async function run() {
  document.getElementById("status").innerText = "Processing...";
  document.getElementById("output").innerText = "";

  const res = await fetch("http://localhost:5678/webhook/video", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      video_path: document.getElementById("video").value
    })
  });

  const data = await res.json();
  document.getElementById("status").innerText = "Done ✅";
  document.getElementById("output").innerText =
    JSON.stringify(data, null, 2);
}
