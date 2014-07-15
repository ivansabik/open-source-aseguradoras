#!/usr/bin/php -q
<?php
$plazos = array(1, 5, 10, 15, 20);
$edades = range(12, 65);
$polizas = array();
file_put_contents('polizas.csv', 'num_poliza,plazo,edad,suma_asegurada');
foreach (range(1,50) as $poliza) {
    $num_poliza = $poliza;
    $plazo = array_rand($plazos);
    $edad = array_rand($edades);
    $suma_asegurada = rand(10000, 70000);
    $poliza = "$num_poliza,$plazo,$edad,$suma_asegurada" . PHP_EOL;
    file_put_contents('polizas.csv', $poliza, FILE_APPEND);
    print $poliza;
}


