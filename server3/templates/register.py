<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form action="/register" method="post">
        <input type="text" name="username" placeholder="username">
        <br>
        <input type="text" name="password" placeholder="password">
        <br>
        <button type="submit">Register </button>
    </form>
    <h3>{{result}}</h3>
</body>
</html>
