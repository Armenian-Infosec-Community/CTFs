<?php

$db = new SQLite3('users.db');

$username = $_POST['username'];
$password = $_POST['password'];

$stmt = $db->prepare("SELECT * FROM users WHERE username = :u AND password = :p");
$stmt->bindValue(":u", $username, SQLITE3_TEXT);
$stmt->bindValue(":p", $password, SQLITE3_TEXT);
$result = $stmt->execute();



if ($row = $result->fetchArray(SQLITE3_ASSOC)) {
if ($username=='admin') {
die('Logins for admin are locked');
}
setcookie('token', $row['token'], time() + 3600*24, "/");
header('Location: /home.php');
}
else {
die('Invalid login creds applied :\ ');
}

?>
