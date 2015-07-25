<?php
define("NUM_REGISTROS", 1000);

$deudores = array();
file_put_contents("RR8DEUD.txt", "nivel_1|nivel_2|nivel_3|nivel_4|moneda|consecutivo|afectación|referencia_regimen|operacion|cve_ramo|primas_por_cobrar_total|recargos|impuestos|derechos_poliza|comi_x_dev|recargos_dev|derechos_poliza_dev|primas_por_cobrar|;" . PHP_EOL);
foreach (range(1, NUM_REGISTROS) as $deudor) {
    $nivel_1 = 140;
    $nivel_2 = rand(1, 4);
    $nivel_3 = 0;
    $nivel_4 = 0;
    $monedas = array(10, 20, 30);
    $moneda = $monedas[array_rand($monedas)];
    $consecutivo = rand(1,15000000);
    $afectacion = 3;
    $referencia_regimen = "";
    $operaciones = array(1000, 2000, 3000, 4000, 5000, 6000); #operacion, clave ramo
    $operacion = $operaciones[array_rand($operaciones)];
    $cve_ramo = 10; # tomar de operación
    $recargos = rand(0, 200);
    $derechos_poliza = rand(0, 500);
    $comi_x_dev = rand(0, 200);
    $recargos_dev = rand(0, 200);
    $derechos_poliza_dev = rand(0, 100);
    $primas_por_cobrar = rand(500, 30000);
    $primas_por_cobrar_total = $recargos + $impuestos + $derechos_poliza + $comi_x_dev + $recargos_dev + $derechos_poliza_dev + $primas_por_cobrar;
    $impuestos = $primas_por_cobrar_total * 0.16;
    $deudor = "$nivel_1|$nivel_2|$nivel_3|$nivel_4|$moneda|$consecutivo|$afectacion|$referencia_regimen|$operacion|$cve_ramo|$primas_por_cobrar_total|$recargos|$impuestos|$derechos_poliza|$comi_x_dev|$recargos_dev|$derechos_poliza_dev|$primas_por_cobrar|;" . PHP_EOL;
    file_put_contents("RR8DEUD.txt", $deudor, FILE_APPEND);
    print $deudor;
}
