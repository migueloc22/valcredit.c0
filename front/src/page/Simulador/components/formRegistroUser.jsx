import React from "react";
import { Box, TextField, MenuItem, Button, Typography } from "@mui/material";
import { useFormRegistro } from "../hooks/useFormRegistro.jsx";

export const FormRegistroUser = ({ onSubmit, handleCloseModal }) => {
  const {
    register,
    handleSubmit,
    onSubmit: onSubmitForm,
    errors,
    isAdult,
    tiposDocumento,
    generos,
  } = useFormRegistro(onSubmit);

  return (
    <Box sx={{ p: 2 }}>
      <Typography variant="h6" gutterBottom>
        Registro de Usuario
      </Typography>

      <form onSubmit={handleSubmit(onSubmitForm)}>
        <Box
          sx={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: 2,
            mb: 2,
          }}
        >
          {/* Tipo de Documento */}
          <TextField
            select
            label="Tipo de documento"
            {...register("tipoDocumento", {
              required: "Selecciona un tipo de documento",
            })}
            error={!!errors.tipoDocumento}
            helperText={errors.tipoDocumento?.message}
          >
            <MenuItem value="">-- Selecciona --</MenuItem>
            {tiposDocumento.map((tipo) => (
              <MenuItem key={tipo.id} value={tipo.id}>
                {tipo.nombre}
              </MenuItem>
            ))}
          </TextField>

          {/* Número de Documento */}
          <TextField
            type="text"
            label="Número de documento"
            placeholder="1234567890"
            {...register("numeroDocumento", {
              required: "El número de documento es requerido",
              pattern: {
                value: /^\d+$/,
                message: "Solo se permiten números",
              },
              minLength: {
                value: 5,
                message: "Mínimo 5 dígitos",
              },
              maxLength: {
                value: 20,
                message: "Máximo 20 dígitos",
              },
            })}
            error={!!errors.numeroDocumento}
            helperText={errors.numeroDocumento?.message}
          />

          {/* Nombres */}
          <TextField
            type="text"
            label="Nombres"
            placeholder="Juan Carlos"
            {...register("nombres", {
              required: "Los nombres son requeridos",
              minLength: {
                value: 2,
                message: "Mínimo 2 caracteres",
              },
            })}
            error={!!errors.nombres}
            helperText={errors.nombres?.message}
          />

          {/* Apellidos */}
          <TextField
            type="text"
            label="Apellidos"
            placeholder="García López"
            {...register("apellidos", {
              required: "Los apellidos son requeridos",
              minLength: {
                value: 2,
                message: "Mínimo 2 caracteres",
              },
            })}
            error={!!errors.apellidos}
            helperText={errors.apellidos?.message}
          />

          {/* Género */}
          <TextField
            select
            label="Género"
            {...register("genero", {
              required: "Selecciona un género",
            })}
            error={!!errors.genero}
            helperText={errors.genero?.message}
          >
            <MenuItem value="">-- Selecciona --</MenuItem>
            {generos.map((gen) => (
              <MenuItem key={gen} value={gen}>
                {gen}
              </MenuItem>
            ))}
          </TextField>

          {/* Fecha de Nacimiento */}
          <TextField
            type="date"
            label="Fecha de nacimiento"
            InputLabelProps={{ shrink: true }}
            {...register("fechaNacimiento", {
              required: "La fecha de nacimiento es requerida",
              validate: (value) =>
                isAdult(value) || "Debes ser mayor de 18 años para registrarte",
            })}
            error={!!errors.fechaNacimiento}
            helperText={errors.fechaNacimiento?.message}
          />

          {/* Celular */}
          <TextField
            type="text"
            label="Celular"
            placeholder="3001234567"
            {...register("celular", {
              required: "El celular es requerido",
              pattern: {
                value: /^\d+$/,
                message: "Solo se permiten números",
              },
              minLength: {
                value: 10,
                message: "Mínimo 10 dígitos",
              },
              maxLength: {
                value: 13,
                message: "Máximo 13 dígitos",
              },
            })}
            error={!!errors.celular}
            helperText={errors.celular?.message}
          />

          {/* Correo Electrónico */}
          <TextField
            type="email"
            label="Correo electrónico"
            placeholder="usuario@example.com"
            {...register("correo", {
              required: "El correo es requerido",
              pattern: {
                value: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
                message: "Formato de correo inválido",
              },
            })}
            error={!!errors.correo}
            helperText={errors.correo?.message}
          />
        </Box>

        <Box
          sx={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: 2,
          }}
        >
          <Button fullWidth variant="contained" color="primary" type="submit">
            Registrarse
          </Button>
          <Button
            fullWidth
            variant="outlined"
            color="alert"
            onClick={handleCloseModal}
          >
            Cerrar
          </Button>
        </Box>
      </form>
    </Box>
  );
};
