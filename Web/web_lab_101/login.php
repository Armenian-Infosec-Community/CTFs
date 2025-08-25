<?php $TITLE="Login"; include __DIR__."/partials/head.php"; ?>
<h2> BTW here admin creds, anyways you can't login </h2><code class="code">admin / root4512</code>
<br><br>
<div class="card">
  <div class="form">
    <div class="title">Sign in</div>
    <div class="sub">Try <code class="code">user1 / pass1</code> better</div>
    <form method="POST" action="/login_action.php">
      <input class="input" name="username" placeholder="Username or email" autocomplete="username" />
      <input class="input" name="password" type="password" placeholder="Password" autocomplete="current-password" />
      <div class="row">
        <button class="btn" type="submit">Sign in</button>
      </div>
    </form>
    <div class="hint"><strong>Hint:</strong> Enough hints for this challenge.</div>
  </div>
</div>
<?php include __DIR__."/partials/foot.php"; ?>
