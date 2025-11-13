import {
  Box,
  Typography,
  Grid,
  Modal,
  Card,
  CardContent,
  Button,
} from "@mui/material";
import React from "react";
import useSimulador from "./hooks/useSimulador.jsx";
import { FormCalcular, FormRegistroUser } from "./components";
import { DataGrid } from "@mui/x-data-grid";
import { esES } from "@mui/x-data-grid/locales";

export const Simulador = () => {
  const {
    onSubmit,
    rows,
    columns,
    openModal,
    handleCloseModal,
    handleOpenModal,
    onSubmitRegistroUser,
  } = useSimulador();

  return (
    <Box sx={{ p: 2, mt: 3, position: "relative", minHeight: "80vh" }}>
      <Typography variant="h4" gutterBottom>
        Simulador de Crédito
      </Typography>

      <Grid container spacing={3}>
        {/* Columna 1: Formulario */}
        <Grid item xs={12} md={6}>
          <FormCalcular onSubmit={onSubmit} />
        </Grid>

        {/* Columna 2: Tabla de resultados */}
        <Grid item xs={12} md={6}>
          {rows && rows.length > 0 && (
            <Box>
              <Box sx={{ height: 400, width: "100%" }}>
                <DataGrid
                  rows={rows}
                  columns={columns}
                  pageSize={5}
                  rowsPerPageOptions={[5, 10]}
                  localeText={
                    esES.components?.MuiDataGrid?.defaultProps?.localeText
                  }
                  autoHeight={false}
                  disableSelectionOnClick
                />
              </Box>
              {/* Botón fuera de la grilla */}
              <Button
                fullWidth
                variant="contained"
                color="success"
                size="large"
                onClick={() => handleOpenModal(rows[0])}
                sx={{ mt: 2 }}
              >
                ¡Lo quiero!
              </Button>
            </Box>
          )}
        </Grid>
      </Grid>

      {/* Modal con detalles de la cuota */}
      <Modal
        open={openModal}
        onClose={handleCloseModal}
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Card sx={{ width: 700, p: 2 }}>
          <CardContent>
            <FormRegistroUser
              onSubmit={onSubmitRegistroUser}
              handleCloseModal={handleCloseModal}
            />
          </CardContent>
        </Card>
      </Modal>
    </Box>
  );
};
