deudores = LOAD 'deudores.txt' using PigStorage('|')
AS (nivel_1:int, nivel_2:int, nivel_3:int, nivel_4:int, moneda:int,
consecutivo:int, afectacion:int, referencia_regimen:chararray, operacion:int, cve_ramo:chararray,
primas_por_cobrar_total:float, recargos:float, impuestos:float, derechos_poliza:float, comi_x_dev:float,
recargos_dev:float, derechos_poliza_dev:float, primas_por_cobrar:float);

deudores = FILTER deudores BY nivel_1 == 140 AND
(nivel_2 == 1 OR nivel_2 == 2 OR nivel_2 == 4);

grupos_deudores = GROUP deudores BY (cve_ramo, moneda);
totales_ramo_moneda = FOREACH grupos_deudores GENERATE group, SUM(deudores.primas_por_cobrar_total);
DUMP totales_ramo_moneda;
