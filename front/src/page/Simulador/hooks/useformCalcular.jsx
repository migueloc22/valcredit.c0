import { useForm } from "react-hook-form";
import { useState, useEffect } from "react";

export function useFormCalcular(onSubmit) {
  const [planPagos, setPlanPagos] = useState(null);
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm({
    defaultValues: {
      valorSolicitado: "",
      numeroCuotas: "",
    },
  });

  const valorSolicitado = watch("valorSolicitado");
  const numeroCuotas = watch("numeroCuotas");

  // Calcular plan de pagos automáticamente
  useEffect(() => {
    if (valorSolicitado && numeroCuotas) {
      const valor = Number(valorSolicitado);
      const cuotas = Number(numeroCuotas);
      if (
        valor >= 100000 &&
        valor <= 100000000 &&
        cuotas >= 2 &&
        cuotas <= 24
      ) {
        const cuotaMensual = Math.round(valor / cuotas);
        setPlanPagos({
          valorTotal: valor,
          numeroCuotas: cuotas,
          cuotaMensual: cuotaMensual,
          totalAPagar: cuotaMensual * cuotas,
        });
      }
    } else {
      setPlanPagos(null);
    }
  }, [valorSolicitado, numeroCuotas]);

  const onSubmit2 = (data) => {
    console.log("Formulario Calcular enviado:", data);
    if (onSubmit) {
      onSubmit(data);
    }
  };

  return {
    register,
    handleSubmit,
    onSubmit2,
    errors,
    planPagos,
  };
}
