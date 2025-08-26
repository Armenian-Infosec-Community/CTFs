<?php


if (!isset($_COOKIE['token'])) {
  header("Location: /login.php"); exit;
}

$db = new SQLite3('users.db');

$stmt = $db->prepare("SELECT username FROM users WHERE token = :t");
$stmt->bindValue(":t", $_COOKIE['token'], SQLITE3_TEXT);
$result = $stmt->execute();
$row = $result->fetchArray(SQLITE3_ASSOC);

$username = $row['username'] ?? 'unknown';


?>
<?php include __DIR__.'/partials/head.php'; ?>
<div class="container">
  <div class="card">
    <h2>Welcome back!</h2>
    <img id="pfp" class="avatar" src="blank_pfp.png"  style="cursor:pointer">
    <p id="welcome">Loading...</p>
  </div>
</div>
<input type="file" style="display:none" id="upload">


<script>
fetch('/backend/user_information.php?username=<?php echo $username;?>')
  .then(res => res.json())
  .then(json => {
    document.getElementById('welcome').innerText = 'Welcome back, ' + json.username;
    if(json.pfp) {
      document.getElementById('pfp').src = 'data:image/png;base64,' + json.pfp;
    }
    if (json.alt) {
          document.getElementById('pfp').alt = json.alt;
    }
  })
  .catch(err => console.error(err));



<?php 

if ($username==='admin'){

echo <<<EOD
// --- Upload logic ---
const pfp = document.getElementById('pfp');
const fileInput = document.getElementById('upload');

// Clicking avatar opens file chooser
pfp.addEventListener('click', () => fileInput.click());

// When file is selected, read as base64 and send POST
fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = () => {
    // reader.result looks like "data:image/png;base64,...."
    const base64data = reader.result.split(',')[1]; 

    const params = new URLSearchParams();
    params.append("name", file.name);
    params.append("binary", base64data);

    fetch('/backend/upload.php', {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: params.toString()
    })
    .then(r => r.text())
    .then(txt => {
      console.log("Upload response:", txt);
      alert("Upload sent! Check server response.");
    })
    .catch(err => console.error("Upload error:", err));
  };
  reader.readAsDataURL(file);
});

EOD;

}
else {

echo "pfp.addEventListener('click', () => {alert('PFP Upload isn\'t developed for all users yet :(') });";
}
?>

</script>
<?php include __DIR__.'/partials/foot.php'; ?>
