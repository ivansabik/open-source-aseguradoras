-- rr8deud_tabla_e7.pig
-- Transforma la info del RR7DEUD, en la de la Tabla E7 del Reporte de Solvencia

deudores = LOAD 'RR8DEUD.txt' using PigStorage('|')
AS (nivel_1:int, nivel_2:int, nivel_3:int, nivel_4:int, moneda:int,
consecutivo:int, afectacion:int, referencia_regimen:chararray, operacion:int, cve_ramo:int,
primas_por_cobrar_total:float, recargos:float, impuestos:float, derechos_poliza:float, comi_x_dev:float,
recargos_dev:float, derechos_poliza_dev:float, primas_por_cobrar:float);

-- Agrupa por operación, moneda
grupos_deudores_operacion = GROUP deudores BY (operacion, moneda);
montos_totales_operacion = FOREACH grupos_deudores_operacion GENERATE group, SUM(deudores.primas_por_cobrar_total);
DUMP montos_totales_operacion;
