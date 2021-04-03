<?php
    $command = escapeshellcmd('python3 scraper.py');
    $output = shell_exec($command);
    echo "The Top 5 names are<br>";
    echo $output;
   
?>