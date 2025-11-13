import { useEffect, useState } from "react";
import { post } from "../../../store";
import Swal from "sweetalert2";

export default function useSimulador() {
  const [rows, setRows] = useState([]);
  const [openModal, setOpenModal] = useState(false);
  const [selectedRow, setSelectedRow] = useState(null);
  const [valor_solicitado, setvalor_solicitado] = useState(0);
  const [numero_cuotas, setnumero_cuotas] = useState(0);

  const onSubmit = async (data) => {
    console.log("Datos enviados al simulador:", data);
    try {
      const parameters = {
        valor_solicitado: Number(data.valorSolicitado),
        numero_cuota: Number(data.numeroCuotas),
      };
      setvalor_solicitado(parameters.valor_solicitado);
      setnumero_cuotas(parameters.numero_cuota);
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
  const onSubmitRegistroUser = async (data) => {
    console.log("Datos enviados registro usuario:", data);
    let parameters = {
      nombres: data.nombres || "",
      apellidos: data.apellidos || "",
      // username: "username123",
      email: data.correo || "",
      celular: data.celular || "",
      numero_documento: data.numeroDocumento || "",
      genero: data.genero || "",
      fk_id_tipo_documento: data.tipoDocumento || "",
    };
    try {
      const data_user = await post("/v1/usuarios/", parameters);
      const usuario_id = data_user?.id;
      if (!usuario_id) {
        throw new Error("ID de usuario no encontrado después del registro");
      }
      let parameters_solicitud = {
        valor_solicitado: valor_solicitado,
        numero_cuotas: numero_cuotas,
        fk_id_usuario: usuario_id,
      };

      const data_solicitud = await post(
        "/v1/solicitudes/",
        parameters_solicitud
      );

      console.log("Usuario registrado:", data_user);
      console.log("Solicitud creada:", data_solicitud);
      Swal.fire({
        position: "bottom-end",
        icon: "success",
        title: "Gracias por registrar tu solicitud. Te contactaremos pronto",
        showConfirmButton: false,
        timer: 1500,
      });
      handleCloseModal();
    } catch (err) {
      console.error("Error al registrar usuario:", err);
    }
  };

  const handleOpenModal = (row) => {
    setSelectedRow(row);
    setOpenModal(true);
  };

  const handleCloseModal = () => {
    setOpenModal(false);
    setSelectedRow(null);
  };

  const columns = [
    { field: "numero_cuota", headerName: "Cuota", width: 110 },
    {
      field: "valor_solicitado",
      headerName: "Valor solicitado",
      flex: 1,
      //   valueFormatter: (params) =>
      //     new Intl.NumberFormat("es-CO", {
      //       style: "currency",
      //       currency: "COP",
      //       maximumFractionDigits: 2,
      //     }).format(params.value ?? 0),
    },
    {
      field: "saldo_pendiente",
      headerName: "Saldo pendiente",
      flex: 1,
      //   valueFormatter: (params) =>
      //     new Intl.NumberFormat("es-CO", {
      //       style: "currency",
      //       currency: "COP",
      //       maximumFractionDigits: 2,
      //     }).format(params.value ?? 0),
    },
  ];

  useEffect(() => {
    return () => {
      setRows([]);
      setOpenModal(false);
      setSelectedRow(null);
    };
  }, []);

  return {
    onSubmit,
    rows,
    columns,
    openModal,
    handleOpenModal,
    handleCloseModal,
    selectedRow,
    onSubmitRegistroUser,
  };
}
