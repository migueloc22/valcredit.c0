import React, { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { get } from "../../../store";
export function useFormRegistro(onSubmitCallback) {
  const [tipoDocs, settipoDocs] = useState([]);
  const {
    register,
    handleSubmit,
    formState: { errors },
    watch,
  } = useForm({
    defaultValues: {
      tipoDocumento: "",
      numeroDocumento: "",
      nombres: "",
      apellidos: "",
      genero: "",
      fechaNacimiento: "",
      celular: "",
      correo: "",
    },
  });
  useEffect(() => {
    return () => {
      get("/v1/tipo_documentos/")
        .then((data) => {
          console.log("Fetched data:", data);
          if (tipoDocs.length === 0) {
            settipoDocs(data);
          }
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    };
  }, [tipoDocs]);

  //  const [fechaNacimiento, setfechaNacimiento] = useState(second)
  //   const fechaNacimiento = watch("fechaNacimiento");

  // Validar que sea mayor de 18 años
  const isAdult = (dateString) => {
    if (!dateString) return true;
    const birthDate = new Date(dateString);
    const today = new Date();
    const age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    if (
      monthDiff < 0 ||
      (monthDiff === 0 && today.getDate() < birthDate.getDate())
    ) {
      return age - 1 >= 18;
    }
    return age >= 18;
  };

  const onSubmit = (data) => {
    console.log("Formulario de registro enviado:", data);
    if (onSubmitCallback) {
      onSubmitCallback(data);
    }
  };

  return {
    register,
    handleSubmit,
    onSubmit,
    errors,
    isAdult,
    tiposDocumento: tipoDocs,
    generos: ["Masculino", "Femenino", "Otro"],
  };
}
