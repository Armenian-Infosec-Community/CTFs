<?php

header('Content-Type: application/json');

if (!isset($_COOKIE['token'])) {
  die('Not logged in :\ ');
}

$db = new SQLite3('../users.db');

$stmt = $db->prepare("SELECT username,token,pfp,alt FROM users WHERE username = :u");
$stmt->bindValue(":u", $_GET['username'], SQLITE3_TEXT);
$result = $stmt->execute();
$row = $result->fetchArray(SQLITE3_ASSOC);

$username = $row['username'] ?? 'unknown';
$pfp = $row['pfp'] ?? '';
$token = $row['token'] ?? '';
$alt = $row['alt'] ?? '';

// Define response object
$obj = new stdClass();
$obj->username = $username;
$obj->pfp = $pfp;
$obj->token = base64_encode($token);
$obj->alt = $alt;

echo json_encode($obj);


?>
