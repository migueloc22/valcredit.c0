import { useEffect, useState } from "react";
import { post } from "../../../store";
export default function useSimulador() {
  const [rows, setRows] = useState([]);
  const onSubmit = async (data) => {
    console.log("Datos enviados al simulador:", data);
    try {
      const parameters = {
        valor_solicitado: Number(data.valorSolicitado),
        numero_cuota: Number(data.numeroCuotas),
      };
      const response = await post("/v1/calcular_pagos", parameters);
      const pagos = Array.isArray(response)
        ? response
        : response?.PlanPagos ?? [];
      const mapped = pagos.map((p, i) => ({
        id: p.numero_cuota ?? i + 1,
        numero_cuota: p.numero_cuota ?? i + 1,
        valor_solicitado: Number(p.valor_solicitado ?? 0),
        saldo_pendiente: Number(p.saldo_pendiente ?? 0),
      }));
      console.log("Respuesta del simulador:", mapped);
      setRows(mapped);
    } catch (err) {
      console.error("Error en simulador:", err);
      setRows([]);
    }
  };

  const columns = [
    { field: "numero_cuota", headerName: "Cuota", width: 110 },
    {
      field: "valor_solicitado",
      headerName: "Valor solicitado",
      flex: 1,
    },
    {
      field: "saldo_pendiente",
      headerName: "Saldo pendiente",
      flex: 1,
    },
  ];
  useEffect(() => {
    return () => {
      setRows([]);
    };
  }, []);
  return {
    onSubmit,
    rows,
    columns,
  };
}
