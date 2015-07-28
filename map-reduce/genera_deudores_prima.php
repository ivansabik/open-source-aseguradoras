<?php
define("NUM_REGISTROS", 1000000);

$deudores = array();
foreach (range(1, NUM_REGISTROS) as $deudor) {
    $nivel1 = 140;
    $nivel2 = rand(1, 4);
    $nivel3 = 0;
    $nivel4 = 0;
    $monedas = array(10, 20, 30);
    $moneda = $monedas[array_rand($monedas)];
    $consecutivo = rand(1,15000000);
    $afectacion = 3;
    $referenciaRegimen = "";
    $operaciones = array(1000, 2000, 3000, 4000, 5000, 6000);
    $operacion = $operaciones[array_rand($operaciones)];
    $ramos = array("010","031","034","037","040","051","053");
    $cveRamo = $ramos[array_rand($ramos)];
    $recargos = rand(0, 200);
    $derechosPoliza = rand(0, 500);
    $comiPorDev = rand(0, 200);
    $recargosDev = rand(0, 200);
    $derechosPolizaDev = rand(0, 100);
    $primasPorCobrar = rand(500, 30000);
    $primasPorCobrarTotal = $recargos + $impuestos + $derechosPoliza + $comiPorDev + $recargosDev + $derechosPolizaDev + $primasPorCobrar;
    $impuestos = $primasPorCobrarTotal * 0.16;
    $deudor = "$nivel1|$nivel2|$nivel3|$nivel4|$moneda|$consecutivo|$afectacion|$referenciaRegimen|$operacion|$cveRamo|$primasPorCobrarTotal|$recargos|$impuestos|$derechosPoliza|$comiPorDev|$recargosDev|$derechosPolizaDev|$primasPorCobrar|;".PHP_EOL;
    file_put_contents("deudores.txt", $deudor, FILE_APPEND);
    print $deudor;
}
