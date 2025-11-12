import { useFormCalcular } from "../hooks/useformCalcular.jsx";
import {
  Box,
  TextField,
  Button,
  Card,
  CardContent,
  Typography,
  Grid,
} from "@mui/material";

export const FormCalcular = ({ onSubmit }) => {
  const { register, handleSubmit, onSubmit2, errors } =
    useFormCalcular(onSubmit);

  return (
    <Box sx={{ p: 3, maxWidth: 600, mx: "auto" }}>
      <Card>
        <CardContent>
          <Typography variant="h5" gutterBottom>
            Simulador de Crédito
          </Typography>

          <form onSubmit={handleSubmit(onSubmit2)}>
            <Box sx={{ mb: 3 }}>
              {/* Valor Solicitado */}
              <TextField
                fullWidth
                type="number"
                label="Valor solicitado (COP)"
                placeholder="100000"
                {...register("valorSolicitado", {
                  required: "El valor es requerido",
                  min: {
                    value: 100000,
                    message: "Mínimo $100.000",
                  },
                  max: {
                    value: 100000000,
                    message: "Máximo $100.000.000",
                  },
                })}
                error={!!errors.valorSolicitado}
                helperText={errors.valorSolicitado?.message}
                sx={{ mb: 2 }}
              />

              {/* Número de Cuotas */}
              <TextField
                fullWidth
                type="number"
                label="Número de cuotas"
                placeholder="12"
                {...register("numeroCuotas", {
                  required: "El número de cuotas es requerido",
                  min: {
                    value: 2,
                    message: "Mínimo 2 cuotas",
                  },
                  max: {
                    value: 24,
                    message: "Máximo 24 cuotas",
                  },
                })}
                error={!!errors.numeroCuotas}
                helperText={errors.numeroCuotas?.message}
                sx={{ mb: 2 }}
              />
            </Box>

            <Button
              fullWidth
              variant="contained"
              color="primary"
              type="submit"
              sx={{ mb: 3 }}
            >
              Calcular
            </Button>
          </form>
        </CardContent>
      </Card>
    </Box>
  );
};
