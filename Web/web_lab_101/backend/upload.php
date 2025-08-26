<?php
$db = new SQLite3(__DIR__ . '/../users.db');

// Require login (token from cookie)
if (!isset($_COOKIE['token'])) {
    http_response_code(403);
    die("Not logged in");
}

$stmt = $db->prepare("SELECT id, username FROM users WHERE token = :t");
$stmt->bindValue(":t", $_COOKIE['token'], SQLITE3_TEXT);
$res = $stmt->execute();
$user = $res->fetchArray(SQLITE3_ASSOC);

if (!$user) {
    http_response_code(403);
    die("Invalid session");
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $filename = $_POST['name'] ?? null;   // 🔥 vulnerable
    $binary   = $_POST['binary'] ?? null; // safe part

    if (!$filename || !$binary) {
        http_response_code(400);
        die("Missing parameters");
    }

    // update picture 
    $stmt = $db->prepare("
    UPDATE users 
    SET 
        pfp = :b64, 
        alt = '$filename'
    WHERE id = :id
    ");
    $stmt->bindValue(":b64", $binary, SQLITE3_TEXT);
    $stmt->bindValue(":id", $user['id'], SQLITE3_INTEGER);

    $stmt->execute();


    echo "✅ Upload saved for user: " . htmlspecialchars($user['username']) . "<br>";

} else {
    echo "Only POST allowed";
}
