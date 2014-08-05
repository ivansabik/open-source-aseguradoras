#!/usr/bin/php -q
<?php
define('NUM_REGISTROS', 5000000);

$plazos = array(1, 5, 10, 15, 20);
$edades = range(12, 65);
$polizas = array();
file_put_contents("polizas.csv", "num_poliza,plazo,edad,suma_asegurada" . PHP_EOL);
foreach (range(1, NUM_REGISTROS) as $poliza) {
    $num_poliza = $poliza;
    $plazo = $plazos[array_rand($plazos)];
    $edad = $edades[array_rand($edades)];
    $suma_asegurada = rand(10000, 70000);
    $poliza = "$num_poliza,$plazo,$edad,$suma_asegurada" . PHP_EOL;
    file_put_contents("polizas.csv", $poliza, FILE_APPEND);
    print $poliza;
}


