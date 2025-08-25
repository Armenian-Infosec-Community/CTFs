<?php
$TITLE = $TITLE ?? "App";
?><!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title><?=htmlspecialchars($TITLE)?></title>
  <link rel="stylesheet" href="/static/style.css" />
</head>
<body>
<header class="header">
  <nav class="nav container">
    <a href="/">Home</a>
    <a href="/login.php">Login</a>
    <span class="badge">CTF</span>
  </nav>
</header>
<main class="container">
